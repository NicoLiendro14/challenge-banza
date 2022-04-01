import unittest
from ..src.models import Base, Client
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from ..src.routes import client_route
from ..src.services import SQLService
from fastapi.testclient import TestClient
from unittest.mock import MagicMock

client_test = TestClient(client_route)


class TestClientRouter(unittest.TestCase):
    def setUp(self):
        self.sql_service = SQLService()
        self.sql_service.config_credentials()
        self.sql_service.crear_base_de_datos()
        self.client = Client(id=1, name='Nicolas')
        self.session = Session(bind=self.sql_service.engine)
        self.session.add(self.client)
        self.session.commit()
        self.all_clients = self.session.query(Client).all()

    def tearDown(self):
        self.sql_service.base.metadata.drop_all(self.sql_service.engine)

    def test_detail_client(self):
        expected = self.client
        result = client_test.get("/1")
        self.assertEqual(result.json()['name'], expected.name)
        self.assertEqual(result.json()['id'], expected.id)

    def test_get_all_client(self):
        expected = self.all_clients
        result = client_test.get("/all/")
        self.assertEqual(len(result.json()), len(expected))

    def test_update_client(self):
        expected_name = "Juan"
        mock_prueba = client_route
        mock_prueba.put = MagicMock(return_value={"id": 1, "name": "Juan"})
        result = mock_prueba.put("/1", data={"id": 1, "name": "Juan"})
        self.assertEqual(result['name'], expected_name)

    def test_detail_client(self):
        expected = self.client
        result = client_test.get("/1")
        self.assertEqual(result.json()['name'], expected.name)
        self.assertEqual(result.json()['id'], expected.id)
