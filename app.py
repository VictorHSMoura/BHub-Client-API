from fastapi import FastAPI, Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from apis.clients import router as clients_router
from apis.bank_details import router as bank_details_router
from db.sqlalchemy_db import Base, engine

Base.metadata.create_all(bind=engine)

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


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )

# Adds routes to endpoints.
app.include_router(clients_router)
app.include_router(bank_details_router)
