from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from .services import SQLService

sql_service = SQLService()
sql_service.config_credentials()
Base = sql_service.base
sql_service.create_db()


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String)
