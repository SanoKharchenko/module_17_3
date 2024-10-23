from fastapi import FastAPI
from routers import task, user

app = FastAPI()


@app.get('/')
async def welcom():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task.router)
app.include_router(user.router)
