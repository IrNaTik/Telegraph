from database import Chat_Instance, User, metadata, engine, create_chat_messages_table, create_chat_messages_pagination_table
from sqlalchemy.orm import Session, mapper
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Table, or_
from sqlalchemy.sql import text

__all__ = 'db_provider'

class WorkWithDatabase():
    def __init__(self, engine, metadata) -> None:
        self.engine = engine
        self.metadata = metadata

        


        # for i in range(10):
        #     response = get_chat_messages_table(f'{i}', metadata)
        # metadata.create_all(engine)
        # current_session.add(user)

    async def create_tables(self):
        
        async with engine.begin() as conn:
            await conn.run_sync(metadata.create_all)

    async def add_user(self, login, password):
        
        async with AsyncSession(engine) as session:
            # user = User(login=login, password=password)
            
            statement = text(f"""INSERT INTO user(login, password) VALUES('{login}', '{password}')""")
            await session.execute(statement)
            await session.commit()
    
    async def get_user_id(self, login):
        async with AsyncSession(engine) as session:
            statement = text(f"""SELECT * FROM user WHERE login = '{login}' """)
            user_object = await session.execute(statement)
            
            user_id = user_object.first().user_id
            
                #user_id = user.user_id
            # async for row in user_object:
            #     user_id = row.user_id
            # user_object = await session.query(User).filter(User.login == login).first()
            
        return user_id
    

    async def add_chat(self, user1_login, user2_login):
        
        user1_id = await self.get_user_id(user1_login)
        user2_id = await self.get_user_id(user2_login)

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
        
        sender_id = await self.get_user_id(sender_login)
        async with AsyncSession(engine) as session:
            data = ( { "sender_id": sender_id, "content": content },)
            statement = text(f"""INSERT INTO {table_name} (sender_id, content) VALUES({sender_id}, '{content}')""")
            
            await session.execute(statement)
            await session.commit() # It's important!!!
        

    async def get_user_chats(self, user_login):
        user_id = await self.get_user_id(user_login)
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
    
db_provider = WorkWithDatabase(engine, metadata)
