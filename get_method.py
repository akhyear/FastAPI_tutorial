from fastapi import FastAPI

app = FastAPI()
@app.get("/items")
def read_items():
    return {"message": "This is a GET request to /items endpoint"}