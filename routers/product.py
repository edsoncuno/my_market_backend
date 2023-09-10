from fastapi import APIRouter, Path, Query
from products import products
from models.product import Product

router = APIRouter()

@router.get("/productos")
def get_productos():
    return products


@router.get("/productos/{id}")
def get_producto(id: int = Path(gt=0)):
    return list(filter(lambda item: item["id"] == id, products))


# query parameters
# products/?stock=10&price=20
@router.get("/productos/")
def get_productos_by_stock(stock: int, price: float = Query(gt=0)):
    # return list(filter(lambda item: item["stock"] == stock, productos))
    return list(
        filter(lambda item: item["stock"] == stock and item["price"] == price, products)
    )


@router.post("/products")
def create_product(product: Product):
    products.append(product)
    return products


@router.put("/products/{id}")
def update_product(id: int, product: Product):
    for index, item in enumerate(products):
        if item["id"] == id:
            products[index]["name"] = product.name
            products[index]["stock"] = product.stock
            products[index]["price"] = product.price
    return products


@router.delete("/products/{id}")
def update_product(id: int):
    for item in products:
        if item["id"] == id:
            products.remove(item)
    return products
