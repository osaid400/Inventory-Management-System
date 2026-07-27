# INVENTORY MANAGEMENT SYSTEM
# Author: Muhammad Abdullah Farooq
# Language: Python

import json
import os
import sys

class Product:
    def __init__(self, product_id, name, category, price, quantity):
        self.product_id = int(product_id)
        self.name = str(name).strip()
        self.category = str(category).strip()
        self.price = float(price)
        self.quantity = int(quantity)

    def update(self, name=None, category=None, price=None, quantity=None):
        if name and name.strip():
            self.name = name.strip()
        if category and category.strip():
            self.category = category.strip()
        if price is not None and price > 0:
            self.price = price
        if quantity is not None and quantity >= 0:
            self.quantity = quantity

    def __str__(self):
        formatted_price = f"Rs. {self.price:,.2f}"
        return f"{self.product_id:<15} {self.name:<25} {self.category:<20} {formatted_price:<20} {self.quantity:<10}"

    def to_dict(self):
        return {
            "Product ID": self.product_id,
            "Name": self.name,
            "Category": self.category,
            "Price": self.price,
            "Stock": self.quantity,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            product_id=data["Product ID"],
            name=data["Name"],
            category=data["Category"],
            price=data["Price"],
            quantity=data["Stock"],
        )


class InventoryManager:
    def __init__(self, filename="products.json"):
        self.filename = filename
        self.products = []
        self.load_products()

        if not self.products:
            initial_data = [
                {"Product ID": 101, "Name": "Keyboard", "Category": "Electronics", "Price": 2500.0, "Stock": 15},
                {"Product ID": 102, "Name": "Mouse", "Category": "Electronics", "Price": 1200.0, "Stock": 25},
                {"Product ID": 103, "Name": "Monitor", "Category": "Electronics", "Price": 28500.0, "Stock": 8},
                {"Product ID": 104, "Name": "Laptop", "Category": "Electronics", "Price": 125000.0, "Stock": 5},
                {"Product ID": 105, "Name": "USB Flash Drive", "Category": "Accessories", "Price": 1800.0, "Stock": 30},
                {"Product ID": 106, "Name": "External Hard Drive", "Category": "Storage", "Price": 14500.0, "Stock": 10},
                {"Product ID": 107, "Name": "Printer", "Category": "Office", "Price": 22000.0, "Stock": 6},
                {"Product ID": 108, "Name": "Notebook", "Category": "Stationery", "Price": 350.0, "Stock": 100},
                {"Product ID": 109, "Name": "Pen", "Category": "Stationery", "Price": 50.0, "Stock": 250},
                {"Product ID": 110, "Name": "Office Chair", "Category": "Furniture", "Price": 18500.0, "Stock": 7},
                {"Product ID": 111, "Name": "Desk", "Category": "Furniture", "Price": 32000.0, "Stock": 4},
                {"Product ID": 112, "Name": "Headphones", "Category": "Electronics", "Price": 6500.0, "Stock": 18},
                {"Product ID": 113, "Name": "Webcam", "Category": "Electronics", "Price": 5400.0, "Stock": 12},
                {"Product ID": 114, "Name": "Microphone", "Category": "Electronics", "Price": 8900.0, "Stock": 9},
                {"Product ID": 115, "Name": "Router", "Category": "Networking", "Price": 7600.0, "Stock": 11},
                {"Product ID": 116, "Name": "Power Bank", "Category": "Accessories", "Price": 4200.0, "Stock": 20},
                {"Product ID": 117, "Name": "Smartphone", "Category": "Electronics", "Price": 78000.0, "Stock": 9},
                {"Product ID": 118, "Name": "Tablet", "Category": "Electronics", "Price": 56000.0, "Stock": 7},
                {"Product ID": 119, "Name": "Calculator", "Category": "Office", "Price": 1800.0, "Stock": 22},
                {"Product ID": 120, "Name": "Projector", "Category": "Office", "Price": 47000.0, "Stock": 3},
                {"Product ID": 121, "Name": "Ethernet Cable", "Category": "Networking", "Price": 650.0, "Stock": 50},
                {"Product ID": 122, "Name": "HDMI Cable", "Category": "Accessories", "Price": 900.0, "Stock": 40},
                {"Product ID": 123, "Name": "SSD 512GB", "Category": "Storage", "Price": 9800.0, "Stock": 14},
                {"Product ID": 124, "Name": "Gaming Mouse", "Category": "Electronics", "Price": 4200.0, "Stock": 16},
                {"Product ID": 125, "Name": "Mechanical Keyboard", "Category": "Electronics", "Price": 8500.0, "Stock": 10},
            ]
            self.products = [Product.from_dict(item) for item in initial_data]
            self.save_products()

    def load_products(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    data = json.load(file)
                    self.products = [Product.from_dict(item) for item in data]
            except (json.JSONDecodeError, ValueError, OSError):
                self.products = []
        else:
            self.products = []

    def save_products(self):
        with open(self.filename, "w") as file:
            data = [prod.to_dict() for prod in self.products]
            json.dump(data, file, indent=4)

    def _find_by_id(self, product_id):
        for prod in self.products:
            if prod.product_id == product_id:
                return prod
        return None

    def _print_header(self):
        print("=" * 95)
        print(f"{'Product ID':<15} {'Name':<25} {'Category':<20} {'Price':<20} {'Stock':<10}")
        print("=" * 95)

    def add_product(self):
        try:
            product_id = int(input("Enter Product ID: "))
        except ValueError:
            print("Invalid Product ID! Please enter a number.")
            return

        if product_id <= 0:
            print("Product ID must be greater than zero!")
            return

        if self._find_by_id(product_id):
            print("Product ID already exists!")
            return

        name = input("Enter Product Name: ").strip()
        if not name:
            print("Product Name cannot be empty!")
            return

        category = input("Enter Category Name: ").strip()
        if not category:
            print("Category Name cannot be empty!")
            return

        try:
            price = float(input("Enter Price: "))
            if price <= 0:
                print("Price must be greater than 0!")
                return
        except ValueError:
            print("Invalid Price! Please enter a valid number.")
            return

        try:
            quantity = int(input("Enter Stock Quantity: "))
            if quantity < 0:
                print("Stock cannot be negative!")
                return
        except ValueError:
            print("Invalid Stock! Please enter a valid number.")
            return

        new_prod = Product(product_id, name, category, price, quantity)
        self.products.append(new_prod)
        self.save_products()
        print("New Product Added Successfully!")

    def view_products(self):
        if not self.products:
            print("No products in stock!")
            return

        self.products.sort(key=lambda p: p.product_id)
        self._print_header()
        for prod in self.products:
            print(prod)
        print("=" * 95)

    def search_product(self):
        print("=" * 95)
        print("\nSearch By:")
        print("1. Search by ID")
        print("2. Search by Name")
        print("3. Search by Category")
        print("=" * 95)

        try:
            choice = int(input("Enter your choice (1-3): "))
        except ValueError:
            print("Invalid choice! Please enter a number.")
            return

        matches = []
        if choice == 1:
            try:
                search_id = int(input("Enter Product ID: "))
            except ValueError:
                print("Invalid Product ID!")
                return
            prod = self._find_by_id(search_id)
            if prod:
                matches.append(prod)

        elif choice == 2:
            query = input("Enter Product Name: ").strip().lower()
            if not query:
                print("Search term cannot be empty!")
                return
            matches = [p for p in self.products if query in p.name.lower()]

        elif choice == 3:
            query = input("Enter Category Name: ").strip().lower()
            if not query:
                print("Search term cannot be empty!")
                return
            matches = [p for p in self.products if query in p.category.lower()]

        else:
            print("Invalid Choice!")
            return

        if not matches:
            print("No matching product found!")
            return

        self._print_header()
        for prod in matches:
            print(prod)
        print("=" * 95)

    def update_product(self):
        try:
            search_id = int(input("Enter Product ID to Update: "))
        except ValueError:
            print("Invalid Product ID!")
            return

        prod = self._find_by_id(search_id)
        if not prod:
            print("Product Not Found!")
            return

        print("\n--- Current Details ---")
        self._print_header()
        print(prod)
        print("=" * 95)

        name = input("Enter new Name (leave blank to keep current): ")
        category = input("Enter new Category (leave blank to keep current): ")
        price_in = input("Enter new Price (leave blank to keep current): ")
        quantity_in = input("Enter new Stock Quantity (leave blank to keep current): ")

        price = None
        if price_in.strip():
            try:
                price = float(price_in)
            except ValueError:
                print("Invalid price format. Keeping current price.")

        quantity = None
        if quantity_in.strip():
            try:
                quantity = int(quantity_in)
            except ValueError:
                print("Invalid stock format. Keeping current stock.")

        prod.update(name=name, category=category, price=price, quantity=quantity)
        self.save_products()
        print("Product Updated Successfully!")

    def delete_product(self):
        try:
            search_id = int(input("Enter Product ID to Delete: "))
        except ValueError:
            print("Invalid Product ID!")
            return

        prod = self._find_by_id(search_id)
        if not prod:
            print("Product Not Found!")
            return

        confirm = input(f"Are you sure you want to delete '{prod.name}'? (y/n): ").strip().lower()
        if confirm == "y":
            self.products.remove(prod)
            self.save_products()
            print("Product Deleted Successfully!")
        else:
            print("Deletion cancelled.")

    def increase_stock(self):
        try:
            search_id = int(input("Enter Product ID: "))
        except ValueError:
            print("Invalid Product ID!")
            return

        prod = self._find_by_id(search_id)
        if not prod:
            print("Product Not Found!")
            return

        try:
            qty = int(input("Enter quantity to add: "))
            if qty <= 0:
                print("Quantity must be greater than zero!")
                return
        except ValueError:
            print("Invalid quantity!")
            return

        prod.quantity += qty
        self.save_products()
        print(f"Stock increased! New quantity for '{prod.name}' is {prod.quantity}.")

    def decrease_stock(self):
        try:
            search_id = int(input("Enter Product ID: "))
        except ValueError:
            print("Invalid Product ID!")
            return

        prod = self._find_by_id(search_id)
        if not prod:
            print("Product Not Found!")
            return

        try:
            qty = int(input("Enter quantity to remove: "))
            if qty <= 0:
                print("Quantity must be greater than zero!")
                return
        except ValueError:
            print("Invalid quantity!")
            return

        if qty > prod.quantity:
            print(f"Insufficient stock! Available stock is only {prod.quantity}.")
            return

        prod.quantity -= qty
        self.save_products()
        print(f"Stock decreased! New quantity for '{prod.name}' is {prod.quantity}.")

    def low_stock_alert(self, threshold=5):
        try:
            custom_threshold = input(f"Enter threshold limit (default {threshold}): ").strip()
            if custom_threshold:
                threshold = int(custom_threshold)
        except ValueError:
            print("Invalid threshold number! Using default (5).")
            threshold = 5

        low_stock_items = [p for p in self.products if p.quantity <= threshold]

        if not low_stock_items:
            print(f"\nAll items have stock greater than {threshold}!")
            return

        print(f"\n--- LOW STOCK ALERT (Items <= {threshold}) ---")
        self._print_header()
        for prod in low_stock_items:
            print(prod)
        print("=" * 95)


def main():
    print("============ Welcome to Inventory Management System =============")
    manager = InventoryManager()

    while True:
        print("\n=============== Select Option (0-8) ===============")
        print("1. Add Product")
        print("2. View All Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Increase Stock")
        print("7. Decrease Stock")
        print("8. Low Stock Alert")
        print("0. Exit")
        print("======================================================")

        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid Choice! Please enter a number.")
            continue

        if choice == 1:
            manager.add_product()
        elif choice == 2:
            manager.view_products()
        elif choice == 3:
            manager.search_product()
        elif choice == 4:
            manager.update_product()
        elif choice == 5:
            manager.delete_product()
        elif choice == 6:
            manager.increase_stock()
        elif choice == 7:
            manager.decrease_stock()
        elif choice == 8:
            manager.low_stock_alert()
        elif choice == 0:
            print("---------------------------------------------------")
            print("Exiting the Inventory Management System.")
            print("Thank you for using the system. Goodbye!")
            print("---------------------------------------------------")
            sys.exit()
        else:
            print("Invalid Choice! Choose between 0 to 8.")

if __name__ == "__main__":
    main()