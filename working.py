from fastapi import FastAPI

app = FastAPI()

inventory = {
    1: {
        "name": "Honey",
        "price": "8.99",
        "brand": "ABC"
    }
}

@app.get("/get-item/{item_id}/{name}")
def get_item(item_id: int, name: str = None):
    return inventory [item_id]