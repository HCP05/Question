from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import pyodbc

SQL_URL = 'mssql+pyodbc://richard_koch:0ptZeciD0u@z3c1@python-internship-server.database.windows.net/python_internship_sample?driver=SQL Server'
# SQL_URL = 'mssql+pyodbc://@HCP05\SQLEXPRESS/test?driver=SQL Server'

engine = create_engine(
    SQL_URL
)

Base = declarative_base()

