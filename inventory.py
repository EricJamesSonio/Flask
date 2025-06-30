from abc import ABC, abstractmethod

class ProductItem:
    def __init__(self, name, code, price, quantity):
        self.name = name
        self.code = code
        self.price = price
        self.quantity = quantity
        
    def details(self):
        return f"Name : {self.name}, Code : {self.code} , Price : {self.price}, Quantity : {self.quantity}"


class Inventory:
    def __init__(self):
        self.inventoryviewer = InventoryViewer(self)
        self.items = []
        self.logger = Logger()
        self.stockalertsystem = StockAlertSystem()
        self.observers = [self.logger, self.stockalertsystem]
        self.threshold = 10
        
    
    def find_item(self, code) :
        for item in self.items:
            if item.code == code:
                return item
        return None

    def add_item(self, item)  :
        existing_item = self.find_item(item.code)
        if existing_item:
            existing_item.quantity += item.quantity
            
        else:
            self.items.append(item)
            
    def remove_item(self, code):
        item = self.find_item(code)
        if item:
            self.items.remove(item)
        else:
            return None
        
    def increase_stock(self, item, quantity):
        if not item:
            return "Item Doesn't Exist"
        else:
            item.quantity += quantity
            
    def decrease_stock(self, item, quantity):
        if not item:
            return "Item Doesn't Exist"
    
        item.quantity -= quantity
        if item.quantity <= 0:
            self.remove_item(item)
            
        self.is_low_stock(item)
        
            
        
        
    def notify(self, message):
        for observer in self.observers:
            observer.update(message)
        
    def display_items(self):
        self.inventoryviewer.display_items()
        
    def set_threshold(self, threshold):
        self.threshold = threshold
        
    def is_low_stock(self, item):
        if item.quantity <= self.threshold:
            print(f"Low Stock : {item.name}")
        return False
    
    def check_stock(self):
        for item in self.items:
            self.is_low_stock(item)
            

    

class InventoryViewer:
    def __init__(self, inventory : Inventory) :
        self.inventory = inventory
        
    def display_items(self):
        for item in self.inventory.items:
            print(item.details())
            
class Observer(ABC):
    def __init__(self):
        self.records = []
        
    def update(self, message):
        pass
    
class Logger(Observer):
    def update(self, message):
        return super().update(message)
    
class StockAlertSystem(Observer):
    pass

class Store:
    def __init__(self, name, id, location) :
        self.name = name
        self.id = id
        self.location = location
        self.inventory = Inventory()
            

    def add_item(self, item):
        self.inventory.add_item(item)
        
    def find_item(self, code):
        return self.inventory.find_item(code)
        
    def remove_item(self, code):
        self.inventory.remove_item(code)
        
    def display_items(self):
        self.inventory.display_items()
        
    def is_low_stock(self, item):
        self.inventory.is_low_stock(item)
        
    
        
    

if __name__ == "__main__":
    p1 = ProductItem("Coke", 12, 20, 10)
    p2 = ProductItem("Sprite", 13, 20, 2)
    p3 = ProductItem("Milk", 14, 20, 30)
    p4 = ProductItem("Hey", 122, 20, 10)
    p5 = ProductItem("ham", 212, 20, 10)
    store = Store("Eric james Store", 1, "Pandi")
    
    store.add_item(p1)
    store.add_item(p2)
    store.add_item(p3)
    store.add_item(p4)
    store.add_item(p5)
    store.display_items()

    store.inventory.check_stock()

    
