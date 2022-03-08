"""
Link para a pagina base: https://fastapi.tiangolo.com/tutorial/path-params-numeric-validations/
outros links: https://fastapi.tiangolo.com/tutorial/query-params-str-validations/

gt: greater than
ge: greater than or equal
lt: less than
le: less than or equal
"""

from fastapi import FastAPI, Path, Query

app = FastAPI()

@app.get('/items/{item_id}')
async def read_items(
        item_id: int = Path(..., title='The ID of the item to get'),
        q: str | None = Query(None, alias='item-query'),
):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    return results

@app.get('/items2/{item_id}')
async def read_items2(
        q: str | None = Query(None, alias='item-query'),
        item_id: int = Path(..., title='The ID of the item to get'),
):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    return results

@app.get('/items3/{item_id}')
async def read_items3(
        *, item_id: int = Path(..., title='The ID of the item to get'), q: str
):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    return results

@app.get('/items4/{item_id}')
async def read_items4(
        *, item_id: int = Path(..., title='The ID of the item to get', ge=1), q: str
):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    return results

@app.get('/items5/{item_id}')
async def read_items5(
        *, item_id: int = Path(..., title='The ID of the item to get', gt=0, le=1000), q: str
):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    return results

@app.get('/items5/{item_id}')
async def read_items6(
        *, item_id: int = Path(..., title='The ID of the item to get', gt=0, le=1000),
        q: str,
        size: float = Query(..., gt=0, lt=10.5)
):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    if size:
        results.update({'size': size})
    return results


