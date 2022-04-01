import requests
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
from .services import SQLService

sql_service = SQLService()
sql_service.config_credentials()
Base = sql_service.base
sql_service.create_db()


class Client(Base):
    __tablename__ = 'clients'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String)


class Account(Base):
    __tablename__ = 'account'
    id = Column(Integer, primary_key=True)
    clients_id = Column(Integer, ForeignKey('clients.id'))
    client = relationship("Client")
    balance_available = Column(Float)

    def get_total_usd(self):
        url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
        res = requests.get(url)
        dolar_bolsa = float(res.json()[4]['casa']['venta'].replace(",", "."))
        return self.balance_available * dolar_bolsa
