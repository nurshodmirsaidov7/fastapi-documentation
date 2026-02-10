from fastapi import FastAPI
from auth_routes import auth_router
from orders_routes import order_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(order_router)




@app.get('/')
async def main():
    return {'Nurshod': 'Mirsaidov'}

@app.get('/full_name')
async def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return {'full name': full_name}

@app.get('/items')
async def process_items(items: list[str]):
    for item in items:
        return [{'message': item.capitalize() for item in items}]
    
