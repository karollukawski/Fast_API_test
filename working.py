from fastapi import FastAPI

app = FastAPI()

inventory = {
    1: {
        "name": "Honey",
        "price": "8.99",
        "brand": "ABC"
    }
}

@app.get("/get-item/{item_id}")
def get_item(item_id: int):
    return inventory [item_id]