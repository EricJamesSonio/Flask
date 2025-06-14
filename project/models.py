from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ProductItem(db.Model):
    __tablename__ = "product_items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50))
    price = db.Column(db.Float, nullable=False)

    __mapper_args__ = {
        "polymorphic_identity": "product_item",
        "polymorphic_on": type,
    }

    def __repr__(self):
        return f"<ProductItem: {self.name}>"


class Burger(ProductItem):
    __tablename__ = "burgers"
    id = db.Column(db.Integer, db.ForeignKey("product_items.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "burger",
    }

    def __repr__(self):
        return f"<Burger: {self.name}>"


class CheeseBurger(Burger):
    __tablename__ = "cheeseburgers"
    id = db.Column(db.Integer, db.ForeignKey("burgers.id"), primary_key=True)

    __mapper_args__ = {
        "polymorphic_identity": "cheeseburger",
    }

    def __repr__(self):
        return f"Cheese Burger : {self.name}"
