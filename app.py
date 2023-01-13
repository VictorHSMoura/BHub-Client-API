from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from apis.clients import router as clients_router

# Creates API app.
app = FastAPI(
    title="BHub Client API",
    description="API created for the BHub admission process.",
    version="0.1.0"
)

# Adds CORS middleware to the application.
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Adds routes to endpoints.
app.include_router(clients_router)