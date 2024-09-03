from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Создаем базу данных и определяем базовый класс
Base = declarative_base()
DATABASE_URL = 'sqlite:///ServerGet/database/database.db'  # Используем SQLite для простоты

# Определяем модель таблицы GetServerGlobal
class GetServerGlobal(Base):
    __tablename__ = 'get_server_global'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    request_time = Column(DateTime, default=datetime.datetime.utcnow)
    client_ip = Column(String)
    client_port = Column(Integer)
    server_ip = Column(String)
    server_port = Column(Integer)

# Определяем модель таблицы GetServerLocal
class GetServerLocal(Base):
    __tablename__ = 'get_server_local'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    request_time = Column(DateTime, default=datetime.datetime.utcnow)
    client_ip = Column(String)
    client_port = Column(Integer)
    server_ip = Column(String)
    server_port = Column(Integer)

# Определяем модель таблицы ProgramList
class ProgramList(Base):
    __tablename__ = 'program_list'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    request_time = Column(DateTime, default=datetime.datetime.utcnow)
    client_ip = Column(String)
    client_port = Column(Integer)
    program_version = Column(String)

# Создаем базу данных и таблицы
def create_database():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)

# Создаем сессию для взаимодействия с базой данных
def get_session():
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    return Session()


# Создаем базу данных
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

# Создаем сессию
Session = sessionmaker(bind=engine)
session = Session()

def add_record_global(client_ip, client_port, server_ip, server_port):
    """Добавляет запись в таблицу GetServerGlobal."""
    new_record = GetServerGlobal(client_ip=client_ip, client_port=client_port, 
                                  server_ip=server_ip, server_port=server_port)
    session.add(new_record)
    session.commit()

def add_record_local(client_ip, client_port, server_ip, server_port):
    """Добавляет запись в таблицу GetServerLocal."""
    new_record = GetServerLocal(client_ip=client_ip, client_port=client_port, 
                                 server_ip=server_ip, server_port=server_port)
    session.add(new_record)
    session.commit()

if __name__ == '__main__':
    create_database()
    print("База данных и таблицы созданы.")