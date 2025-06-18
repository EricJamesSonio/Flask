from extension import db
from model.product import Burger, CheeseBurger, SpicyBurger, OverloadBurger
from main import app  # Import your Flask app for app context

with app.app_context():
    db.create_all()

    if not Burger.query.first():
        cheeseburger = CheeseBurger(
            name="Cheesy Delight", category="Burger", price=120.0, quantity=10
        )
        spicyburger = SpicyBurger(
            name="Hot Lava", category="Burger", price=130.0, quantity=8
        )
        overloadburger = OverloadBurger(
            name="Mega Stack", category="Burger", price=150.0, quantity=5
        )

        db.session.add_all([cheeseburger, spicyburger, overloadburger])
        db.session.commit()
        print("✅ Seeded burger data.")
    else:
        print("ℹ️ Burgers already seeded.")
