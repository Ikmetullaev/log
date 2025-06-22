from pydantic import BaseModel

class Log(BaseModel):
    ip: str
    port: str
    method: str
    path: str
    country: str
    region: str
    city: str
    timestamp: str
