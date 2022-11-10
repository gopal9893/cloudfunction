"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import mysql.connector
#SQLALCHEMY_DB_URL= mysql.connector.connect(host='35.244.61.133',user='root', passwd='easyaspataal123',db='ea-dbprod')
SQLALCHEMY_DB_URL = 'mysql://root:easyaspataal123@35.244.61.133:3306/ea-dbprod'
engine = create_engine(SQLALCHEMY_DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
"""


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from google.cloud.sql.connector import Connector

# Python Connector database connection function
def getconn():
    with Connector() as connector:
        conn = connector.connect(
            "/cloudsql/effective-aria-346508:asia-south1:ea-prod", # Cloud SQL Instance Connection Name
            "pg8000",
            user="root",
            password="easyaspataal123",
            db="ea-dbprod",
            ip_type= "35.244.61.133"  # IPTypes.PRIVATE for private IP
        )
    return conn

SQLALCHEMY_DATABASE_URL = "postgresql+pg8000://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL , creator=getconn
)

# create SQLAlchemy ORM session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

