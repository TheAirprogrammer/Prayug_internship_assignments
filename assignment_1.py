class Product:
    def __init__(self, name, price, quantity, location):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.location = location

    def __str__(self):
        return f"{self.name} - Price: ${self.price:.2f}, Quantity: {self.quantity}, Location: {self.location}"

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.name in self.products:
            print(f"Warning: {product.name} already exists.")
        else:
            self.products[product.name] = product

    def update_quantity(self, product_name, quantity):
        if product_name in self.products:
            self.products[product_name].quantity += quantity
        else:
            print("Product not found.")

    def remove_product(self, product_name):
        if product_name in self.products:
            del self.products[product_name]
        else:
            print("Product not found.")

    def display_inventory(self):
        print("\nCurrent Inventory:")
        for product in self.products.values():
            print(product)

def main():
    inventory = Inventory()

    while True:
        print("\n1. Add Product")
        print("2. Update Quantity")
        print("3. Remove Product")
        print("4. Display Inventory")
        print("5. Check Availability")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter initial quantity: "))
            location = input("Enter product location: ")
            product = Product(name, price, quantity, location)
            inventory.add_product(product)
        elif choice == "2":
            name = input("Enter product name: ")
            quantity = int(input("Enter quantity to add/remove: "))
            inventory.update_quantity(name, quantity)
        elif choice == "3":
            name = input("Enter product name: ")
            inventory.remove_product(name)
        elif choice == "4":
            inventory.display_inventory()
        elif choice == "5":
            name = input("Enter product name: ")
            if name in inventory.products:
                product = inventory.products[name]
                if product.quantity > 0:
                    print(f"{name} is available.")
                else:
                    print(f"{name} is out of stock.")
            else:
                print("Product not found.")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()