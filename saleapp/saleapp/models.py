import json

from saleapp import db, app
from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship

class Base(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(150), nullable=False, unique=True)

class Category(Base):
    products = relationship('Product', backref="category", lazy=True)

    def __str__(self):
        return self.name

class Product(Base):
    image = Column(String(1000), nullable=False, default="data:image/webp;base64,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")
    price = Column(Float, default=0.0)
    cate_id=Column(Integer, ForeignKey(Category.id), nullable=False)

    def __str__(self):
        return self.name

if __name__=="__main__":
    with app.app_context():
        #db.create_all()
        c1=Category(name="Laptop")
        c2 = Category(name="Mobile")
        c3 = Category(name="Tablet")

        # db.session.add_all([c1,c2,c3])

        # with open("data/product.json", encoding="utf-8") as f:
        #     products = json.load(f)
        #
        #     for p in products:
        #         db.session.add(Product(**p))
        #
        # db.session.commit()
        print(c2.products)

