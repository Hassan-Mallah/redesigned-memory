from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Simple FastAPI App")

class Item(BaseModel):
    id: int
    name: str

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id, "name": f"Item {item_id}"}

@app.post("/items/")
async def create_item(item: Item):
    return {"created": item}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
