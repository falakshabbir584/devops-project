from fastapi import FastAPI, HTTPException
from app.db import database
import app.crud as crud

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
def root():
    return {"message": "Hello from FastAPI!"}

@app.post("/users/{user_id}")
async def create_user(user_id: int, name: str):
    existing = await crud.get_user(user_id)
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")
    return await crud.create_user(user_id, name)

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    user = await crud.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}")
async def update_user(user_id: int, name: str):
    user = await crud.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return await crud.update_user(user_id, name)

@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    user = await crud.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    await crud.delete_user(user_id)
    return {"message": "User deleted"}
