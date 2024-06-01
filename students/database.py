from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker, declarative_base

SQL_DATABASE_URL = "sqlite:///./sql_app.db"

engine =  create_engine(SQL_DATABASE_URL, connect_args={"check_same_thrad": False})
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_session() -> Session:
    session = Session()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
    finally:
        session.close()

