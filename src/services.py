from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Float, DateTime
import logging


class SQLService:
    def __init__(self):
        """ Initialize the class """
        self.conn_string = ''
        self.engine = None
        self.base = declarative_base()

    def create_db(self):
        self.base.metadata.create_all(self.engine)

    def execute_sql_script(self, script):
        """ Execute the sql script """
        self.engine.execute(script)

    def config_credentials(self):
        """ Configure the credentials to connect to the database from a .env file"""
        USER = config('USER', default='postgres')
        PASSWORD = config('PASSWORD')
        HOSTNAME = config('HOSTNAME', default='localhost')
        PORT = config('PORT', default=5432)
        DB_NAME = config('DB_NAME')
        db_string = "postgresql://{USER}:{PASSWORD}@{HOSTNAME}:{PORT}/{DB_NAME}".format(
            USER=USER, PASSWORD=PASSWORD, HOSTNAME=HOSTNAME, PORT=PORT, DB_NAME=DB_NAME)
        try:
            self.conn_string = db_string
            self.engine = create_engine(self.conn_string)
        except Exception as e:
            logging.error(e)
            raise e

    def crear_base_de_datos(self):
        meta = MetaData()
        clients = Table(
            'clients', meta,
            Column('id', Integer, primary_key=True),
            Column('name', String),
        )
        account = Table(
            'account', meta,
            Column('id', Integer, primary_key=True),
            Column('clients_id', Integer, ForeignKey('clients.id')),
            Column('balance_available', Float),
        )
        activities = Table(
            'activities', meta,
            Column('id', Integer, primary_key=True),
            Column('date', DateTime),
            Column('clients_id', Integer, ForeignKey('clients.id')),
        )
        activities_detail = Table(
            'activities_detail', meta,
            Column('id', Integer, primary_key=True),
            Column('activities_id', Integer, ForeignKey('activities.id')),
            Column('type_of', String),
            Column('amount', Float)
        )
        meta.create_all(self.engine)


sql_service = SQLService()
sql_service.config_credentials()
Base = sql_service.base
sql_service.crear_base_de_datos()
