import time
import uuid
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.logging import get_logger

logger = get_logger("middleware")

class LoggingMiddleware(BaseHTTPMiddleware):
    """Middleware to log HTTP requests and responses."""
    
    async def dispatch(self, request: Request, call_next):
        # Generate unique request ID
        request_id = str(uuid.uuid4())
        
        # Start timing
        start_time = time.time()
        
        # Process request
        response: Response = await call_next(request)
        
        # Calculate processing time
        process_time = time.time() - start_time
        
        # Only log errors or slow requests
        if response.status_code >= 400 or process_time > 1.0:
            logger.info(
                f"[{request_id}] {request.method} {request.url.path} - "
                f"Status: {response.status_code} - Time: {process_time:.4f}s"
            )
        
        # Add request ID to response headers
        response.headers["X-Request-ID"] = request_id
        
        return response