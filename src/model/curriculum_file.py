from pydantic import BaseModel

class CurriculumFile(BaseModel):
    id: int
    file: bytes
    