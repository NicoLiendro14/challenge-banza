from pydantic import BaseModel


class ClientRequest(BaseModel):
    name: str

    class Config:
        orm_mode = True
