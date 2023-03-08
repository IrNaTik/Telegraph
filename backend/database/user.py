# user data table

import sqlalchemy as sa
from .base import Base

class User(Base):
    __tablename__ =  "user"

    user_id = sa.Column('user_id', sa.Integer, primary_key=True)
    login = sa.Column(sa.TEXT, nullable=False, unique=True)
    password = sa.Column(sa.TEXT,  nullable=False)
