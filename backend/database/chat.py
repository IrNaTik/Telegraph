
import sqlalchemy as sa

from .base import Base
from .user import User

class Chat_Instance(Base):
    __tablename__ = 'chat_instance'

    chat_id = sa.Column('chat_id', sa.Integer, primary_key=True)
    user_1 = sa.Column('user_1', sa.Integer, sa.ForeignKey('user.user_id'), nullable=False) 
    user_2 = sa.Column('user_2', sa.Integer, sa.ForeignKey('user.user_id'), nullable=False)


def create_chat_messages_table(table_name, metadata, engine):
    
    table_object = sa.Table(table_name, metadata, 
                            sa.Column('message_id', sa.Integer, primary_key=True, nullable=False),
                            sa.Column('sender_id', sa.ForeignKey('user.user_id'), nullable=False),
                            sa.Column('content', sa.TEXT, nullable=False))
    metadata.create_all(engine)
    
    return "Good"





# class Chat_Messages(Base):
#     # def __new__(cls, *args, **kwargs):
#     #     print('Something')
#     # def __init__(self, user1_id: str, user2_id: str) -> None:
#     #     print('Baaaad')
#     #     Chat_Messages.__tablename__ = str(user1_id) + "_" + str(user2_id)
    
#     __tablename__ = "chat_messages"
#     message_id = sa.Column('message_id', sa.Integer, sa.ForeignKey('chat_instance.chat_id'), primary_key=True, nullable=False)
#     sender = sa.Column('sender_id', sa.ForeignKey('user.user_id'), nullable=False)
#     content = sa.Column('content', sa.TEXT, nullable=False)



        