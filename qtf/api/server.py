from fastapi import FastAPI
from qtf.config import settings

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        debug=settings.DEBUG
    )
    
    @app.get("/")
    async def root():
        return {"message": "Welcome to QTF Quant Server", "status": "running"}
        
    return app
