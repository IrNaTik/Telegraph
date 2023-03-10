from database import  metadata, engine, create_chat_messages_table, create_chat_messages_pagination_table, create_user_photos_table
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text

__all__ = 'db_provider'

class UserInstance():
    async def add_user(self, login, password):
        
        async with AsyncSession(engine) as session:
            statement = text(f"""INSERT INTO user(login, password) VALUES('{login}', '{password}')""")
            await session.execute(statement)
            await session.commit()
    
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
        
        async with AsyncSession(engine) as session:
            statement = text(f"""INSERT INTO {table_name} (photo_path) VALUES('{photo_path}')""")
            
            await session.execute(statement)
            await session.commit() 

    async def update_access_data_table(self, user_login, last_visit, refresh_token):
        user_id = await db_provider.user.get_user_id(user_login)
        async with AsyncSession(engine) as session:
            statement = text(f"""INSERT INTO user_access_data (last_visit, refresh_token) VALUES({last_visit}, {refresh_token})""")
            
            await session.execute(statement)
            await session.commit() 
        f'''UPDATE user_access_data
        SET last_visit = {last_visit}, refresh_token= {refresh_token}
        WHERE user_id = {user_id};'''

    async def get_access_data_table(self, user_login):
        user_id = await db_provider.user.get_user_id(user_login)
        async with AsyncSession(engine) as session:
            statement = text(f"""SELECT * FROM user WHERE user_id = '{user_id}' """)
            user_object = await session.execute(statement)
            user_data = user_object.first()

        return user_data # Have keys refresh_token and last_visit


class ChatInstance():
    async def add_chat(self, user1_login, user2_login):
        
        user1_id = await db_provider.user.get_user_id(user1_login)
        user2_id = await db_provider.user.get_user_id(user2_login)

        if not user1_id or not user2_id:
            print('No user with such login')
            return 'No user with such login'
        
        # Creating Chat_Instance
        async with AsyncSession(engine) as session:
            # user = Chat_Instance(user_1=user1_id, user_2=user2_id)
            statement = text(f"""INSERT INTO chat_instance(user_1, user_2) VALUES({user1_id}, {user2_id})""")
            await session.execute(statement)
            await session.commit()

        # Creating Chat_Messages table
        chat_name = (str(user1_login) + '_' + str(user2_login)).lower()
        await create_chat_messages_table(chat_name, metadata, engine)

        # Creating Pagination_table 
        table_name = ('pagination_' + str(user1_login) + '_' + str(user2_login)).lower()
        await create_chat_messages_pagination_table(table_name, metadata, engine)

        async with AsyncSession(engine) as session:
            
            statements = (text(f"""INSERT INTO {table_name}(user_id, message_id) VALUES({user1_id}, 0)"""), # If message_id = 0 it means that it is last message
                          text(f"""INSERT INTO {table_name}(user_id, message_id) VALUES({user2_id}, 0)"""))
            
            for statement in statements:
                await session.execute(statement)

            await session.commit()


    async def add_message(self, table_name, sender_login, content):
        
        sender_id = await db_provider.user.get_user_id(sender_login)
        async with AsyncSession(engine) as session:
            data = ( { "sender_id": sender_id, "content": content },)
            statement = text(f"""INSERT INTO {table_name} (sender_id, content) VALUES({sender_id}, '{content}')""")
            
            await session.execute(statement)
            await session.commit() # It's important!!!
        

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
    
    async def get_chat_messages(self, table_name):
        print(metadata)
        async with engine.connect() as con:
            
            
            # statement = text(f"""SELECT * FROM {table_name} ORDER BY message_id DESC WHERE message_id >= {} """) # Сделать пагинацию 
            statement = text(f"""SELECT * FROM {table_name}""") 
            message_objects = await con.execute(statement)
            # print(message_objects)
            messages = []
            for row in message_objects:
                messages.append(row)
        return messages

class WorkWithDatabase():
    def __init__(self) -> None:
        self.user = UserInstance()
        self.chat = ChatInstance()

    async def create_tables(self): 
        async with engine.begin() as conn:
            await conn.run_sync(metadata.create_all)


    
db_provider = WorkWithDatabase()

