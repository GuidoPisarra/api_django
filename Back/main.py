from typing import Union

from fastapi import FastAPI
from Routers import products
from Routers import users

app = FastAPI()
# PARA INICIAR EL SERVIDOR python -m uvicorn main:app --reload
# DOCUMENTACION http://127.0.0.1:8000/redoc o http://127.0.0.1:8000/docs#/ (esta ultima es swagger)


def root():
    return "Holaaaaaaaaaaa"


app.include_router(products.router)
app.include_router(users.router)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
