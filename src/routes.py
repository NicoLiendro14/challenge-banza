from fastapi import APIRouter, status
from sqlalchemy.orm import Session
from .models import Account, sql_service, Client
from .schemas import ClientRequest

client_route = APIRouter()
activity_route = APIRouter()
amount_route = APIRouter()


@client_route.post("/register", status_code=status.HTTP_201_CREATED)
def register_client(client_req: ClientRequest):
    session = Session(bind=sql_service.engine, expire_on_commit=False)
    client = Client(name=client_req.name)
    session.add(client)
    session.commit()
    account = Account(balance_available=5000, clients_id=client.id)
    session.add(account)
    session.commit()
    session.close()
    return {"msg": "Client created",
            "client": client,
            "account": account
            }
