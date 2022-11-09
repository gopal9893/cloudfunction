from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLALCHEMY_DB_URL= mysql.connector.connect(host='localhost',user='root', passwd='root',db='first_db')
SQLALCHEMY_DB_URL = 'mysql://root:easyaspataal123@35.244.61.133:3306/ea-dbprod'
engine = create_engine(SQLALCHEMY_DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


