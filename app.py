# app.py
from fastapi import FastAPI

app = FastAPI()


@app.post("/client/register")
def register_client():
    return {"msg": "Client registered"}


@app.put("/client/{id}")
def update_client():
    return {"msg": "Client updated"}


@app.delete("/client/{id}")
def delete_client():
    return {"msg": "Client deleted"}


@app.get("/client/{id}")
def detail_client():
    return {"msg": "Client detail"}


@app.get("/client/all")
def get_all_client():
    return {"msg": "All clients"}
