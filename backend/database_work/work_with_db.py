from database import metadata, engine, create_chat_messages_table, create_user_photos_table
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text
from sqlalchemy import exc
from .serializers import *
from datetime import datetime


__all__ = 'db_provider'


class BaseDbWorkMixin():

    @staticmethod
    async def _add(table_name: str, arguments: dict):
        print(arguments)
        try:
            keys = f'{", ".join([key for key in arguments.keys()])}'

            values = [str(arguments[key]) if type(arguments[key]) ==
                      int else f"'{arguments[key]}'" for key in arguments.keys()]
            values = ', '.join(values)

            async with AsyncSession(engine) as session:
                statement = text(
                    f"""INSERT INTO '{table_name}'({keys}) VALUES({values})""")
                print(statement)
                await session.execute(statement)
                await session.commit()

            return {'error': False}
        except Exception as e:
            return {'error': True, 'type': f'{type(e)}', 'message': e}

    @staticmethod
    async def _execute_statement(statement, session):
        try:
            response = await session.execute(statement)
            await session.commit()
            return {'error': False, 'response': response}
        except Exception as e:
            return {'error': True, 'type': f'{type(e)}', 'message': e}


class UserInstance(BaseDbWorkMixin):
    async def add_user(self, login, password, username):
        new_user = UserSerializer(login, password)

        if new_user.is_valid:
            user = await BaseDbWorkMixin._add('user', {'login': login, 'password': password})
            print(user)
            if not user['error']:
                user_id = await db_provider.user.get_user_id_by_login(login)
                await BaseDbWorkMixin._add('user_access_data', {'user_id': user_id['user_id'], 'last_visit': 'null', 'refresh_token': 'null'})
                resp = await BaseDbWorkMixin._add('user_parametres', {'user_id': user_id['user_id'], 'username': username, 'description': 'null'})

                if not resp['error']:
                    return {'error': False, 'user_id': user_id}
                else:
                    return resp
            else:
                return user

        return new_user.error_data

    async def get_user_id_by_login(self, login):
        async with AsyncSession(engine) as session:
            try:
                statement = text(
                    f"""SELECT * FROM user WHERE login = '{login}' """)
                user_object = await session.execute(statement)

                user_id = user_object.first().user_id
                return {'error': False, 'user_id': user_id}
            except AttributeError:
                return {'error': True, 'type': 'AttributeArror', 'message': 'No user with such login'}

    async def get_user_id_by_username(self, username):
        async with AsyncSession(engine) as session:
            try:
                statement = text(
                    f"""SELECT * FROM user_parametres WHERE username = '{username}' """)
                user_object = await session.execute(statement)

                user_id = user_object.first().user_id
                return {'error': False, 'user_id': user_id}
            except AttributeError:
                return {'error': True, 'type': 'AttributeArror', 'message': 'No user with such username'}

    async def create_photos_table(self, user_login):
        table_name = (str(user_login) + '_' + 'photos').lower()
        response = await create_user_photos_table(table_name, metadata, engine)
        return response

    async def add_photo(self, user_login, photo_path):
        table_name = (str(user_login) + '_' + 'photos').lower()

        photo_row = PhotoSerializer(photo_path)  # Нужно редачить

        if photo_row.is_valid:
            new_photo = await BaseDbWorkMixin._add(table_name, {'photo_path': photo_path})

            if new_photo['error']:
                return new_photo

        return photo_row.error_data

    async def update_access_data_table(self, user_id, last_visit, refresh_token):

        async with AsyncSession(engine) as session:
            statement = text(f'''UPDATE user_access_data
                                 SET last_visit = '{last_visit}', refresh_token='{refresh_token}'
                                 WHERE user_id = {user_id};''')
            response = await self._execute_statement(statement, session)
            return response

    async def get_access_data_table(self, user_id):
        async with AsyncSession(engine) as session:
            statement = text(
                f"""SELECT refresh_token FROM user_access_data WHERE user_id={user_id} """)
            user_object = await session.execute(statement)
            user_data = user_object.first()

        return user_data  # Have keys refresh_token and last_visit

    async def get_by_prefix(self, prefix):
        async with AsyncSession(engine) as session:
            statement = text(
                f"""SELECT * FROM user WHERE login LIKE '{prefix}%' LIMIT 10""")
            response = await self._execute_statement(statement, session)

            if response['error']:
                return response

            objects = response['response'].all()
            return objects


class ChatInstance():
    async def add_chat(self, user1_id, user2_id):
        async with AsyncSession(engine) as session:
            statement = text(
                f"""SELECT user_1, user_2 FROM chat_instance WHERE (user_1 = '{user1_id}' AND user_2 = '{user2_id}') OR (user_1 = '{user2_id}' AND user_2 = '{user1_id}')""")
            print(statement)
            response = await BaseDbWorkMixin._execute_statement(statement, session)
            if response['error']:
                return response

        if response['error']:
            return response

        obj = response['response'].first()
        if obj == None:
            # Creating Chat_Instance
            response = await BaseDbWorkMixin._add('chat_instance', {'user_1': user1_id, 'user_2': user2_id, 'date': str(datetime.utcnow())})
            if response['error']:
                return response
            print(response)

            # Creating Chat_Messages table
            chat_name = (str(user1_id) + '_' + str(user2_id)).lower()
            await create_chat_messages_table(chat_name, metadata, engine)

            response['isNewChat'] = True
            response['chat_name'] = chat_name
            return response

        response['chat_name'] = f'{obj[0]}_{obj[1]}'
        response['isNewChat'] = False
        return response

    async def add_message(self, table_name: str, sender_username: str, content: str):
        sender_id = await db_provider.user.get_user_id_by_username(sender_username)

        if sender_id['error']:
            return sender_id

        print(sender_id['user_id'], content)
        message = MessageSerializer(sender_id['user_id'], content)

        if not message.is_valid:
            return message.error_data
        response = await BaseDbWorkMixin._add(table_name, {'sender_id': sender_id['user_id'], 'content': content, 'date': str(datetime.utcnow()), 'is_readen': False})
        return response

    async def get_user_chats(self, username):
        user_id = await db_provider.user.get_user_id_by_username(username)

        if user_id['error']:
            return user_id

        async with AsyncSession(engine) as session:
            statement = text(
                f"""SELECT * FROM chat_instance WHERE user_1 = '{user_id['user_id']}' OR user_2 = '{user_id['user_id']}' """)
            print(statement)
            response = await BaseDbWorkMixin._execute_statement(statement, session)

            if response['error']:
                return response

            chat_objects = response['response'].all()

            return chat_objects

    # Возвращает 25 сообщений, начиная с определённого
    async def get_chat_messages(self, table_name: str, start: int) -> None:

        async with AsyncSession(engine) as session:

            statement = text(
                f'''
                    SELECT sender_id, content, date, is_readen
                    FROM "{table_name}"
                    WHERE message_id < {start}
                    ORDER BY message_id DESC
                    LIMIT 25
                ''')
            response = await BaseDbWorkMixin._execute_statement(statement, session)
            print(statement)

            if response['error']:
                return response

            messages = list(response['response'].all())
            messages = ([{"sender_id": message[0],
                          "content": message[1],
                          'date': message[2],
                          'is_readen': message[3]
                          }
                         for message in messages])

            return messages


class WorkWithDatabase():
    def __init__(self) -> None:
        self.user = UserInstance()
        self.chat = ChatInstance()

    async def create_tables(self):
        async with engine.begin() as conn:
            await conn.run_sync(metadata.create_all)


db_provider = WorkWithDatabase()
