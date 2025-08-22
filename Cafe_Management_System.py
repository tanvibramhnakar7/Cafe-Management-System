# Cafe Management System (Console-Based)

menu = {
    "Coffee": 50,
    "Tea": 30,
    "Sandwich": 70,
    "Burger": 120,
    "Pastry": 90
}

order = {}

def show_menu():
    print("\n=== Welcome to Python Cafe ===")
    print("Available Menu:")
    for item, price in menu.items():
        print(f"{item}: ₹{price}")

def add_order():
    item = input("\nEnter item name: ").title()
    if item in menu:
        qty = int(input("Enter quantity: "))
        if item in order:
            order[item] += qty
        else:
            order[item] = qty
        print(f"✅ {qty} {item}(s) added to order.")
    else:
        print("⚠ Item not available!")

def view_order():
    if not order:
        print("\n🛒 No items in order yet!")
    else:
        print("\n=== Your Order ===")
        total = 0
        for item, qty in order.items():
            price = menu[item] * qty
            print(f"{item} x {qty} = ₹{price}")
            total += price
        print(f"💰 Total Bill: ₹{total}")

def remove_item():
    if not order:
        print("\n⚠ No items to remove.")
        return
    item = input("\nEnter item name to remove: ").title()
    if item in order:
        del order[item]
        print(f"❌ {item} removed from order.")
    else:
        print("⚠ Item not in order!")

while True:
    print("\n=== Cafe Management System ===")
    print("1. Show Menu")
    print("2. Add Item to Order")
    print("3. View Order & Bill")
    print("4. Remove Item from Order")
    print("5. Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        show_menu()
    elif choice == "2":
        add_order()
    elif choice == "3":
        view_order()
    elif choice == "4":
        remove_item()
    elif choice == "5":
        print("\n🙏 Thank you for visiting Python Cafe. Goodbye!")
        break
    else:
        print("⚠ Invalid choice! Try again.")
