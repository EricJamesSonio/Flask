from extension import db


class Customer(db.Model):
    __tablename__ = "customers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    orders = db.relationship("Order", backref="order", lazy=True)

    __mapper_args__ = {"polymorphic_identity": "customer"}

    def __repr__(self):
        return f"Customer : {self.name}, Id : {self.id}"
