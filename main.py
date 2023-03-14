from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles
from app.routers import marcas


app = FastAPI()


app.include_router(marcas.router)


app.mount("/static", StaticFiles(directory="app/static"), name="static")


if __name__ == "__main__":    
    uvicorn.run("main:app", port = 8000, reload = True)