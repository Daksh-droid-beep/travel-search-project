from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.search import router as search_router

app = FastAPI(title="Travel Search API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # IMPORTANT
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(search_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Travel Search API running"}

@app.get("/health")
def health():
    return {"status": "ok"}
