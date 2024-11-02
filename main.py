class Item:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    def print_item_info(self):
        print("Name of item", self.name)
        print("price", self.price)


item1=Item(name=("coffe"),price=(10))
item2=Item(name=("cake"),price=(20))
item3=Item(name=("nothing"),price=(50))


class Customer:
    def __init__(self,name):
        self.name = name
        self.orders = []
    def order(self,order):
        self.orders.append(order)


class Order:
    def __init__(self):
        self.items = []
    
    def add__item(self,item):
        self.items.append(item)

order1 = Order()
order1.add__item(item2)
order1.add__item(item1)

customer1 = Customer("Lee Lee")
customer1.orders(order1)

print(customer1)
print(order1)

order2 = Order()
order2.add__item(item3)
order2.add__item(item1)

customer2= Customer("Adik")
customer2.orders(order2)

print(customer2)
print(order2)
