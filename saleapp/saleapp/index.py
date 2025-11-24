import math

from flask import render_template, request, redirect
import dao
from saleapp import app


@app.route("/")
def index():
    q = request.args.get("q")
    cate_id=request.args.get("cate_id")
    page = request.args.get("page")
    products = dao.load_products(q=q, cate_id=cate_id, page=page)
    pages = math.ceil(dao.count_products()/app.config["PAGE_SIZE"])

    return render_template("index.html", products = products, pages = pages)


@app.route("/products/<int:id>")
def details(id):
    p = dao.get_product_by_id(id)
    return render_template("product-details.html", prods = p)

@app.route("/login", methods=["get", "post"])
def login():

    if(request.method=="POST"):
        username = request.form.get("username")
        password = request.form.get("password")
        if (username == "namdz" and password == "123"):
            return redirect("/")



    return render_template("login.html")

@app.context_processor
def common_attribute():
    return {
        "cates":dao.load_categorys()
    }

if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)
