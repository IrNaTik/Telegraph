import aiopg.sa

from sqlalchemy import create_engine, MetaData

from apps.settings import config
from apps.auth.models import user

DSN = "postgresql+psycopg2://postgres:postgresг@{host}:{port}/{database}"

def create_tables(engine):

    # meta = MetaData()
    user.create(engine)

    




def sample_data(engine):
    con = engine.connect()
    con.execute(user.insert(), {"id": 1, 'name': "tihon"})
    con.close()


if __name__ == '__main__':
    db_url = DSN.format(**config['postgres'])
    engine = create_engine(db_url)

    print(engine)
    # create_tables(engine)
    sample_data(engine)


async def pg_context(app):
    conf = app['config']['postgres']
    engine = await aiopg.sa.create_engine(
        database=conf['database'],
        user=conf['user'],
        password=conf['password'],
        host=conf['host'] await app['db'].wait_closed(),
        port=conf['port'],
        minsize=conf['minsize'],
        maxsize=conf['maxsize'],
    )

    app['db'] = engine

    yield

    app['db'].close()
    await app['db'].wait_closed()