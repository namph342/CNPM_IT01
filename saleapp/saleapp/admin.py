from flask_admin import Admin, AdminIndexView, expose, BaseView
from flask_admin.theme import Bootstrap4Theme
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user, logout_user
from werkzeug.utils import redirect

from saleapp import app, db
from saleapp.models import Category, Product, User


class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self) -> str:
        return self.render('admin/index.html')


admin = Admin(app=app, name="E-Commerce", theme=Bootstrap4Theme(), index_view=MyAdminIndexView())


class MyCategoryView(ModelView):
    column_list = ['id', 'name', 'created_date', 'products']
    column_searchable_list = ['name']
    column_filters = ['name']
    column_labels = {
        'name': 'Ten Loai',
        'created_date': 'Ngay tao',
        'products': 'Ten San Pham'
    }

    def is_accessible(self) -> bool:
        return current_user.is_authenticated

class MyProductView(ModelView):
    column_list = ['id', 'name', 'category', 'created_date']
    column_searchable_list = ['name']
    column_filters = ['name']
    def is_accessible(self) -> bool:
        return current_user.is_authenticated

class MyAdminLogoutView(BaseView):
    @expose('/')
    def index(self) -> str:
        logout_user()
        return redirect("/admin")


admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductView(Product, db.session))
admin.add_view(MyAdminLogoutView("Dang xuat"))

