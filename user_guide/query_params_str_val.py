from fastapi import FastAPI, Query

app = FastAPI()

@app.get('/items/')
async def read_items(q: str | None = Query(None, min_length=3, max_length=50, regex="^fixedquery$")):
    results = {'items': [{'item_id': 'foo'}, {'item_id': 'Bar'}]}
    if q:
        results.update({'q': q})
    return results

@app.get('/items2/')
async def read_items2(q: str | None = Query("fixedquery", min_length=3)):
    results = {'items': [{'item_id': 'foo'}, {'item_id': 'Bar'}]}
    if q:
        results.update({'q': q})
    return results

@app.get('/items3/')
async def read_items3(q: str | None = Query(..., min_length=3)):
    results = {'items': [{'item_id': 'foo'}, {'item_id': 'Bar'}]}
    if q:
        results.update({'q': q})
    return results

@app.get("/items4/")
async def read_items4(q: list[str] | None = Query(None)):
    query_items = {'q': q}
    return query_items

@app.get("/items5/")
async def read_items5(q: list[str] = Query(['foo', 'bar'])):
    query_items = {'q': q}
    return query_items

@app.get("/items6/")
async def read_items6(q: list = Query([])):
    query_items = {'q': q}
    return query_items

@app.get("/items7/")
async def read_items7(q: str | None = Query(None, title="Query string", min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items8/")
async def read_items8(
        q: str
        | None = Query(
            None, title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
        )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items9/")
async def read_items9(q: str | None = Query(None, alias='item-query')):
    results = {'items': [{'item_id': 'Foo'}, {'item_id': 'Bar'}]}
    if q:
        results.update({'q': q})
    return results

@app.get("/items10/")
async def read_items10(
        q: str
        | None = Query(
            None,
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that hava a good match",
            min_length=3,
            max_length=50,
            regex="^fixedquery$",
            deprecated=True,
        )
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

@app.get("/items11/")
async def read_items11(hidden_query: str | None = Query(None, include_in_schema=False)):
    if hidden_query:
        return {"hidden_query": hidden_query}
    else:
        return {"hidden_query": "Not found"}