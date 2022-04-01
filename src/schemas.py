from pydantic import BaseModel


class ClientRequest(BaseModel):
    name: str

    class Config:
        orm_mode = True


class ActivitySchema(BaseModel):
    clients_id: int
    type_of: str
    amount: float

    class Config:
        orm_mode = True
