import aiopg.sa

from sqlalchemy import (Column, String, Integer, Date, ForeignKey,
                        MetaData, Table)

meta = MetaData()

__all__ = ['user']

user = Table(
    'user', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String)
)

async def pg_context(app):
    conf = app['config']['postgres']
    engine = await aiopg.sa.create_engine(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'],
        port=conf['port'],
        minsize=conf['minsize'],
        maxsize=conf['maxsize'],
    )

    app['db'] = engine

    yield

    app['db'].close()
    await app['db'].wait_closed()