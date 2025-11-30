import hashlib
import json

from saleapp.models import Category, Product, User
from saleapp import app


def load_categorys():
    # with open("data/category.json", encoding="utf-8") as f:
    #     return json.load(f)
    return Category.query.all()


def load_products(q=None, cate_id=None, page=None):
    # with open("data/product.json", encoding="utf-8") as f:
    #     products = json.load(f)
    #     if q:
    #         products = [p for p in products if p["name"].find(q)>=0]
    #
    #     if cate_id:#= if cate_id == None
    #         products = [p for p in products if p["cate_id"]==(int(cate_id))]
    #     return products

    query = Product.query

    if q:
        query = query.filter(Product.name.contains(q))

    if cate_id:
        query = query.filter(Product.cate_id.__eq__(cate_id))

    if page:
        size = app.config["PAGE_SIZE"]
        start = (int(page) - 1) * size;
        end = start + size;
        query = query.slice(start, end)

    return query.all()


def count_products():
    return Product.query.count()

def auth_user(username, password):
    password=hashlib.md5(password.encode("utf-8")).hexdigest()
    return User.query.filter(User.username == username, User.password==password).first()

def get_user_by_id(user_id):
    return User.query.get(user_id)

def get_product_by_id(id):
    # with open("data/product.json", encoding="utf-8") as f:
    #     products = json.load(f)
    #     for p in products:
    #         if p["id"]==id:
    #             return p
    #     return None
    return Product.query.get(id)


if __name__ == "__main__":
    with app.app_context():
        print(auth_user("user3", "123"))
