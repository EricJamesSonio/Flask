from models import ProductItem


class Inventory:
    def __init__(self, db_session):
        self.db_session = db_session

    def add_item(self, item: ProductItem):
        self.db_session.add(item)
        self.db_session.commit()
        print(f"Successfully Added Item : {item}")

    def reduce_stock(self, item_id, amount):
        item = ProductItem.query.get(item_id)
        if item:
            if hasattr(item, "quantity"):
                item.quantity -= amount
                self.db_session.commit()
                print(f"Successfully Updated Item : {item}")
                if item.quantity <= 0:
                    self.db_session.delete(item)
                    self.db_session.commit()
                    print("Deleted Item, Reason : Quantity = 0")
            else:
                print("Doesn't have Quanttiy Attribute")
        else:
            print("Not Successful")

    def increase_stock(self, item_id, amount):
        item = ProductItem.query.get(item_id)
        if item:
            if hasattr(item, "quantity"):
                item.quantity += amount
                self.db_session.commit()
                print(f"Successfully Increase Amount {item}")
            else:
                print("Doesn't have Quantity Attribute")
        else:
            print(f"Item with Id : {item_id} doesn't exist")

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
