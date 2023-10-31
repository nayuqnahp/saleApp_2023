from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from app import db


class Category(db.Model):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    products = relationship('Product', backref = 'category', lazy = True)

class Product(db.Model):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, default=0)
    image = Column(Float(100))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

if __name__ == "__main__":
    from app import app
    with app.app_context():
        c1 = Category("Mobile")
        c2 = Category("Tablet")
        db.session.add_all[c1, c2]
        db.session.commit()
        #db.create_all()

