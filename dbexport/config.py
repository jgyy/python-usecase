# $Env:DB_URL="postgres://jgyy:jgyy@13.229.62.87:80/reviews"
# $Env:PYTHONPATH="."
# python .\dbexport\config.py
import os
from functools import lru_cache

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


@lru_cache(maxsize=32)
def engine(db_url=None):
    db_url = db_url or os.getenv("DB_URL")
    if not db_url:
        raise ValueError("database URL is required")
    return create_engine(db_url)


def get_connection(db_url=None):
    return engine(db_url).connect()


@lru_cache(maxsize=32)
def session_class(db_url=None):
    return sessionmaker(bind=engine(db_url))


if __name__ == "__main__":
    os.environ["DB_URL"] = "postgres://jgyy:jgyy@13.229.62.87:80/reviews"
    db = get_connection()
    print(id(engine()))
    print(engine() is engine(None))
    result = db.execute("SELECT count(id) FROM reviews")
    row = result.first()
    print(row[0])

    Session = session_class()
    session = Session()
    print(session)
    print(session.bind)
