"""import

    from dbSessionCreator import Base
    from dbSessionCreator import engine
    from models import *

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import pyodbc

SQL_URL = 'mssql+pyodbc://richard_koch:0ptZeciD0u@z3c1@python-internship-server.database.windows.net/python_internship_sample?driver=SQL Server'
# SQL_URL = 'mssql+pyodbc://@HCP05\SQLEXPRESS/test'

engine = create_engine(
    SQL_URL
)


# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
with engine.connect() as connection:
    print("sunt connectat")


# db = SessionLocal()

