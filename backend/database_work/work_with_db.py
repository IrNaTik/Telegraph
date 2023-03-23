from database import  metadata, engine, create_chat_messages_table, create_chat_messages_pagination_table, create_user_photos_table
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text
from sqlalchemy import exc
from .serializers import *

__all__ = 'db_provider'
class BaseDbWorkMixin():

    @staticmethod
    async def _add(table_name: str, arguments: dict):
        print(arguments)
        try:
            keys = f'{", ".join([key for key in arguments.keys()])}'

            values = [str(arguments[key]) if type(arguments[key]) == int else f"'{arguments[key]}'" for key in arguments.keys()]
            values = ', '.join(values)

            async with AsyncSession(engine) as session:
                statement = text(f"""INSERT INTO '{table_name}'({keys}) VALUES({values})""")
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
                statement = text(f"""SELECT * FROM user WHERE login = '{login}' """)
                user_object = await session.execute(statement)
                
                user_id = user_object.first().user_id
                return {'error': False, 'user_id': user_id}
            except AttributeError:
                return {'error': True, 'type': 'AttributeArror', 'message': 'No user with such login'}
            
    async def get_user_id_by_username(self, username):
        async with AsyncSession(engine) as session:
            try:
                statement = text(f"""SELECT * FROM user_parametres WHERE username = '{username}' """)
                user_object = await session.execute(statement)
                
                user_id = user_object.first().user_id
                return {'error': False, 'user_id': user_id}
            except AttributeError:
                return {'error': True, 'type': 'AttributeArror', 'message': 'No user with such username'}
            
        
    
    async def create_photos_table(self, user_login):
        table_name = (str(user_login) + '_' +'photos').lower()
        response = await create_user_photos_table(table_name, metadata, engine)
        return response

    async def add_photo(self, user_login, photo_path):
        table_name = (str(user_login) + '_' + 'photos').lower()
    
        photo_row = PhotoSerializer(photo_path) # Нужно редачить
        
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
            statement = text(f"""SELECT refresh_token FROM user_access_data WHERE user_id={user_id} """)
            user_object = await session.execute(statement)
            user_data = user_object.first()
            

        return user_data[0] # Have keys refresh_token and last_visit
    
    async def get_by_prefix(self, prefix):
        async with AsyncSession(engine) as session:
            statement = text(f"""SELECT * FROM user WHERE login LIKE '{prefix}%' LIMIT 10""")
            response = await self._execute_statement(statement, session)
            
            if response['error']:
                return response
            
            objects = response['response'].all()
            return objects


class ChatInstance():
    async def add_chat(self, user1_login, user2_login):
        
        user1_id = await db_provider.user.get_user_id_by_login(user1_login)
        user2_id = await db_provider.user.get_user_id_by_login(user2_login)
        

        if user1_id['error'] or user1_id['error']:
            return user1_id
        
        print(user1_id, user2_id)
        
        # Creating Chat_Instance
        response = await BaseDbWorkMixin._add('chat_instance', {'user_1': user1_id['user_id'], 'user_2': user2_id['user_id'], 'unreaden_message_id': 0})

        if response['error']:
            return response

        # Creating Chat_Messages table
        chat_name = (str(user1_login) + '_' + str(user2_login)).lower()
        await create_chat_messages_table(chat_name, metadata, engine)

        # Creating Pagination_table 
        # table_name = ('pagination_' + str(user1_login) + '_' + str(user2_login)).lower()
        # await create_chat_messages_pagination_table(table_name, metadata, engine)
        # await BaseDbWorkMixin._add(table_name, {'user_id': user1_id, 'message_id': 0}) # If message_id = 0 it means that it is last message
        # await BaseDbWorkMixin._add(table_name, {'user_id': user2_id, 'message_id': 0})

        print(response, 154)
        return response


    async def add_message(self, table_name, sender_username, content):
        sender_id = await db_provider.user.get_user_id_by_username(sender_username)

        if sender_id['error']:
            return sender_id
        
        print(sender_id['user_id'], content)
        message = MessageSerializer(sender_id['user_id'], content)

        if not message.is_valid:
            return message.error_data
        response = await BaseDbWorkMixin._add(table_name, {'sender_id': sender_id['user_id'], 'content': content})
        return response
        
    async def get_user_chats(self, user_login):
        user_id = await db_provider.user.get_user_id_by_login(user_login)

        if user_id['error']:
            return user_id
        
        async with AsyncSession(engine) as session:
            statement = text(f"""SELECT * FROM chat_instance WHERE user_1 = '{user_id['user_id']}' OR user_2 = '{user_id['user_id']}' """)
            print(statement)
            response = await BaseDbWorkMixin._execute_statement(statement, session)

            if response['error']:
                return response
            
            chat_objects = response['response'].all()

            return chat_objects
        
    
    async def get_chat_messages(self, table_name, message_id): # Возвращает 25 сообщений, начиная с определённого
        async with AsyncSession(engine) as session:
            
            statement = text(f'''SELECT * FROM '{table_name}' ORDER BY message_id DESC LIMIT 1;''')
            response = await BaseDbWorkMixin._execute_statement(statement, session)
            
            
            if response['error']:
                return response
            
            last_message_id = response['response'].first()
            last_message_id = last_message_id.message_id
            print(last_message_id)

            statement = text(f'''SELECT * from '{table_name}' WHERE message_id <= {last_message_id - message_id+1}  ORDER BY message_id DESC
                                   LIMIT 5;''')

            print(statement) 
            response = await BaseDbWorkMixin._execute_statement(statement, session)
            if response['error']:
                return response
            
            messages = response['response'].all()

            return messages

class WorkWithDatabase():
    def __init__(self) -> None:
        self.user = UserInstance()
        self.chat = ChatInstance()

    async def create_tables(self): 
        async with engine.begin() as conn:
            await conn.run_sync(metadata.create_all)

db_provider = WorkWithDatabase()

