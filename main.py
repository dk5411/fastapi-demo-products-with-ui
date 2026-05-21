from fastapi import FastAPI
from models import Product

app = FastAPI()

@app.get("/")
def greet():
    return {"message": "Welcome to FastAPI server application"}

products = [
    Product(id=1, name="phone", description="budget phone", price=99.99, quantity=10),
    Product(id=2, name="laptop", description="gaming laptop", price=999.99, quantity=5),
    Product(id=3, name="headphones", description="wireless headphones", price=199.99, quantity=15),
    Product(id=4, name="smartwatch", description="fitness smartwatch", price=149.99, quantity=20),
    Product(id=5, name="tablet", description="10-inch tablet", price=299.99, quantity=8)

]

@app.get("/products")
def get_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return {"message": "Product not found"}

@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return {"message": "Product added successfully", "product": product}

@app.put("/product")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product Updated Successfully"
    return "No product found with the given ID"

@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product Deleted Successfully"
    return "No product found with the given ID"