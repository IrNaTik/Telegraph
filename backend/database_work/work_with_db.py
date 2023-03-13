from database import  metadata, engine, create_chat_messages_table, create_chat_messages_pagination_table, create_user_photos_table
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text
from sqlalchemy import exc

__all__ = 'db_provider'
class BaseDbWorkMixin():

    @staticmethod
    async def _add(table_name: str, arguments: dict):
        try:
            keys = f'{", ".join([key for key in arguments.keys()])}'

            values = [str(arguments[key]) if type(arguments[key]) == int else f"'{arguments[key]}'" for key in arguments.keys()]
            values = ', '.join(values)

            async with AsyncSession(engine) as session:
                statement = text(f"""INSERT INTO {table_name}({keys}) VALUES({values})""")
                await session.execute(statement)
                await session.commit()

        except exc.IntegrityError:
            print("user is exists in table")        


class UserInstance(BaseDbWorkMixin):
    async def add_user(self, login, password):  
        await BaseDbWorkMixin._add('user', {'login': login, 'password': password})
        user_id = await db_provider.user.get_user_id(login)
        await BaseDbWorkMixin._add('user_access_data', {'user_id': user_id, 'last_visit': 'null', 'refresh_token': 'null'})
        await BaseDbWorkMixin._add('user_parametres', {'user_id': user_id, 'username': 'null', 'description': 'null'})


    async def get_user_id(self, login):
        async with AsyncSession(engine) as session:
            statement = text(f"""SELECT * FROM user WHERE login = '{login}' """)
            user_object = await session.execute(statement)
            
            user_id = user_object.first().user_id
            
        return user_id
    
    async def create_photos_table(self, user_login):
        table_name = (str(user_login) + '_' +'photos').lower()
        await create_user_photos_table(table_name, metadata, engine)

    async def add_photo(self, user_login, photo_path):
        table_name = (str(user_login) + '_' + 'photos').lower()
        await BaseDbWorkMixin._add(table_name, {'photo_path': photo_path})

    async def update_access_data_table(self, user_login, last_visit, refresh_token):
        user_id = await db_provider.user.get_user_id(user_login)

        async with AsyncSession(engine) as session:
            statement = text(f'''UPDATE user_access_data
                                 SET last_visit = '{last_visit}', refresh_token='{refresh_token}'
                                 WHERE user_id = {user_id};''')
            
            await session.execute(statement)
            await session.commit() 
        
    async def get_access_data_table(self, user_id):

        async with AsyncSession(engine) as session:
            statement = text(f"""SELECT * FROM user_access_data WHERE user_id = {user_id} """)
            user_object = await session.execute(statement)
            user_data = user_object.first()

        return user_data # Have keys refresh_token and last_visit
    
    async def get_by_prefix(self, prefix):
        async with AsyncSession(engine) as session:
            statement = text(f"""SELECT * FROM user WHERE login LIKE '{prefix}%' LIMIT 10""")
            objects = await session.execute(statement)
            objects = objects.all()
            return objects


class ChatInstance():
    async def add_chat(self, user1_login, user2_login):
        
        user1_id = await db_provider.user.get_user_id(user1_login)
        user2_id = await db_provider.user.get_user_id(user2_login)

        if not user1_id or not user2_id:
            print('No user with such login')
            return 'No user with such login'
        
        # Creating Chat_Instance
        await BaseDbWorkMixin._add('chat_instance', {'user_1': user1_id, 'user_2': user2_id})

        # Creating Chat_Messages table
        chat_name = (str(user1_login) + '_' + str(user2_login)).lower()
        await create_chat_messages_table(chat_name, metadata, engine)

        # Creating Pagination_table 
        table_name = ('pagination_' + str(user1_login) + '_' + str(user2_login)).lower()
        await create_chat_messages_pagination_table(table_name, metadata, engine)

        await BaseDbWorkMixin._add(table_name, {'user_id': user1_id, 'message_id': 0}) # If message_id = 0 it means that it is last message
        await BaseDbWorkMixin._add(table_name, {'user_id': user2_id, 'message_id': 0})


    async def add_message(self, table_name, sender_login, content):
        sender_id = await db_provider.user.get_user_id(sender_login)
        await BaseDbWorkMixin._add(table_name, {'sender_id': sender_id, 'content': content})
        
    async def get_user_chats(self, user_login):
        user_id = await db_provider.user.get_user_id(user_login)
        async with AsyncSession(engine) as session:
            statement = text(f"""SELECT * FROM chat_instance WHERE user_1 = '{user_id}' OR user_2 = '{user_id}' """)
            chat_objects_future = await session.execute(statement)
            chat_objects = chat_objects_future.all()

            user_chats = []
            for row  in chat_objects:
                user_chats.append(row)

        return user_chats # Объекты чатов
    
    async def get_chat_messages(self, table_name, message_id): # Возвращает 25 сообщений, начиная с определённого
        async with engine.connect() as con:

            statement = text(f'''SELECT user_id from user ORDER BY user_id DESC
                                 LIMIT 25 ;''')
            last_user = await con.execute(statement)
            
            last_user_id = last_user.first().user_id

            statement = text(f'''SELECT user_id from user WHERE user_id <= {last_user_id - message_id}  ORDER BY user_id DESC
                                   LIMIT 25;''')
            
            user_objects = await con.execute(statement)
            users = user_objects.all()

        return users

class WorkWithDatabase():
    def __init__(self) -> None:
        self.user = UserInstance()
        self.chat = ChatInstance()

    async def create_tables(self): 
        async with engine.begin() as conn:
            await conn.run_sync(metadata.create_all)

db_provider = WorkWithDatabase()

