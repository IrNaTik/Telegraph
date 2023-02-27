from sqlalchemy import (Column, String, Integer, Date, ForeignKey,
                        MetaData, Table)

meta = MetaData()

user = Table(
    'user', meta,
    Column('id', Integer, primary_key=True)
)