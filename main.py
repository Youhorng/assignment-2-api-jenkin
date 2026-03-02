from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    email: str

# GET
@app.get("/")
def root():
    return {"message": "Hello from FastAPI!"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/users")
def get_users():
    return {"users": ["Alice", "Bob", "Charlie"]}

# POST
@app.post("/users")
def create_user(user: User):
    return {"message": "User created", "user": user}

# PUT
@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    return {"message": f"User {user_id} updated", "user": user}

# DELETE
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {"message": f"User {user_id} deleted"}