from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.search import router as search_router
from app.services.es_index_service import create_index

app = FastAPI(title="Travel Search API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    create_index()

app.include_router(search_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Travel Search API running"}

@app.get("/health")
def health():
    return {"status": "ok"}
