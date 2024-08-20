from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm.session import sessionmaker

def dbcreate():
    db_name = 'CLINISOFTWB'
    db_user = 'postgres'
    db_pass = '123'
    db_host = 'localhost'
    db_port = '5432'

    try:
        db_string = f'postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'
        engine = create_engine(db_string,pool_size=100, max_overflow=20)
        return engine
    except Exception as ex:
        return print(str(ex), ": Error")
    
engine = dbcreate()
meta_data = MetaData()

SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 


Base=declarative_base()