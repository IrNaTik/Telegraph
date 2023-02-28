from sqlalchemy import create_engine, MetaData

from apps.settings import config
from apps.auth.models import user

DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"

def create_tables(engine):
    meta = MetaData()
    meta.create_all(bind=engine, tables=[user])


def sample_data(engine):
    con = engine.connect()
    con.execute(user.insert(), {"id": 1, 'name': "tihon"})
    con.close()


if __name__ == '__main__':
    db_url = DSN.format(**config['postgres'])
    engine = create_engine(db_url)

    create_tables(engine)
    sample_data(engine)