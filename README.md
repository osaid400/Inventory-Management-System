# Inventory Management System

A simple console-based **Inventory Management System** built with Python. This project demonstrates CRUD (Create, Read, Update, Delete) operations, JSON file handling, searching, input validation, and inventory management.

## Features

- Add new products
- View all products
- Search products
  - By Product ID
  - By Product Name
  - By Category
- Update product information
- Delete products
- Prevent duplicate Product IDs
- Validate user input
- Store data using JSON file handling

## Technologies Used

- Python 3
- JSON

## Concepts Covered

- Functions
- Lists
- Dictionaries
- Loops
- Conditional Statements
- JSON File Handling
- Exception Handling
- Data Validation
- CRUD Operations
- Sorting
- Helper Functions

## Project Structure

```text
Inventory-Management-System/
│
├── Inventory Management System.py
├── .gitignore
└── README.md
```

## Sample Output

### Main Menu

```text
=============== Select the Option (0-5) ===============
1. Add Product
2. View Products
3. Search Product
4. Update Product
5. Delete Product
0. Exit
```

### View Products

```text
==============================================================================================================
Product ID          Name                     Category                Price                        Stock
==============================================================================================================
101                 Keyboard                 Electronics             Rs. 2,500.0                  15
102                 Mouse                    Electronics             Rs. 1,200.0                  25
103                 Monitor                  Electronics             Rs. 28,500.0                 8
==============================================================================================================
```

### Search Product

```text
Search By:
1. Search by ID
2. Search by Name
3. Search by Category
```

### Add Product

```text
Enter the Product ID: 130
Enter the Product name: Webcam Stand
Enter the Category name: Accessories
Enter the Price: 2500
Enter the Stock: 12

New Product Added Successfully!
```

### Update Product

```text
Enter the Product ID: 130

Product Updated Successfully!
```

### Delete Product

```text
Enter the Product ID: 130
Are you sure you want to delete Product Webcam Stand? (y/n): y

Product Deleted Successfully!
```

## How to Run

1. Clone the repository

```bash
git clone https://github.com/osaid400/Inventory-Management-System.git
```

2. Navigate to the project folder

```bash
cd Inventory-Management-System
```

3. Run the program

```bash
python "Inventory Management System.py"
```

## Future Improvements

- Low stock alerts
- Total inventory value
- Sort products by price or stock
- Export inventory to CSV/Excel
- Supplier management
- Sales and purchase history
- Barcode support
- SQLite/MySQL database integration

## Learning Outcomes

This project helped me practice:

- Writing modular Python programs
- Managing inventory using dictionaries and lists
- Performing CRUD operations
- Searching and updating records
- Working with JSON file storage
- Validating user input
- Building menu-driven console applications

## Author

**Muhammad Abdullah Farooq**

GitHub: https://github.com/osaid400