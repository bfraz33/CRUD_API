from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    model: str
    price: int

items = {}

#Post ->  Create
@app.post("/items/{item_id}")
def create_item(item_id: int, item: Item):
    items[item_id] = item
    return {"message": "Item created", "item": item}


#Get ->  Retrieve
@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id in items:
        return items[item_id]
    return {"error": "Item not found"}

#Put ->  Update
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    if item_id in items:
       items[item_id] = item
       return{"message": "Item updated", "item": item}
    return{"error": "Item not found"}

#Delete ->  Delete
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in items:
        deleted = items.pop(item_id)
        return {"message": "item deleted", "deleted_item": deleted}
    return {"error": "Item not found"}