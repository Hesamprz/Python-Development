products = [
    {"name": "Apple" , "price": 12},
    {"name": "Banana" , "price": 23},
    {"name": "Orange" , "price": 15}
]

def add():
    name = input("Enter the name of product: ")
    price = float(input("Enter the price of product: "))
    products.append({"name": name , "price": price})
    print(f"Product {name} added successfully.")
    
def find():
    name = input("Enter product name to find: ")
    for product in products:
        if product['name'] == name:
            print(f"Product found: {product}")
            return product
    print("Product not found.")
    return None

def remove():
    name = input("Enter product name to remove: ")
    for product in products:
        if product['name'] == name:
            products.remove(product)
            print(f"Product {name} removed successfully.")
            return True
    print("Product not found.")
    return False

def update():
    name = input("Enter product name to update: ")
    for product in products:
        if product['name'] == name:
            new_name = input("Enter new product name: ")
            new_price = float(input("Enter new product price: "))
            product['name'] = new_name
            product['price'] = new_price
            print(f"Product {name} updated successfully.")
            return True
    print("Product not found.")
    return False
