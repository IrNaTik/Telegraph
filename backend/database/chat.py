
import sqlalchemy as sa
from .base import Base
from .user import User

class Chat_Instance(Base):
    __tablename__ = 'chat_instance'

    id = sa.Column('chat_id', sa.Integer, primary_key=True)
    user_1 = sa.Column('user_1', sa.Integer, sa.ForeignKey(User.id), nullable=False) 
    user_2 = sa.Column('user_2', sa.Integer, sa.ForeignKey(User.id), nullable=False)


class Chat_Messages(Base):
    def __init__(self, user1_id: str, user2_id: str) -> None:
        print('Baaaad')
        Chat_Messages.__tablename__ = str(user1_id) + "_" + str(user2_id)
    

    id = sa.Column('message_id', sa.Integer, sa.ForeignKey(Chat_Instance.id), nullable=False)
    sender = sa.Column('sender_id', sa.ForeignKey(User.id), nullable=False)
    content = sa.Column('content', sa.TEXT, nullable=False)
        