from pydantic import BaseModel


class Curriculum(BaseModel):
    id: int
    file_name: str
    