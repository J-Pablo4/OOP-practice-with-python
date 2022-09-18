class Item:
    def __init__(self, name, price=0, quantity=0):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculate_total_price(self):
        return self.price * self.quantity


item1 = Item("Phone", 100)

item2 = Item("Laptop", 1000)

item2.has_numpad = False

