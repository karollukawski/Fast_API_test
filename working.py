from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

inventory = {
    1: {
        "name": "Honey",
        "price": "8.99",
        "brand": "ABC"
    }
}

@app.get("/get-item/{item_id}")
def get_item(item_id: int = Path(description = "The ID of the item to retrive", gt = 0, le = 5)):
    return inventory [item_id]

# URL: http://127.0.0.1:8000/get-by-name/1?test=2&name=Honey <- order doesn't matter
@app.get("/get-by-name/{item_id}")
def get_item(*, item_id: int, name: Optional[str] = None, test: int):
    for id in inventory:
        if inventory[item_id]["name"] == name:
            return inventory[item_id]
    return {"Data":"Not found"}

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {"Error": "Item ID already exists."}
    
    inventory[item_id] = {"name": item.name, "brand": item.brand, "price": item.price}
    return inventory[item_id]