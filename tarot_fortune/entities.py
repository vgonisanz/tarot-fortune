from pydantic import BaseModel, Field
from typing import List

class TarotCard(BaseModel):
    id: str
    type: str
    title: str
    description: str
    orientation: str = Field(default="up", regex=r"^(up|down)$")
    meaning_up: List[str] = Field(..., min_items=1)
    meaning_down: List[str] = Field(..., min_items=1)
