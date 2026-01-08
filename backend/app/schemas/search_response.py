from pydantic import BaseModel
from typing import List, Optional

class Location(BaseModel):
    name: str
    city: str
    description: str
    type: str
    score: Optional[int] = None

class SearchData(BaseModel):
    query: str
    total_results: int
    limit: int
    offset: int
    results: List[Location]

class SearchResponse(BaseModel):
    status: str
    data: SearchData
