# user data table

import sqlalchemy as sa
from .base import Base

class User(Base):
    __tablename__ =  "user"

    user_id = sa.Column('user_id', sa.Integer, primary_key=True)
    login = sa.Column(sa.TEXT, nullable=False, unique=True)
    password = sa.Column(sa.TEXT,  nullable=False)

class UserParametres(Base):
    __tablename__ = "user_parametres"

    user_id = sa.Column('user_id', sa.Integer, primary_key=True)
    username = sa.Column(sa.TEXT, nullable=False, unique=True)
    description = sa.Column(sa.TEXT, nullable=True)

class UserAccessData(Base):
    __tablename__ = "user_access_data"

    user_id = sa.Column('user_id', sa.Integer, primary_key=True)
    last_visit = sa.Column(sa.TEXT, nullable=False)
    refresh_token = sa.Column(sa.TEXT, nullable=False)

async def create_user_photos_table(table_name, metadata, engine):
    table_object = sa.Table(table_name, metadata, 
                            sa.Column('photo_path', sa.TEXT, nullable=False),
                            )
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)



