import datetime
from fastapi import APIRouter, status, HTTPException, Response
from sqlalchemy.orm import Session
from .models import Account, Activity, ActivityDetail, sql_service, Client
from .schemas import ClientRequest, ActivitySchema


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


@ client_route.put("/{id}")
def update_client(id: int, name: str):
    session = Session(bind=sql_service.engine, expire_on_commit=False)

    client = session.query(Client).get(id)

    if client:
        client.name = name
        session.commit()

    session.close()

    if not client:
        raise HTTPException(
            status_code=404, detail=f"Client item with ID {id} doesn't exist.")

    return client


@ client_route.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_client(id: int):

    # create a new database session
    session = Session(bind=sql_service.engine, expire_on_commit=False)

    # get the todo item with the given id
    client = session.query(Client).get(id)

    # if todo item with given id exists, delete it from the database. Otherwise raise 404 error
    if client:
        session.delete(client)
        session.commit()
        session.close()
    else:
        raise HTTPException(
            status_code=404, detail=f"Client with ID {id} doesn't exist")

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@activity_route.post("/register", status_code=status.HTTP_201_CREATED)
def register_activity(activity_req: ActivitySchema):
    session = Session(bind=sql_service.engine, expire_on_commit=False)
    account = session.query(Account).get(activity_req.clients_id)
    activity = Activity(clients_id=activity_req.clients_id,
                        date=datetime.datetime.utcnow())
    session.add(activity)
    session.commit()
    activity_detail = ActivityDetail(
        activities_id=activity.id,
        type_of=activity_req.type_of,
        amount=activity_req.amount
    )
    if activity_req.type_of == "ingreso":
        account.balance_available = account.balance_available + activity_req.amount

    if activity_req.type_of == "egreso":
        account.balance_available = account.balance_available - activity_req.amount
    session.add(account)
    session.add(activity_detail)
    session.commit()
    session.close()
    return {
        "msg": "Activity registered.",
        "activity_detail": activity_detail,
        "activity": activity,
        "account": account
    }


@activity_route.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_activity(id: int):
    # create a new database session
    session = Session(bind=sql_service.engine, expire_on_commit=False)

    # get the todo item with the given id
    activity = session.query(Activity).get(id)
    activity_detail = session.query(ActivityDetail).get(activity.id)
    account = session.query(Account).get(activity.clients_id)

    if activity_detail.type_of == "ingreso":
        account.balance_available = account.balance_available - activity_detail.amount

    if activity_detail.type_of == "egreso":
        account.balance_available = account.balance_available + activity_detail.amount

    if activity:
        session.delete(activity)
        session.delete(activity_detail)
        session.commit()
        session.close()

    else:
        raise HTTPException(
            status_code=404, detail=f"Client with ID {id} doesn't exist")

    return Response(status_code=status.HTTP_204_NO_CONTENT)


@activity_route.get("/{id}")
def get_activity(id: int):
    session = Session(bind=sql_service.engine, expire_on_commit=False)
    activity = session.query(Activity).get(id)
    activity_detail = session.query(ActivityDetail).get(activity.id)
    session.close()
    if not activity:
        raise HTTPException(
            status_code=404, detail=f"Client with ID {id} doesn't exist.")
    return activity_detail


@amount_route.get("/{id}")
def get_amount(id: int):
    session = Session(bind=sql_service.engine, expire_on_commit=False)
    account = session.query(Account).get(id)
    session.close()
    if not account:
        raise HTTPException(
            status_code=404, detail=f"Client with ID {id} doesn't exist.")
    return {'balance_available': account.balance_available}
