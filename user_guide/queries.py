from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{'item_name': 'Foo'},
                 {'item_name': 'Bar'},
                 {'item_name': 'Baz'},
                 {'item_name': 'Buz'},
                 {'item_name': 'Biz'},
                 {'item_name': 'Boz'},
                 {'item_name': 'Bez'},
                 {'item_name': 'Bor'},
                 {'item_name': 'Bur'},
                 {'item_name': 'Bir'},
                 {'item_name': 'Ber'},
                 {'item_name': 'Bour'}]

@app.get('/items')
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]