# INVENTORY MANAGEMENT SYSTEM
# Author: Muhammad Abdullah Farooq
# Language: Python
# Level: Beginner

print ("============ Welcome to Inventory Management System =============")

products = [
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
    {"Product ID": 125, "Name": "Mechanical Keyboard", "Category": "Electronics", "Price": 8500.0, "Stock": 10}
]

def add_product():
    try:
        product_id = int(input("Enter the Product ID: "))
    except ValueError:
        print("Invalid Product ID! Please enter a number.")
        return
    if product_id <= 0:
        print("Enter a valid Product ID!")
        return

    for product in products:
        if product["Product ID"] == product_id:
            print("Product ID already exists!")
            return

    Name = input("Enter the Product name: ")
    Category = input("Enter the Category name: ")

    try:
        price = float(input("Enter the Price: "))
        if price <=0:
            print("Price must be a positive number!")
            return
    except ValueError:
        print("Invalid Price! Please enter a number.")
        return  
    
    try:
        stock = int(input("Enter the Stock: "))
        if stock < 0:
            print("Stock must be a positive number!")
            return
    except ValueError:
        print("Invalid Stock! Please enter a number.")
        return 

    Name = Name.strip()
    Category = Category.strip()

    if Name == "":
        print("Product Name cannot be empty!")
        return

    if Category == "":
        print("Category cannot be empty!")
        return

    new_product = {
        "Name": Name,
        "Category": Category,
        "Product ID": product_id,
        "Price": price,
        "Stock": stock
    }

    products.append(new_product)
    print("New Product Added Successfully!")

def view_products():
    if len(products) == 0:
        print("No Products in stocks!")
        return
    for product in products:
            print("---------------------------------------------------")
            print("Name:", product["Name"])
            print("Category:", product["Category"])
            print("Product ID:", product["Product ID"])
            print("Price:", product["Price"])
            print("Stock:", product["Stock"])
            print("---------------------------------------------------")

def search_product():
    try:
        search = int(input("Enter the Product ID: "))
    except ValueError:
        print("Invalid Product ID! Please enter a number.")
        return

    found = False
    for product in products:
        if product["Product ID"] == search:
            print("---------------------------------------------------")
            print("Name:", product["Name"])
            print("Category:", product["Category"])
            print("Product ID:", product["Product ID"])
            print("Price:", product["Price"])
            print("Stock:", product["Stock"])
            print("---------------------------------------------------")
            found = True
            break
    if not found:
        print("Product Not Found!")

def update_product():
    try:
        search = int(input("Enter the Product ID: "))
    except ValueError:
        print("Invalid Product ID! Please enter a number.")
        return

    found = False
    for product in products:
        if product["Product ID"] == search:
            print("---------------------------------------------------")
            print("Current Details:")
            print("Name:", product["Name"])
            print("Category:", product["Category"])
            print("Product ID:", product["Product ID"])
            print("Price:", product["Price"])
            print("Stock:", product["Stock"])
            print("---------------------------------------------------")

            Name = input("Enter the new Product name (leave blank to keep current): ")
            Category= input("Enter the new Category name (leave blank to keep current): ")
            price_input = input("Enter the new Price name (leave blank to keep current): ")
            stock_input = input("Enter the new Stock (leave blank to keep current): ")

            if Name.strip():
                product["Name"] = Name.strip()
            if Category.strip():
                product["Category"] = Category.strip()
            if price_input.strip():
                try:
                    price = float(price_input)
                    if price <= 0:
                        print("Price must be a positive number! Keeping current price.")
                    else:
                        product["Price"] = price
                except ValueError:
                    print("Invalid Price! Keeping current price.")
            if stock_input.strip():
                try:
                    stock = int(stock_input)
                    if stock < 0:
                        print("Stock must be a positive number! Keeping current stock.")
                    else:
                        product["Stock"] = stock
                except ValueError:
                    print("Invalid Stock! Keeping current stock.")            
            print("Product Updated Successfully!")
            found = True
            break
    if not found:
        print("Product Not Found!")

def delete_product():
    try:
        search = int(input("Enter the Product ID: "))
    except ValueError:
        print("Invalid Product ID! Please enter a number.")
        return

    found = False
    for product in products:
        if product["Product ID"] == search:
            confirm = input(f"Are you sure you want to delete Product {product['Name']}? (y/n): ")
            if confirm.lower() != "y":
                print("Deletion cancelled.")
                return
            products.remove(product)
            print("Product Deleted Successfully!")
            found = True
            break
    if not found:
        print("Product Not Found!")


def exit_system():
    print("---------------------------------------------------")
    print("Exiting the Inventory Management System.")
    print("Thank you for using the system. Goodbye!")
    print("---------------------------------------------------")
    import sys
    sys.exit()

while True:
    print()
    print("=============== Select the Option (0-5) ===============")
    print("1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Product")
    print("5. Delete Product")
    print("0. Exit")

    try:
        choice = int(input("Enter the number: "))
    except ValueError:
        print("Invalid Choice! Please enter a number.")
        continue
    except Exception as e:
        print(f"An error occurred: {e}")
        continue

    if choice == 1:
        add_product()
    elif choice == 2:
        view_products()
    elif choice == 3:
        search_product()
    elif choice == 4:
        update_product()
    elif choice == 5:
        delete_product()
    elif choice == 0:
        exit_system()
        break
    else:
        print("Invalid Choice! Choose between 0 to 5")

