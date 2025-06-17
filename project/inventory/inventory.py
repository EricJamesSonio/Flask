from models import ProductItem


class Inventory:
    def __init__(self, db_session):
        self.db_session = db_session

    def add_item(self, item: ProductItem):
        try:
            existing_item = ProductItem.query.filter_by(
                name=item.name, category=item.category
            ).first()

            if existing_item:
                if not hasattr(existing_item, "quantity") or not hasattr(
                    item, "quantity"
                ):
                    print("❌ Item exists but lacks 'quantity' attribute.")
                    return

                existing_item.quantity += item.quantity
                self.db_session.commit()
                print(f"✅ Successfully added stock to existing item: {existing_item}")
                return

            self.db_session.add(item)
            self.db_session.commit()
            print(f"✅ Successfully added new item: {item}")

        except Exception as e:
            print(f"❌ Failed to add item: {e}")

    def reduce_stock(self, item_id, amount):
        item = ProductItem.query.get(item_id)
        if not item:
            print("Doesnt exist")
            return

        if not hasattr(item, "quantity"):
            print("No attributes ")
            return

        try:
            item.quantity -= amount
            self.db_session.commit()
            print("Successfully Reduced stock")
        except Exception as e:
            print(f"Failed to reduce stock {e}")

    def increase_stock(self, item_id, amount):
        item = ProductItem.query.get(item_id)
        if not item:
            print(f"Item Doesnt exist")
            return

        if not hasattr(item, "quantity"):
            print("Doesn't have attribute quantity")
            return

        try:
            item.quantity += amount
            self.db_session.commit()
            print("Successfully !")
        except Exception as e:
            print(f"Error exception Failed {e}")

    def show_all_items(self):
        items = ProductItem.query.all()
        print("\n📦 Inventory Items:")
        for item in items:
            print(
                f"- ID: {item.id} | Name: {item.name} | Type: {item.type} | Qty: {item.quantity} | Category: {item.category} | Price: ₱{item.price}"
            )
