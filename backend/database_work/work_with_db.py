from database import Chat_Instance, User, metadata, engine, create_chat_messages_table
from sqlalchemy.orm import Session, mapper
from sqlalchemy import Table, or_
from sqlalchemy.sql import text

__all__ = 'db_provider'

class WorkWithDatabase():
    def __init__(self, engine, metadata) -> None:
        self.engine = engine
        self.metadata = metadata

        self.create_tables()

    def create_tables(self):
        self.metadata.create_all(self.engine)
        
        # for i in range(10):
        #     response = get_chat_messages_table(f'{i}', metadata)
        # metadata.create_all(engine)
        # current_session.add(user)

    def add_user(self, login, password):
        
        with Session(engine) as session:
            user = User(login=login, password=password)
            session.add(user)
            session.commit()
    
    def get_user_id(self, login):
        with Session(engine) as session:
            user_object = session.query(User).filter(User.login == login).first()
            user_id = user_object.user_id
        return user_id
    

    def add_chat(self, user1_login, user2_login):
        
        user1_id = self.get_user_id(user1_login)
        user2_id = self.get_user_id(user2_login)

        if not user1_id or not user2_id:
            print('No user with such login')
            return 'No user with such login'
        
        # Creating Chat_Instance
        with Session(engine) as session:
            user = Chat_Instance(user_1=user1_id, user_2=user2_id)
            session.add(user)
            session.commit()

        # Creating Chat_Messages table
        chat_name = (str(user1_login) + '_' + str(user2_login)).lower()
        create_chat_messages_table(chat_name, metadata, engine)


    def add_message(self, table_name, sender_login, content):
        
        sender_id = self.get_user_id(sender_login)
        with engine.connect() as con:
            data = ( { "sender_id": sender_id, "content": content },)
            statement = text(f"""INSERT INTO {table_name}(sender_id, content) VALUES(:sender_id, :content)""")

            for line in data:
                con.execute(statement, **line)

    def get_user_chats(self, user_login):
        user_id = self.get_user_id(user_login)
        with Session(engine) as session:
            chat_objects = session.query(User).filter(or_(Chat_Instance.user_1 == user_id, Chat_Instance.user_2 == user_id)).all()

        return chat_objects # Объекты чатов
    
    def get_chat_messages(self, table_name):
        print(metadata)
        with engine.connect() as con:
            
            statement = text(f"""SELECT * FROM {table_name}""")
            message_objects = con.execute(statement)
            print(message_objects)
            for row in message_objects:
                print(row)
        return message_objects
    
db_provider = WorkWithDatabase(engine, metadata)