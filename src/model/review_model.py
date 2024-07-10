from pydantic import BaseModel
from typing import List


class ReviewResponse(BaseModel):
    id_curriculum:int
    occupation_area: str
    top_probabilities: List = []
    seniority: str
