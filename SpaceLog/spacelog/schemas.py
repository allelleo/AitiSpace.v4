from pydantic import BaseModel


class LogInput(BaseModel):
    project: str
    service: str = None
    level: str
    message: str
    code: int = 0
