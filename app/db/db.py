from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base, sessionmaker
import dotenv


class mySqlManager:
    
    def __init__(self) -> None:
        self._session = self._establish_db_connection()
        
    def _establish_db_connection(self):
        DATABASE = 'testDB'
        USER = 'admin'
        PASSWORD = 'password'
        HOST = 'localhost'
        PORT = '3306'
        DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
        
        engine = create_engine(DATABASE_URL)
        Session = sessionmaker(bind=engine)
        session = Session()
        
        return session
    
    def insert_user_data