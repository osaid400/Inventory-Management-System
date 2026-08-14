# src/UI.py

csv = __import__('csv')
sys = __import__('sys')
import os
from datetime import datetime
from src.manager import DatabaseManager
from src.models import HistoryLog, Product, Supplier, hash_password

class InventorySystem:
    def __init__(self):
        self.db = DatabaseManager()
        self.users = self.db.load_users()
        self.suppliers = self.db.load_suppliers()
        self.products = self.db.load_products()
        self.history = self.db.load_history()
        self.current_user = None

    def log_action(self, action_type, details):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        username = self.current_user.username if self.current_user else "System"
        log = HistoryLog(timestamp, username, action_type, details)
        self.history.append(log)
        self.db.save_history(self.history)

    def login(self):
        print("================== User Login ==================")
        print("1. Admin")
        print("2. User")
        choice = input("Select Role (1-2): ").strip()

        if choice == "1":
            role = "Admin"
        elif choice == "2":
            role = "Staff"
        else:
            print("Invalid role selection!")
            return False

        target_user = None
        for user in self.users:
            if user.role == role:
                target_user = user
                break

        if not target_user:
            print("User profile not found!")
            return False

        if role == "Admin":
            while True:
                password = input("Enter Password: ").strip()
                if hash_password(password) == target_user.password_hash:
                    self.current_user = target_user
                    print(f"Login Successful! Welcome, {target_user.username} ({target_user.role})")
                    return True
                print("Invalid password! Try again.")
        else:
            attempts = 3
            while attempts > 0:
                password = input(f"Enter Password ({attempts} attempts left): ").strip()
                if hash_password(password) == target_user.password_hash:
                    self.current_user = target_user
                    print(f"Login Successful! Welcome, {target_user.username} ({target_user.role})")
                    return True
                attempts -= 1
                print("Invalid password!")
            print("Maximum login attempts exceeded. Access locked.")
            return False

    def _find_product_by_id(self, pid):
        for p in self.products:
            if p.product_id == pid:
                return p
        return None

    def _find_supplier_by_id(self, sid):
        for s in self.suppliers:
            if s.supplier_id == sid:
                return s
        return None

    def _print_product_header(self):
        print("=" * 100)
        print(f"{'ID':<10} {'Name':<22} {'Category':<18} {'Price':<18} {'Stock':<10} {'Supplier ID'}")
        print("=" * 100)

    def _print_supplier_header(self):
        print("=" * 88)
        print(f"{'Supplier ID':<15} {'Name':<25} {'Phone':<18} {'Email':<30}")
        print("=" * 88)

    def view_products(self):
        if not self.products:
            print("No products available.")
            return
        self.products.sort(key=lambda x: x.product_id)
        self._print_product_header()
        for p in self.products:
            print(f"{p.product_id:<10} {p.name:<22} {p.category:<18} {f'Rs. {p.price:,.2f}':<18} {p.quantity:<15} {p.supplier_id}")
        print("=" * 100)

    def search_product(self):
        query = input("Enter search keyword (Name or Category): ").strip().lower()
        if not query:
            print("Search query cannot be empty.")
            return
        matches = [p for p in self.products if query in p.name.lower() or query in p.category.lower()]
        if not matches:
            print("No products found matching query.")
            return
        self._print_product_header()
        for p in matches:
            print(f"{p.product_id:<10} {p.name:<22} {p.category:<18} {f'Rs. {p.price:,.2f}':<18} {p.quantity:<10} {p.supplier_id}")
        print("=" * 110)

    def add_product(self):
        if self.current_user.role != "Admin":
            print("Access Denied! Admins only.")
            return

        pid = max((p.product_id for p in self.products), default=100) + 1
        name = input("Enter Product Name: ").strip()
        if not name:
            print("Name cannot be empty.")
            return

        category = input("Enter Category: ").strip()
        if not category:
            print("Category cannot be empty.")
            return

        try:
            price = float(input("Enter Price: "))
            if price <= 0:
                print("Price must be greater than zero.")
                return
        except ValueError:
            print("Invalid price input.")
            return

        try:
            qty = int(input("Enter Initial Stock Quantity: "))
            if qty < 0:
                print("Stock cannot be negative.")
                return
        except ValueError:
            print("Invalid stock input.")
            return

        self.view_suppliers()
        try:
            sid = int(input("Enter Supplier ID: "))
            if not self._find_supplier_by_id(sid):
                print("Supplier ID does not exist.")
                return
        except ValueError:
            print("Invalid supplier ID.")
            return

        new_prod = Product(pid, name, category, price, qty, sid)
        self.products.append(new_prod)
        self.db.save_products(self.products)
        self.log_action("ADD_PRODUCT", f"Added product {name} with ID {pid}")
        print(f"Product added successfully with ID {pid}.")

    def update_product(self):
        if self.current_user.role != "Admin":
            print("Access Denied! Admins only.")
            return

        try:
            pid = int(input("Enter Product ID to Update: "))
        except ValueError:
            print("Invalid ID.")
            return

        p = self._find_product_by_id(pid)
        if not p:
            print("Product not found.")
            return

        name = input("Enter new Name (leave blank to skip): ")
        category = input("Enter new Category (leave blank to skip): ")
        price_in = input("Enter new Price (leave blank to skip): ")
        qty_in = input("Enter new Stock (leave blank to skip): ")
        sup_in = input("Enter new Supplier ID (leave blank to skip): ")

        price = float(price_in) if price_in.strip() else None
        qty = int(qty_in) if qty_in.strip() else None
        sid = int(sup_in) if sup_in.strip() else None

        p.update(name=name, category=category, price=price, quantity=qty, supplier_id=sid)
        self.db.save_products(self.products)
        self.log_action("UPDATE_PRODUCT", f"Updated product ID {pid}")
        print("Product updated successfully.")

    def delete_product(self):
        if self.current_user.role != "Admin":
            print("Access Denied! Admins only.")
            return

        try:
            pid = int(input("Enter Product ID to Delete: "))
        except ValueError:
            print("Invalid ID.")
            return

        p = self._find_product_by_id(pid)
        if not p:
            print("Product not found.")
            return

        confirm = input(f"Are you sure you want to delete {p.name}? (y/n): ").strip().lower()
        if confirm == 'y':
            self.products.remove(p)
            self.db.save_products(self.products)
            self.log_action("DELETE_PRODUCT", f"Deleted product ID {pid}")
            print("Product deleted successfully.")
        else:
            print("Deletion cancelled.")

    def increase_stock(self):
        try:
            pid = int(input("Enter Product ID: "))
        except ValueError:
            print("Invalid ID.")
            return

        p = self._find_product_by_id(pid)
        if not p:
            print("Product not found.")
            return

        try:
            qty = int(input("Enter quantity to add (Purchase): "))
            if qty <= 0:
                print("Quantity must be greater than zero.")
                return
        except ValueError:
            print("Invalid quantity.")
            return

        p.quantity += qty
        self.db.save_products(self.products)
        self.log_action("PURCHASE_STOCK", f"Added {qty} units to product ID {pid}")
        print(f"Stock increased. New quantity: {p.quantity}")

    def decrease_stock(self):
        try:
            pid = int(input("Enter Product ID: "))
        except ValueError:
            print("Invalid ID.")
            return

        p = self._find_product_by_id(pid)
        if not p:
            print("Product not found.")
            return

        try:
            qty = int(input("Enter quantity to sell (Sale): "))
            if qty <= 0:
                print("Quantity must be greater than zero.")
                return
        except ValueError:
            print("Invalid quantity.")
            return

        if qty > p.quantity:
            print(f"Insufficient stock! Available: {p.quantity}")
            return

        p.quantity -= qty
        self.db.save_products(self.products)
        self.log_action("SALE_STOCK", f"Sold {qty} units of product ID {pid}")
        print(f"Stock decreased. Remaining quantity: {p.quantity}")

    def low_stock_alert(self):
        threshold = 5
        try:
            val = input("Enter threshold limit (default 5): ").strip()
            if val:
                threshold = int(val)
        except ValueError:
            threshold = 5

        items = [p for p in self.products if p.quantity <= threshold]
        if not items:
            print(f"No items found below stock threshold {threshold}.")
            return

        print(f"--- LOW STOCK ALERT (Stock <= {threshold}) ---")
        self._print_product_header()
        for p in items:
            print(f"{p.product_id:<10} {p.name:<22} {p.category:<18} {f'Rs. {p.price:,.2f}':<18} {p.quantity:<10} {p.supplier_id}")
        print("=" * 110)

    def manage_suppliers(self):
        if self.current_user.role != "Admin":
            print("Access Denied! Admins only.")
            return

        while True:
            print("\n================= Supplier Management ==============")
            print("1. View Suppliers")
            print("2. Add Supplier")
            print("0. Back to Main Menu")
            choice = input("Enter choice: ").strip()

            if choice == "1":
                self.view_suppliers()
            elif choice == "2":
                sid = max((s.supplier_id for s in self.suppliers), default=0) + 1
                name = input("Enter Supplier Name: ").strip()
                phone = input("Enter Phone Number: ").strip()
                email = input("Enter Email Address: ").strip()
                if name:
                    self.suppliers.append(Supplier(sid, name, phone, email))
                    self.db.save_suppliers(self.suppliers)
                    self.log_action("ADD_SUPPLIER", f"Added supplier {name}")
                    print("Supplier added successfully.")
                else:
                    print("Name cannot be empty.")
            elif choice == "0":
                break
            else:
                print("Invalid choice.")

    def view_suppliers(self):
        if not self.suppliers:
            print("No suppliers found.")
            return
        self.suppliers.sort(key=lambda x: x.supplier_id)
        self._print_supplier_header()
        for s in self.suppliers:
            print(s)
        print("=" * 88)

    def inventory_valuation_report(self):
        if self.current_user.role != "Admin":
            print("Access Denied! Admins only.")
            return

        total_value = 0
        report_lines = []
        report_lines.append("=" * 90)
        report_lines.append(f"{'Product Name':<25} {'Category':<20} {'Price':<15} {'Stock':<10} {'Total Value'}")
        report_lines.append("=" * 90)
        for p in self.products:
            val = p.price * p.quantity
            total_value += val
            report_lines.append(f"{p.name:<25} {p.category:<20} {f'Rs. {p.price:,.2f}':<15} {p.quantity:<10} {f'Rs. {val:,.2f}'}")
        report_lines.append("=" * 90)
        report_lines.append(f"Total Inventory Valuation: Rs. {total_value:,.2f}")
        report_lines.append("=" * 90)

        report_text = "\n".join(report_lines)
        print(report_text)

        filename = os.path.join("Reports", f"inventory_valuation_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(report_text)
        print(f"Report automatically saved to {filename}")

    def view_history(self):
        if self.current_user.role != "Admin":
            print("Access Denied! Admins only.")
            return

        if not self.history:
            print("No history logs recorded.")
            return

        print("=" * 110)
        print(f"{'Timestamp':<20} {'Username':<15} {'Action Type':<20} {'Details'}")
        print("=" * 110)
        for h in self.history:
            print(f"{h.timestamp:<20} {h.username:<15} {h.action_type:<20} {h.details}")
        print("=" * 110)

    def export_data(self):
        if self.current_user.role != "Admin":
            print("Access Denied! Admins only.")
            return

        print("1. Export Inventory to CSV")
        print("2. Export History Log to CSV")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            filename = os.path.join("Reports", "inventory_export.csv")
            with open(filename, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Product ID", "Name", "Category", "Price", "Stock", "Supplier ID"])
                for p in self.products:
                    writer.writerow([p.product_id, p.name, p.category, p.price, p.quantity, p.supplier_id])
            print(f"Inventory successfully exported to {filename}")
        elif choice == "2":
            filename = os.path.join("Reports", "history_export.csv")
            with open(filename, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Timestamp", "Username", "Action Type", "Details"])
                for h in self.history:
                    writer.writerow([h.timestamp, h.username, h.action_type, h.details])
            print(f"History log successfully exported to {filename}")
        else:
            print("Invalid choice.")

    def run(self):
        print("================== Inventory Management System ==================")
        while True:
            if not self.login():
                cont = input("Try again? (y/n): ").strip().lower()
                if cont != 'y':
                    break
                continue

            while self.current_user:
                if self.current_user.role == "Admin":
                    print("\n=============== Admin Menu ===============")
                    print("1. View Products")
                    print("2. Search Product")
                    print("3. Add Product")
                    print("4. Update Product")
                    print("5. Delete Product")
                    print("6. Increase Stock (Purchase)")
                    print("7. Decrease Stock (Sale)")
                    print("8. Low Stock Alert")
                    print("9. Supplier Management")
                    print("10. Inventory Valuation Report")
                    print("11. View History Logs")
                    print("12. Export Data to CSV")
                    print("13. Logout")
                    print("0. Exit Application")
                    print("==========================================")

                    choice = input("Enter choice: ").strip()
                    if choice == "1":
                        self.view_products()
                    elif choice == "2":
                        self.search_product()
                    elif choice == "3":
                        self.add_product()
                    elif choice == "4":
                        self.update_product()
                    elif choice == "5":
                        self.delete_product()
                    elif choice == "6":
                        self.increase_stock()
                    elif choice == "7":
                        self.decrease_stock()
                    elif choice == "8":
                        self.low_stock_alert()
                    elif choice == "9":
                        self.manage_suppliers()
                    elif choice == "10":
                        self.inventory_valuation_report()
                    elif choice == "11":
                        self.view_history()
                    elif choice == "12":
                        self.export_data()
                    elif choice == "13":
                        self.current_user = None
                        print("Logged out successfully.")
                    elif choice == "0":
                        sys.exit()
                    else:
                        print("Invalid choice.")

                elif self.current_user.role == "Staff":
                    print("\n=============== Staff Menu ===============")
                    print("1. View Products")
                    print("2. Search Product")
                    print("3. Increase Stock (Purchase)")
                    print("4. Decrease Stock (Sale)")
                    print("5. Low Stock Alert")
                    print("6. Logout")
                    print("0. Exit Application")
                    print("==========================================")

                    choice = input("Enter choice: ").strip()
                    if choice == "1":
                        self.view_products()
                    elif choice == "2":
                        self.search_product()
                    elif choice == "3":
                        self.increase_stock()
                    elif choice == "4":
                        self.decrease_stock()
                    elif choice == "5":
                        self.low_stock_alert()
                    elif choice == "6":
                        self.current_user = None
                        print("Logged out successfully.")
                    elif choice == "0":
                        sys.exit()
                    else:
                        print("Invalid choice.")