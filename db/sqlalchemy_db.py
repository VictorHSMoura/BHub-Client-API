from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_PATH = "sqlite:///database.db"

""" Create sqlalchemy engine. """
engine = create_engine(DATABASE_PATH)

""" Declares data mapping. """
Base = declarative_base()

""" Creates sqlalchemy session for DB. """
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db_instance():
    """ Returns a DB instance and closes the DB after finishing using it. """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
