# src/manager.py

import json
import os
from src.models import User, Supplier, Product, HistoryLog, hash_password

class DatabaseManager:
    def __init__(self):
        os.makedirs("data", exist_ok=True)
        os.makedirs("Reports", exist_ok=True)
        self.suppliers_file = os.path.join("data", "Suppliers.json")
        self.products_file = os.path.join("data", "products.json")
        self.users_file = os.path.join("data", "Users.json")
        self.history_file = os.path.join("data", "history.json")

    def load_users(self):
        if os.path.exists(self.users_file):
            try:
                with open(self.users_file, "r") as f:
                    return [User.from_dict(i) for i in json.load(f)]
            except:
                pass
        default_users = [
            User("admin", hash_password("admin123"), "Admin"),
            User("staff", hash_password("staff123"), "Staff")
        ]
        self.save_users(default_users)
        return default_users

    def save_users(self, users):
        with open(self.users_file, "w") as f:
            json.dump([u.to_dict() for u in users], f, indent=4)

    def load_suppliers(self):
        if os.path.exists(self.suppliers_file):
            try:
                with open(self.suppliers_file, "r") as f:
                    return [Supplier.from_dict(i) for i in json.load(f)]
            except:
                return []
        else:
            suppliers = [
                Supplier(1, "Global Tech Supplies", "0300-1234567", "contact@globaltech.com"),
                Supplier(2, "Global Tech Supplies", "0300-1234567", "contact@globaltech.com"),
                Supplier(3, "Global Tech Supplies", "0300-1234567", "contact@globaltech.com"),


                ]
            self.save_suppliers(suppliers)
            return suppliers

    def save_suppliers(self, suppliers):
        with open(self.suppliers_file, "w") as f:
            json.dump([s.to_dict() for s in suppliers], f, indent=4)

    def load_products(self):
        if os.path.exists(self.products_file):
            try:
                with open(self.products_file, "r") as f:
                    return [Product.from_dict(i) for i in json.load(f)]
            except:
                return []
        else:
            initial_data = [
                {"Product ID": 101, "Name": "Keyboard", "Category": "Electronics", "Price": 2500.0, "Stock": 15, "Supplier ID": 1},
                {"Product ID": 102, "Name": "Mouse", "Category": "Electronics", "Price": 1200.0, "Stock": 25, "Supplier ID": 1}
            ]
            products = [Product.from_dict(i) for i in initial_data]
            self.save_products(products)
            return products

    def save_products(self, products):
        with open(self.products_file, "w") as f:
            json.dump([p.to_dict() for p in products], f, indent=4)

    def load_history(self):
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, "r") as f:
                    return [HistoryLog.from_dict(i) for i in json.load(f)]
            except:
                return []
        return []

    def save_history(self, history):
        with open(self.history_file, "w") as f:
            json.dump([h.to_dict() for h in history], f, indent=4)