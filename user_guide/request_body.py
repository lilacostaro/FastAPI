from fastapi import FastAPI
from pydantic import BaseModel

# Create your data model
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None

# create the app
app = FastAPI()

# Declare the method and the path of the function
@app.post('/items')
# Declare the model as a parameter of the function
async def create_item(item: Item):
    # Using the model
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({'price_with_tax': price_with_tax})
    return item_dict

# Request body + path parameters
# @app.put('/items/{item_id}')
# async def create_item_put(item_id: int, item: Item):
#     return {'item_id': item_id, **item.dict()}

# Request body + path + query parameters¶
@app.put('/items/{item_id}')
async def create_item_put(item_id: int, item: Item, q: str | None = None):
    result = {'item_id': item_id, **item.dict()}
    if q:
        result.update({'q': q})
    return result