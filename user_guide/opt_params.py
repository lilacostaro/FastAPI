from fastapi import FastAPI

app = FastAPI()

# Query with no required parameters.
@app.get('/items/{item_id}')
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {'item_id': item_id}
    if q:
        item.update(
            {'q': q}
        )
    if not short:
        item.update(
            {'description': 'This is an amazing item tha has a long description'}
        )
    return item

# Multiple path and query parameters
@app.get('/users/{user_id}/items/{item_id}')
async def read_user_item(user_id: int, item_id: str, q: str | None = None, short: bool = False):
    item = {'item_id': item_id, 'owner_id': user_id}
    if q:
        item.update(
            {'q': q}
        )
    if not short:
        item.update(
            {'description': 'This is an amazing item tha has a long description'}
        )
    return item

# With required paramenters.
@app.get('/required/{item_id}')
async def item_required(item_id: str, needy: str):
    item = {'item_id': item_id, 'needy': needy}
    return item

# with required, non-required and optional parameters
@app.get('/optional/{item_id}')
async def optional_required(item_id: str, needy: str, skip: int = 0, limit: int | None = None):
    item = {'item_id': item_id, 'needy': needy, 'skip': skip, 'limit': limit}
    return item