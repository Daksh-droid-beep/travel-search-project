from fastapi import APIRouter, Query
from app.services.search_service import search_locations_service

router = APIRouter()

@router.get("/search")
def search(
    q: str = Query(..., min_length=1),
    search_type: str = Query("all"),
    limit: int = Query(6, ge=1, le=50),
    offset: int = Query(0, ge=0),
):
    """
    Search API endpoint
    """
    result = search_locations_service(
        q=q,
        search_type=search_type,
        limit=limit,
        offset=offset
    )

    return result
