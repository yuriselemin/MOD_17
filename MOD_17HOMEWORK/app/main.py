from fastapi import FastAPI
from routers import user
from routers import tack

app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

app.include_router(user.router)
app.include_router(tack.router)