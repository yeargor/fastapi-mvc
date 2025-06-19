from pydantic import BaseModel

class SBookAdd(BaseModel):
    title: str
    description: str | None = None