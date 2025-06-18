from datetime import datetime
from extension import db


class OrderItem(db.Model):
    __tablename__ = "orderitems"
    id = db.Column(db.Integer, db.ForeignKey("product_items.id"), nullable=False)
    product = db.relationship("ProductItem", backref="productitem", lazy=True)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    __mapper_args__ = {"polymorphic_identity": "orderitem"}

    def __repr__(self):
        return f"Order Item : {self.product.name} Qtty : {self.product.quantity} Price : {self.product.price}"


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column(db.Integer, primary_key=True)
    # customer_id = db.Column(db.String, db.ForeignKey("customers.id"), nullable=False) Remove this since i change my mind lol
    orders = db.relationship("OrderItem", backref="orderitem", lazy=True)
    created_time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    order_code = db.Column(db.String(20), nullable=False)

    __mapper_args__ = {"polymorphic_identity": "order"}

    def __repr__(self):
        return f"Order Id : {self.id}, Customer Id : {self.customer_id}, Created Time : {self.created_time}"
