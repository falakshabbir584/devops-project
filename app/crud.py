from app.models import users
from app.db import database

async def get_user(user_id: int):
    query = users.select().where(users.c.id == user_id)
    return await database.fetch_one(query)

async def create_user(user_id: int, name: str):
    query = users.insert().values(id=user_id, name=name)
    await database.execute(query)
    return {"id": user_id, "name": name}

async def update_user(user_id: int, name: str):
    query = users.update().where(users.c.id == user_id).values(name=name)
    await database.execute(query)
    return {"id": user_id, "name": name}

async def delete_user(user_id: int):
    query = users.delete().where(users.c.id == user_id)
    await database.execute(query)
