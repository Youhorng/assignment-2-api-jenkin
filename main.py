from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from FastAPI!"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/users")
def get_users():
    return {"users": ["Alice", "Bob", "Charlie"]}