from fastapi import FastAPI
from routers.product import router as product_router

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


app.include_router(product_router)
