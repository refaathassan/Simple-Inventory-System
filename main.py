import traceback
import numpy as np

# Define a class to represent a product with name, price, and quantity attributes
class product:
    def __init__(self, name, price, quantity):
        # Initialize the product attributes (name, price, and quantity)
        self.name = name
        self.price = price
        self.quantity = quantity

    def display(self):
        # Method to display the product's details (name, price, and quantity)
        print("Product name: ", self.name)
        print("Price: $", self.price)
        print("Quantity in stock: ", self.quantity)

    def quantity_update(self, update):
        # Method to update the quantity of the product in stock
        self.quantity = update

    def total_value(self):
        # Method to calculate and return the total value of the product (price * quantity)
        return self.price * self.quantity

# Define a class to represent the product inventory that contains a list of products
class inventory:
    def __init__(self):
        # Initialize the inventory with a sample product
        self.lists = [product("Chipcy", 10, 3)]  # Example product with initial quantity of 3

    def display(self):
        # Method to display all products in the inventory
        if len(self.lists) >= 1:
            for product_instance in self.lists:
                # For each product in the inventory, display its details
                product_instance.display()

    def product_add(self, name, price, quantity):
        # Method to add a new product to the inventory
        self.lists.append(product(name, price, quantity))

    def product_quantity_updata(self, name, update):
        # Method to update the quantity of a specific product in the inventory
        for i in self.lists:
            if i.name == name:
                # If the product with the given name is found, update its quantity
                i.quantity_update(update)

    def total_inventory_value(self):
        # Method to calculate and return the total value of the entire inventory
        total = 0
        for i in self.lists:
            total += i.total_value()  # Sum the total value of each product in the inventory
        return total

# Define an exception handling function to catch and handle specific exceptions
def exception_handling(ex):
    # Handle different types of exceptions and provide appropriate messages
    if isinstance(ex, FileNotFoundError):
        print("Please make sure you have a file to save.")
        main_program()
    elif isinstance(ex, PermissionError):
        print("Please make sure you have permission to open and write in this file.")
        main_program()
    elif isinstance(ex, IndexError):
        print("Please make sure you chose a correct line index.")
        main_program()
    elif isinstance(ex, ValueError):
        print("Please make sure you enter an integer number as a choice.")
        main_program()
    else:
        # Default case for any unhandled exception
        main_program()

# Main function where the user interacts with the inventory system
def main_program():
    try:
        # Create a new inventory instance
        inv = inventory()

        while True:
            # Display menu options to the user
            print("Please enter the option:\n1 - Display products \n2 - Add product")
            user_in = int(input("3 - Update quantity\n4 - Display total inventory value\nYour choice: "))

            # Use match-case to handle different user choices
            match user_in:
                case 1:
                    # Option 1: Display all products in the inventory
                    inv.display()
                case 2:
                    # Option 2: Add a new product to the inventory
                    name = input("Please enter the product name: ")
                    price = int(input("Enter the price: $"))
                    quantity = int(input("Enter the quantity: "))  # Get the quantity from the user
                    inv.product_add(name, price, quantity)  # Add the new product to the inventory
                case 3:
                    # Option 3: Update the quantity of a specific product
                    title = input("Please enter the product name: ")
                    availability = int(input("Please enter the updated quantity: "))  # Update the product's quantity
                    inv.product_quantity_updata(title, availability)  # Update quantity in the inventory
                case 4:
                    # Option 4: Display the total value of all products in the inventory
                    print("The total inventory value is: $", inv.total_inventory_value())
                case _:
                    # If the user enters an invalid option, notify them
                    print("Please enter a valid choice.")
    except Exception:
        # If an exception occurs, handle it by calling exception_handling
        exception_handling(Exception)

# Start the program
main_program()
