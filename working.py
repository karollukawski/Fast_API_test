from typing import Annotated

from fastapi import FastAPI, Path 

app = FastAPI()

inventory = {
    1: {
        "name": "Honey",
        "price": "8.99",
        "brand": "ABC"
    }
}

@app.get("/get-item/{item_id}")
def get_item(item_id: Annotated[int, Path(description = "The ID of the item to retrive", gt = 0, le = 5)]):
    return inventory [item_id]