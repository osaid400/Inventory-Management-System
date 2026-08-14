# src/models.py

import hashlib
import json
import os

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

class User:
    def __init__(self, username, password_hash, role):
        self.username = str(username).strip()
        self.password_hash = str(password_hash).strip()
        self.role = str(role).strip().capitalize()

    def to_dict(self):
        return {
            "Username": self.username,
            "PasswordHash": self.password_hash,
            "Role": self.role
        }

    @classmethod
    def from_dict(cls, data):
        pwd_hash = data.get("PasswordHash")
        if not pwd_hash and "Password" in data:
            pwd_hash = hash_password(data["Password"])
        return cls(
            username=data["Username"],
            password_hash=pwd_hash,
            role=data["Role"]
        )

class Supplier:
    def __init__(self, supplier_id, name, phone, email):
        self.supplier_id = int(supplier_id)
        self.name = str(name).strip()
        self.phone = str(phone).strip()
        self.email = str(email).strip()

    def __str__(self):
        return f"{self.supplier_id:<15} {self.name:<25} {self.phone:<18} {self.email:<30}"

    def to_dict(self):
        return {
            "Supplier ID": self.supplier_id,
            "Name": self.name,
            "Phone": self.phone,
            "Email": self.email
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            supplier_id=data["Supplier ID"],
            name=data["Name"],
            phone=data["Phone"],
            email=data["Email"]
        )

class Product:
    def __init__(self, product_id, name, category, price, quantity, supplier_id):
        self.product_id = int(product_id)
        self.name = str(name).strip()
        self.category = str(category).strip().capitalize()
        self.price = float(price)
        self.quantity = int(quantity)
        self.supplier_id = int(supplier_id)

    def update(self, name=None, category=None, price=None, quantity=None, supplier_id=None):
        if name is not None and name.strip():
            self.name = name.strip()
        if category is not None and category.strip():
            self.category = category.strip().capitalize()
        if price is not None and price > 0:
            self.price = float(price)
        if quantity is not None and quantity >= 0:
            self.quantity = int(quantity)
        if supplier_id is not None:
            self.supplier_id = int(supplier_id)

    def to_dict(self):
        return {
            "Product ID": self.product_id,
            "Name": self.name,
            "Category": self.category,
            "Price": self.price,
            "Stock": self.quantity,
            "Supplier ID": self.supplier_id
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            product_id=data["Product ID"],
            name=data["Name"],
            category=data["Category"],
            price=data["Price"],
            quantity=data["Stock"],
            supplier_id=data.get("Supplier ID", 1)
        )

class HistoryLog:
    def __init__(self, timestamp, username, action_type, details):
        self.timestamp = str(timestamp)
        self.username = str(username)
        self.action_type = str(action_type)
        self.details = str(details)

    def to_dict(self):
        return {
            "Timestamp": self.timestamp,
            "Username": self.username,
            "Action Type": self.action_type,
            "Details": self.details
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            timestamp=data["Timestamp"],
            username=data["Username"],
            action_type=data["Action Type"],
            details=data["Details"]
        )