class Inventory:
    def __init__(self, db_session, model):
        self.db_session = db_session
        self.model = model

    def add_item(self, item):
        try:
            existing_item = self.model.query.filter_by(
                name=item.name, category=item.category
            ).first()

            if existing_item:
                if hasattr(existing_item, "quantity") and hasattr(item, "quantity"):
                    existing_item.quantity += item.quantity
                    self.db_session.commit()
                    print(
                        f"✅ Added stock to existing {self.model.__name__}: {existing_item}"
                    )
                    return

                print("❌ Item exists but lacks 'quantity' attribute.")
                return

            self.db_session.add(item)
            self.db_session.commit()
            print(f"✅ Added new {self.model.__name__}: {item}")

        except Exception as e:
            print(f"❌ Failed to add item: {e}")

    def reduce_stock(self, item_id, amount):
        item = self.model.query.get(item_id)
        if not item or not hasattr(item, "quantity"):
            print("❌ Item not found or missing 'quantity'")
            return

        try:
            item.quantity -= amount
            self.db_session.commit()
            print("✅ Reduced stock")
        except Exception as e:
            print(f"❌ Error: {e}")

    def increase_stock(self, item_id, amount):
        item = self.model.query.get(item_id)
        if not item or not hasattr(item, "quantity"):
            print("❌ Item not found or missing 'quantity'")
            return

        try:
            item.quantity += amount
            self.db_session.commit()
            print("✅ Increased stock")
        except Exception as e:
            print(f"❌ Error: {e}")

    def show_all_items(self):
        items = self.model.query.all()
        print(f"\n📦 {self.model.__name__} Inventory:")
        for item in items:
            print(item)
