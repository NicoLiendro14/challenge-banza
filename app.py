from src.routes import client_route, activity_route, amount_route
from fastapi import FastAPI

app = FastAPI()

app.include_router(client_route, prefix="/client")
app.include_router(activity_route, prefix="/activity")
app.include_router(amount_route, prefix="/amount")
