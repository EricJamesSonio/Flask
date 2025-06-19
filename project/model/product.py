from datetime import datetime
from sqlalchemy.sql import func
from extension import db
from model.supplier import Supplier


class ProductItem(db.Model):
    __tablename__ = "product_items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50))
    description = db.Column(db.Text, nullable=True)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, default=0)
    type = db.Column(db.String(50))  # polymorphic discriminator
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

    __mapper_args__ = {
        "polymorphic_identity": "productitem",
        "polymorphic_on": type,
    }

    def __repr__(self):
        return (
            f"<ProductItem: {self.name}, Category: {self.category}, Type: {self.type}>"
        )


# ----------------------
# BURGERS
# ----------------------


class Burger(ProductItem):
    __tablename__ = "burgers"
    id = db.Column(db.Integer, db.ForeignKey("product_items.id"), primary_key=True)

    __mapper_args__ = {"polymorphic_identity": "burger"}

    def __repr__(self):
        return f"<Burger: {self.name}>"


class CheeseBurger(Burger):
    __tablename__ = "cheeseburgers"
    id = db.Column(db.Integer, db.ForeignKey("burgers.id"), primary_key=True)

    __mapper_args__ = {"polymorphic_identity": "cheeseburger"}

    def __repr__(self):
        return f"<CheeseBurger: {self.name}>"


class SpicyBurger(Burger):
    __tablename__ = "spicyburgers"
    id = db.Column(db.Integer, db.ForeignKey("burgers.id"), primary_key=True)

    __mapper_args__ = {"polymorphic_identity": "spicyburger"}

    def __repr__(self):
        return f"<SpicyBurger: {self.name}>"


class OverloadBurger(Burger):
    __tablename__ = "overloadburgers"
    id = db.Column(db.Integer, db.ForeignKey("burgers.id"), primary_key=True)

    __mapper_args__ = {"polymorphic_identity": "overloadburger"}

    def __repr__(self):
        return f"<OverloadBurger: {self.name}>"


# ----------------------
# PIZZA
# ----------------------


class Pizza(ProductItem):
    __tablename__ = "pizzas"
    id = db.Column(db.Integer, db.ForeignKey("product_items.id"), primary_key=True)

    __mapper_args__ = {"polymorphic_identity": "pizza"}

    def __repr__(self):
        return f"<Pizza: {self.name}>"


class HawaiianPizza(Pizza):
    __tablename__ = "hawaiian_pizzas"
    id = db.Column(db.Integer, db.ForeignKey("pizzas.id"), primary_key=True)

    __mapper_args__ = {"polymorphic_identity": "hawaiianpizza"}

    def __repr__(self):
        return f"<HawaiianPizza: {self.name}>"


class PepperoniPizza(Pizza):
    __tablename__ = "pepperoni_pizzas"
    id = db.Column(db.Integer, db.ForeignKey("pizzas.id"), primary_key=True)

    __mapper_args__ = {"polymorphic_identity": "pepperonipizza"}

    def __repr__(self):
        return f"<PepperoniPizza: {self.name}>"


class AllMeatPizza(Pizza):
    __tablename__ = "allmeat_pizzas"
    id = db.Column(db.Integer, db.ForeignKey("pizzas.id"), primary_key=True)

    __mapper_args__ = {"polymorphic_identity": "allmeatpizza"}

    def __repr__(self):
        return f"<AllMeatPizza: {self.name}>"


# ----------------------
# DRINKS
# ----------------------


class Drinks(ProductItem):
    __tablename__ = "drinks"
    id = db.Column(db.Integer, db.ForeignKey("product_items.id"), primary_key=True)

    __mapper_args__ = {"polymorphic_identity": "drinks"}

    def __repr__(self):
        return f"<Drink: {self.name}>"


class Coke(Drinks):
    __tablename__ = "cokes"
    id = db.Column(db.Integer, db.ForeignKey("drinks.id"), primary_key=True)

    __mapper_args__ = {"polymorphic_identity": "coke"}

    def __repr__(self):
        return f"<Coke : {self.name}"


class IcedTea(Drinks):
    __tablename__ = "icedteas"
    id = db.Column(db.Integer, db.ForeignKey("drinks.id"), primary_key=True)

    __mapper_args__ = {"polymorphic_identity": "icedtea"}

    def __repr__(self):
        return f"<Iced Tea: {self.name}"


class BottledWater(Drinks):
    __tablename__ = "bottledwaters"
    id = db.Column(db.Integer, db.ForeignKey("drinks.id"), primary_key=True)

    __mapper_args__ = {"polymorphic_identity": "bottledwater"}

    def __repr__(self):
        return f"<Bottled Water : {self.name}"


# ----------------------
# INGREDIENTS
# ----------------------


class IngredientItem(ProductItem):
    __tablename__ = "ingredient_items"
    id = db.Column(db.Integer, db.ForeignKey("product_items.id"), primary_key=True)
    supplier_id = db.Column(db.Integer, db.ForeignKey("suppliers.id"), nullable=False)
    supplier = db.relationship("Supplier", backref="ingredients")

    __mapper_args__ = {"polymorphic_identity": "ingredientitem"}

    def __repr__(self):
        return f"<IngredientItem: {self.name}, Supplier: {self.supplier.name}>"


class Bread(IngredientItem):
    __tablename__ = "breads"
    id = db.Column(db.Integer, db.ForeignKey("ingredient_items.id"), primary_key=True)

    __mapper_args__ = {"polymorphic_identity": "bread"}

    def __repr__(self):
        return f"<Bread: {self.name}>"


class Hotdog(IngredientItem):
    __tablename__ = "hotdogs"
    id = db.Column(db.Integer, db.ForeignKey("ingredient_items.id"), primary_key=True)

    __mapper_args__ = {"polymorphic_identity": "hotdog"}

    def __repr__(self):
        return f"<Hotdog: {self.name}>"


class Sauce(IngredientItem):
    __tablename__ = "sauces"
    id = db.Column(db.Integer, db.ForeignKey("ingredient_items.id"), primary_key=True)

    __mapper_args__ = {"polymorphic_identity": "sauce"}

    def __repr__(self):
        return f"<Sauce: {self.name}>"
