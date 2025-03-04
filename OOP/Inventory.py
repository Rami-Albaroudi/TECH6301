class Product:

    products = []
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        Product.products.append(self)

    def display_info(self):
        print(f"There are {self.quantity} units of {self.name} available at {self.price} each.")
    
    def update_quantity(self, quantity_change):
        self.quantity += quantity_change
        print(f"The new product quantity is {self.quantity}")

def add_product(name, price, quantity):
    return Product(name, price, quantity)

def display_total_values():
    total = 0
    for product in Product.products:
        value = product.price * product.quantity
        total += value
        print(f"Total inventory value is {total}")

product = add_product("Doohickey", 10.99, 5)

product.update_quantity(100)

display_total_values()