from extension import db


class Supplier(db.Model):
    __tablename__ = "suppliers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    contact = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(100), nullable=False)

    __mapper_args__ = {"polymorphic_identity": "supplier"}
