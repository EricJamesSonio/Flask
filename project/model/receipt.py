from extension import db
from datetime import datetime


class Receipt(db.Model):
    __tablename__ = "receipts"
    id = db.Column(db.Integer, primary_key=True)
    receipt_code = db.Column(db.String(20), unique=True, nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False)
    total_amount = db.Column(db.float, nullable=False)
    discount = db.Column(db.float, default=0.0)
    subtotal = db.Column(db.float, nullable=False)
    amount_paid = db.Column(db.float, nullable=False)
    change = db.Column(db.float, nullable=False)

    payment_time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    __mapper_args__ = {"polymorphic_identity": "receipt"}

    def __repr__(self):
        return f"Receipt Id : {self.id}"
