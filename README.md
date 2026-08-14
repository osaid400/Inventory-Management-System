# Inventory Management System

A console-based **Inventory Management System** built with Python. This project demonstrates Object-Oriented Programming (OOP), CRUD operations, JSON-based file persistence, inventory tracking, input validation, and stock management in a menu-driven application.

---

## Features

- Add new products
- View all products in a formatted table
- Search products by:
  - Product ID
  - Product Name
  - Category
- Update product details
- Delete products
- Increase product stock
- Decrease product stock
- Low Stock Alert with customizable threshold
- Prevent duplicate Product IDs
- Validate user input
- Persistent storage using JSON file handling

---

## Technologies Used

- Python 3

---

## Concepts Covered

- Object-Oriented Programming (OOP)
- Classes & Objects
- Functions
- Lists
- Dictionaries
- Loops (`for`, `while`)
- Conditional Statements (`if`, `elif`, `else`)
- Exception Handling (`try`, `except`)
- CRUD Operations
- Data Validation
- Sorting
- List Comprehensions
- String Methods (`strip()`, `lower()`)
- JSON File Handling (`json.load()`, `json.dump()`)
- `os.path.exists()` for safe file loading

---

## Project Structure

```text
Inventory-Management-System/
│
├── Inventory Management System.py
├── .gitignore
└── README.md
```

> **Note:** `products.json` is automatically created when the program runs and stores inventory data locally. It is excluded from the repository via `.gitignore` because it contains runtime data rather than source code.

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/osaid400/Inventory-Management-System.git
```

### 2. Navigate to the project folder

```bash
cd Inventory-Management-System
```

### 3. Run the program

```bash
python "Inventory Management System.py"
```

---

## Example Output

### Main Menu

```text
============ Welcome to Inventory Management System ============

=============== Select Option (0-8) ===============
1. Add Product
2. View All Products
3. Search Product
4. Update Product
5. Delete Product
6. Increase Stock
7. Decrease Stock
8. Low Stock Alert
0. Exit
====================================================
```

### View Products

```text
===============================================================================================
Product ID      Name                     Category             Price                Stock
===============================================================================================
101             Keyboard                 Electronics          Rs. 2,500.00         15
102             Mouse                    Electronics          Rs. 1,200.00         25
103             Monitor                  Electronics          Rs. 28,500.00        8
===============================================================================================
```

### Search Product

```text
===============================================================================================
Search By:
1. Search by ID
2. Search by Name
3. Search by Category
===============================================================================================
```

### Low Stock Alert

```text
--- LOW STOCK ALERT (Items <= 5) ---
===============================================================================================
Product ID      Name                     Category             Price                Stock
===============================================================================================
120             Projector                Office               Rs. 47,000.00        3
111             Desk                     Furniture            Rs. 32,000.00        4
===============================================================================================
```

---

## How Data Persistence Works

- On startup, the program checks if `products.json` exists using `os.path.exists()`.
- If it exists, all products are loaded into memory using `json.load()`.
- If it doesn't exist, the program automatically creates a default inventory with sample products.
- Every time a product is added, updated, deleted, or its stock changes, the complete inventory is saved back to `products.json` using `json.dump()`.
- This ensures that all inventory data persists between program runs.

---

## Future Improvements

- Inventory value report
- Export inventory to CSV or Excel
- Sales and purchase history
- Supplier management
- Barcode support
- Product image support
- SQLite/MySQL database integration
- User authentication and roles
- Build a GUI version using Tkinter


---

## Learning Outcomes

This project helped me practice:

- Designing applications using Object-Oriented Programming (OOP)
- Building reusable classes and methods
- Performing CRUD operations
- Managing inventory records
- Implementing stock management features
- Searching records using multiple criteria
- Working with JSON file persistence
- Validating user input and handling exceptions
- Building structured menu-driven console applications
- Improving debugging and problem-solving skills

---

## Author

**Muhammad Abdullah Farooq**

GitHub: https://github.com/osaid400