from fastapi import APIRouter, status, HTTPException
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


@ client_route.get("/{id}", response_model=ClientRequest)
def detail_client(id: int):
    session = Session(bind=sql_service.engine, expire_on_commit=False)
    client = session.query(Client).get(id)
    session.close()
    if not client:
        raise HTTPException(
            status_code=404, detail=f"Client with ID {id} doesn't exist.")
    return client


@ client_route.get("/all/")
def get_all_client():
    session = Session(bind=sql_service.engine, expire_on_commit=False)
    all_clients = session.query(Client).all()
    session.close()
    return all_clients
