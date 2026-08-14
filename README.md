# Inventory Management System

A console-based Inventory Management System built with Python using Object-Oriented Programming (OOP) principles. It goes beyond basic stock CRUD with role-based access (Admin/Staff), supplier tracking, a full action history log, inventory valuation reporting, and CSV export — all backed by JSON persistence and a modular package structure.

---

## Features

* **Role-Based Access:**
  * Admin Login (full access, unlimited retry)
  * Staff Login (restricted access, 3-attempt lockout)

* **Admin-Only Operations:**
  * Add / Update / Delete Product (with auto-assigned Product ID)
  * Supplier Management (View / Add Suppliers, linked to products)
  * Inventory Valuation Report (auto-saved as `.txt` to `Reports/`)
  * View History Logs (every action, timestamped, tied to the user who did it)
  * Export Data to CSV (Inventory or History Log)

* **Shared (Admin + Staff) Operations:**
  * View All Products
  * Search Product (by Name or Category)
  * Increase Stock (Purchase)
  * Decrease Stock (Sale, with insufficient-stock protection)
  * Low Stock Alert (custom threshold)

* **Data & Security Features:**
  * SHA-256 Password Hashing for user accounts
  * Persistent JSON Storage for Products, Suppliers, Users, and History
  * Full action audit trail — every add/update/delete/stock-change/supplier-add is logged with timestamp, username, and details
  * Input validation and exception handling throughout

---

## Technologies Used

* **Python 3** (Object-Oriented Programming)
* **JSON Module** (Data persistence)
* **CSV Module** (Data export)
* **hashlib** (SHA-256 password hashing)
* **Datetime Module** (Timestamps for history logs and reports)
* **OS Module** (Directory and file handling)

---

## Project Structure

```text
Inventory-Management-System/
│
├── data/
│   ├── products.json          # Persistent product records (gitignored)
│   ├── Suppliers.json         # Persistent supplier records (gitignored)
│   ├── Users.json             # Persistent user accounts (gitignored)
│   └── history.json           # Persistent action history log (gitignored)
│
├── Reports/                    # Auto-generated valuation reports and CSV exports (gitignored)
│
├── src/                        # Source code package
│   ├── __init__.py
│   ├── models.py                 # User, Supplier, Product, HistoryLog classes + password hashing
│   ├── manager.py                  # DatabaseManager class — all JSON load/save logic
│   └── UI.py                       # InventorySystem class — login, menus, role-based access, reporting
│
├── .gitignore                  # Excludes __pycache__, Reports, and local data
├── main.py                     # Application entry point
└── README.md
```

> **Note:** `data/*.json` files are created automatically on first run, seeded with default products, suppliers, and two default user accounts (`admin` / `admin123` and `staff` / `staff123`). They are excluded from the repository via `.gitignore`.

---

## How to Run

Clone the repository

```bash
git clone https://github.com/osaid400/Inventory-Management-System.git
```

Move into the project folder

```bash
cd Inventory-Management-System
```

Run the program

```bash
python main.py
```

---

## Example Outputs

### Login

```text
================== Inventory Management System ==================
========================= User Login ===========================
1. Admin
2. User
Select Role (1-2): 1
Enter Password: admin123
Login Successful! Welcome, admin (Admin)
```

### Admin Menu

```text
=============== Admin Menu ===============
1. View Products
2. Search Product
3. Add Product
4. Update Product
5. Delete Product
6. Increase Stock (Purchase)
7. Decrease Stock (Sale)
8. Low Stock Alert
9. Supplier Management
10. Inventory Valuation Report
11. View History Logs
12. Export Data to CSV
13. Logout
0. Exit Application
==========================================
```

### Staff Menu (Restricted)

```text
=============== Staff Menu ===============
1. View Products
2. Search Product
3. Increase Stock (Purchase)
4. Decrease Stock (Sale)
5. Low Stock Alert
6. Logout
0. Exit Application
==========================================
```

### Staff Login with Wrong Password (Lockout)

```text
Enter Password (3 attempts left): wrongpass
Invalid password!
Enter Password (2 attempts left): wrongpass
Invalid password!
Enter Password (1 attempts left): wrongpass
Invalid password!
Maximum login attempts exceeded. Access locked.
```

### View Products

```text
====================================================================================================
ID         Name                   Category           Price              Stock      Supplier ID
====================================================================================================
101        Keyboard               Electronics        Rs. 2,500.00       15             1
102        Mouse                  Electronics        Rs. 1,200.00       25             1
103        Monitor                Electronics        Rs. 28,500.00      8              1
104        Laptop                 Electronics        Rs. 125,000.00     5              1
====================================================================================================
```

### Add Product (Admin Only)

```text
Enter Product Name: Wireless Earbuds
Enter Category: Electronics
Enter Price: 6500
Enter Initial Stock Quantity: 20

======================================================================================
Supplier ID    Name                      Phone              Email
======================================================================================
1              Global Tech Supplies      0300-1234567       contact@globaltech.com
2              Global Tech Supplies      0300-1234567       contact@globaltech.com
======================================================================================
Enter Supplier ID: 1

Product added successfully with ID 126.
```

### Search Product

```text
Enter search keyword (Name or Category): electronics

====================================================================================================
ID         Name                   Category           Price              Stock      Supplier ID
====================================================================================================
101        Keyboard               Electronics        Rs. 2,500.00       15         1
102        Mouse                  Electronics        Rs. 1,200.00       25         1
112        Headphones             Electronics        Rs. 6,500.00       18         1
====================================================================================================
```

### Increase / Decrease Stock

```text
Enter Product ID: 103
Enter quantity to add (Purchase): 10
Stock increased. New quantity: 18

Enter Product ID: 104
Enter quantity to sell (Sale): 2
Stock decreased. Remaining quantity: 3
```

### Low Stock Alert

```text
Enter threshold limit (default 5): 5
--- LOW STOCK ALERT (Stock <= 5) ---
====================================================================================================
ID         Name                   Category           Price              Stock      Supplier ID
====================================================================================================
104        Laptop                 Electronics        Rs. 125,000.00     3             1
111        Desk                   Furniture          Rs. 32,000.00      4             1
120        Projector              Office             Rs. 47,000.00      3             1
====================================================================================================
```

### Staff Trying an Admin-Only Action

```text
Enter choice: 3
Access Denied! Admins only.
```

### Supplier Management

```text
================= Supplier Management ==============
1. View Suppliers
2. Add Supplier
0. Back to Main Menu
Enter choice: 2
Enter Supplier Name: Prime Electronics Wholesale
Enter Phone Number: 0321-9876543
Enter Email Address: sales@primeelectronics.com
Supplier added successfully.
```

### Inventory Valuation Report

```text
==========================================================================================
Product Name              Category             Price           Stock      Total Value
==========================================================================================
Keyboard                  Electronics          Rs. 2,500.00     15         Rs. 37,500.00
Mouse                     Electronics          Rs. 1,200.00     25         Rs. 30,000.00
Monitor                   Electronics          Rs. 28,500.00    8          Rs. 228,000.00
Laptop                    Electronics          Rs. 125,000.00   3          Rs. 375,000.00
==========================================================================================
Total Inventory Valuation: Rs. 670,500.00
==========================================================================================
Report automatically saved to Reports/inventory_valuation_20260813_143022.txt
```

### View History Logs

```text
==============================================================================================================
Timestamp            Username        Action Type                        Details
==============================================================================================================
2026-08-13 14:20:11   admin           ADD_PRODUCT          Added product Wireless Earbuds with ID 126
2026-08-13 14:22:05   admin           PURCHASE_STOCK       Added 10 units to product ID 103
2026-08-13 14:23:40   staff           SALE_STOCK           Sold 2 units of product ID 104
2026-08-13 14:25:17   admin           ADD_SUPPLIER         Added supplier Prime Electronics Wholesale
==============================================================================================================
```

### Export Data to CSV

```text
1. Export Inventory to CSV
2. Export History Log to CSV
Enter choice: 1
Inventory successfully exported to Reports/inventory_export.csv
```

---

## Concepts Covered

* **Object-Oriented Programming (OOP):** Class design across four models (`User`, `Supplier`, `Product`, `HistoryLog`), each with `to_dict()` / `from_dict()` serialization.
* **CRUD Operations:** Full product lifecycle (add, search, update, delete), plus supplier creation.
* **JSON Data Serialization:** Four separate persistent JSON stores (products, suppliers, users, history), each managed through a single `DatabaseManager`.
* **Security:** SHA-256 password hashing for user accounts, with role-based access control enforced on every admin-only method.
* **Audit Logging:** Every meaningful action (add/update/delete a product, stock changes, adding a supplier) is recorded in a persistent, timestamped history log tied to the acting user.
* **Business Reporting:** An inventory valuation report (`price × stock`, summed across all products) generated and auto-saved to disk, plus CSV export for both inventory and history.
* **Modules & Packages:** Code organized into a `src/` package (`models.py`, `manager.py`, `UI.py`), separating data, persistence, and presentation/business logic, with `main.py` as the entry point outside the package.
* **Defensive Programming:** Input validation and exception handling across all menus and role checks.

---

## How Role-Based Access Works

* Two roles exist: **Admin** (full access) and **Staff** (day-to-day stock operations only).
* Admin-only actions (adding/editing/deleting products, supplier management, reports, history, CSV export) each check `self.current_user.role != "Admin"` and refuse with `"Access Denied! Admins only."` if a Staff user attempts them.
* Every action taken while logged in is attributed to `self.current_user.username` in the history log — so the audit trail always shows who did what.

## How the History Log & Reporting Work

* `log_action()` is called after every meaningful change, recording a timestamp, the acting username, an action type (e.g. `ADD_PRODUCT`, `SALE_STOCK`), and a short description.
* The Inventory Valuation Report sums `price × stock` across every product for a single "how much is currently in stock worth" figure, and is both printed to the console and saved as a timestamped `.txt` file in `Reports/`.
* Both the inventory and the history log can be exported to `.csv` independently, for use outside the app (e.g. in Excel).

---

## Future Improvements

* Add a 3-attempt lockout to Admin login as well (currently only Staff login has one)
* Move default admin/staff credentials out of source code
* Supplier editing and deletion (currently suppliers can only be viewed and added)
* Low stock alerts tied to per-supplier reorder suggestions
* SQLite integration replacing JSON persistence
* Graphical User Interface (Tkinter)

---

## Learning Outcomes

This project helped me practice and solidify key software engineering concepts:

* **Multi-model persistence:** Managing four related but independent JSON stores (products, suppliers, users, history) through one `DatabaseManager`.
* **Role-based access control:** Enforcing Admin-only permissions consistently across every sensitive method, rather than just hiding menu options.
* **Audit trail design:** Building a history log that ties every action back to a specific user and timestamp — a pattern directly useful for real inventory/POS systems.
* **Business reporting:** Calculating and formatting a real business metric (total inventory valuation) and exporting data in multiple formats (`.txt` reports, `.csv` exports).
* **Modular project structure:** Splitting a growing single-file project into a `models` / `manager` / `UI` / `main` package as its feature set expanded well beyond simple CRUD.

---

## Author

**Muhammad Abdullah Farooq**

GitHub: [https://github.com/osaid400](https://github.com/osaid400)