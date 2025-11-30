import math

from flask import render_template, request, redirect
import dao
from saleapp import app, login, admin
from saleapp.dao import auth_user
from flask_login import login_user, current_user, logout_user


@app.route("/")
def index():
    q = request.args.get("q")
    cate_id = request.args.get("cate_id")
    page = request.args.get("page")
    products = dao.load_products(q=q, cate_id=cate_id, page=page)
    pages = math.ceil(dao.count_products() / app.config["PAGE_SIZE"])

    return render_template("index.html", products=products, pages=pages)


@app.route("/products/<int:id>")
def details(id):
    p = dao.get_product_by_id(id)
    return render_template("product-details.html", prods=p)


@app.route("/login", methods=["get", "post"])
def login_account():
    if current_user.is_authenticated:
        return redirect("/")

    err_msg = None

    if (request.method == "POST"):
        username = request.form.get("username")
        password = request.form.get("password")

        user = auth_user(username, password)

        if user:
            login_user(user)
            return redirect("/")
        else:
            err_msg = "Tai khoan hoac mat khau khong dung"

    return render_template("login.html", err_msg=err_msg)


@app.route("/admin-login", methods=["post"])
def admin_login():
    err_msg = None
    username = request.form.get("username")
    password = request.form.get("password")

    user = auth_user(username, password)

    if user:
        login_user(user)
        return redirect("/admin")
    else:
        err_msg = "Tai khoan hoac mat khau khong dung"


@app.route("/logout")
def logout_account():
    logout_user()
    return redirect("/")


@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)


@app.context_processor
def common_attribute():
    return {
        "cates": dao.load_categorys()
    }


if __name__ == "__main__":
    with app.app_context():
        app.run(debug=True)
