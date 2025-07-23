from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import api_router
from app.core.config import settings
from app.core.database import engine, Base
from app.core.logging import setup_logging, get_logger
from app.core.middleware import LoggingMiddleware
import app.models  # Import all models to register them with SQLAlchemy

# Initialize logging
logger = setup_logging(
    log_level=settings.LOG_LEVEL,
    log_file=settings.LOG_FILE
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Create database tables
    logger.info("AA84 API startup - Creating database tables")
    Base.metadata.create_all(bind=engine)
    yield
    # Shutdown: Clean up resources if needed
    logger.info("AA84 API shutdown")

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="AA84 API",
    version="1.0.0",
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    lifespan=lifespan
)

app.add_middleware(LoggingMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=settings.API_V1_STR)

@app.get("/")
async def root():
    return {"message": "Welcome to AA84 API"}