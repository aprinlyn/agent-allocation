import fastapi
import uvicorn

@app.exception_handler(Exception)
def validation_exception_handler(request, err):
    base_error_message = f"Failed to execute: {request.method}: {request.url}"
    return JSONResponse(status_code=400, content={"message": f"{base_error_message}. Detail: {err}"})

if __name__ == "__main__":
    uvicorn.run("main:app", port=9000, reload=True)