import logging
from fastapi import HTTPException
from fastapi.responses import JSONResponse

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Custom exception handler
async def http_exception_handler(request, exc):
    logger.error(f"HTTP error occurred: {exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

# Example usage in a route
@app.get("/example")
async def example_route():
    try:
        # Your code here
        result = some_function()
        logger.info(f"Successfully processed request: {result}")
        return {"result": result}
    except SomeSpecificError as e:
        logger.error(f"Specific error occurred: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.exception("Unexpected error occurred")
        raise HTTPException(status_code=500, detail="Internal server error")

# Add this to your main.py
app.add_exception_handler(HTTPException, http_exception_handler)
