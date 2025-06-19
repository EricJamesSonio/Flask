from flask import Blueprint, jsonify, request
from model.product import ProductItem
from extension import db

product_bp = Blueprint("product_bp", __name__, url_prefix="/api/products")


@product_bp.route("/", methods=["GET"])
def get_all_products():
    products = ProductItem.query.all()
    return jsonify(
        [
            {
                "id": p.id,
                "name": p.name,
                "price": p.price,
                "quantity": p.quantity,
                "type": p.type,
            }
            for p in products
        ]
    )


# Filter by type/category (e.g., burgers, drinks)
@product_bp.route("/filter", methods=["GET"])
def get_products_by_type():
    product_type = request.args.get("type")
    if not product_type:
        return jsonify({"error": "Type parameter is required"}), 400

    filtered_products = ProductItem.query.filter_by(type=product_type).all()
    return jsonify(
        [
            {
                "id": p.id,
                "name": p.name,
                "price": p.price,
                "quantity": p.quantity,
                "type": p.type,
            }
            for p in filtered_products
        ]
    )


@product_bp.route("/filter", methods=["GET"])
def filter_products():
    product_type = request.args.get("type")
    if not product_type:
        return jsonify({"error": "Missing product type"}), 400

    filtered = ProductItem.query.filter_by(type=product_type).all()
    result = [
        {
            "id": p.id,
            "name": p.name,
            "price": p.price,
            "quantity": p.quantity,
            "type": p.type,
            "description": p.description if hasattr(p, "description") else "",
        }
        for p in filtered
    ]
    return jsonify(result), 200
