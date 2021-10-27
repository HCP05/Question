"""import

    from dbSessionCreator import Base
    from dbSessionCreator import engine
    from models import *

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.engine import URL
# SQL_URL = 'mssql+pyodbc://user:password@server/database'
# SQL_URL = 'mssql+pyodbc://@HCP05\SQLEXPRESS/test'

connection_url = URL.create(
    "mssql+pyodbc",
    host="HCP05\SQLEXPRESS",
    database="test",
    query={
        "driver": "OLEDBC Driver 19 for SQL Server",
        "authentication": "ActiveDirectoryIntegrated",
    },
)
engine = create_engine(
    connection_url
)

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
with engine.connect():
    select('table_name')



# db = SessionLocal()

