# Assuming you're in a Flask app context
from inventory import Inventory
from models import db, CheeseBurger

inv = Inventory(db.session)

# Add a new cheeseburger
burger = CheeseBurger(
    name="Classic Cheeseburger", category="Burgers", price=120.0, quantity=10
)
inv.add_item(burger)

# Increase stock
inv.increase_stock(item_id=1, amount=5)

# Reduce stock
inv.reduce_stock(item_id=1, amount=3)

# Show all items
inv.show_all_items()
