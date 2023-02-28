from sqlalchemy import (Column, String, Integer, Date, ForeignKey,
                        MetaData, Table)

meta = MetaData()

__all__ = ['user']

user = Table(
    'user', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String)
)

