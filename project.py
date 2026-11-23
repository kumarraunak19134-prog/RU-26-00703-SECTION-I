# ==========================================
#       SHOPPING CART SYSTEM
# ==========================================

# Product Catalogue
products = {
    "Pen": 10,
    "Notebook": 50,
    "Bag": 500
}

# Shopping Cart
cart = {}


# Function to Display Products
def view_products():
    print("\n------ AVAILABLE PRODUCTS ------")
    for product, price in products.items():
        print(f"{product} : Rs.{price}")


# Function to Add Items to Cart
def add_to_cart():
    product = input("Enter product name: ").strip().title()

    if product not in products:
        print("Invalid product. Available: Pen, Notebook, Bag")
        return

    try:
        quantity = int(input("Enter quantity: "))

        if quantity < 1:
            print("Quantity must be at least 1.")
            return

        cart[product] = cart.get(product, 0) + quantity

        subtotal = sum(
            products[item] * qty
            for item, qty in cart.items()
        )

        print(f"{product} x{quantity} added | Cart subtotal: {subtotal}")

    except ValueError:
        print("Invalid quantity. Please enter a number.")


# Function to Remove Items from Cart
def remove_from_cart():
    product = input("Enter product name to remove: ").strip().title()

    if product in cart:
        del cart[product]

        print(f"{product} removed.")

        if cart:
            print("Cart:")
            view_cart()
        else:
            print("Cart is empty.")
    else:
        print("Product not found in cart.")


# Function to View Cart
def view_cart():
    print("\n--------- YOUR CART ---------")

    if not cart:
        print("Cart is empty.")
        return

    for product, quantity in cart.items():
        amount = products[product] * quantity
        print(f"{product} x{quantity} = Rs.{amount}")


# Function to Calculate and Generate Bill
def checkout():
    if not cart:
        print("\nCart is empty. Add products first.")
        return

    subtotal = sum(
        products[item] * qty
        for item, qty in cart.items()
    )

    # 10% Discount if subtotal is greater than 500
    if subtotal > 500:
        discount = subtotal * 0.10
    else:
        discount = 0

    # GST is calculated after discount
    taxable_amount = subtotal - discount
    gst = taxable_amount * 0.18

    grand_total = taxable_amount + gst

    print("\n========== FINAL BILL ==========")

    for product, quantity in cart.items():
        amount = products[product] * quantity
        print(f"{product} x{quantity} = Rs.{amount}")

    print("--------------------------------")
    print(f"Subtotal: Rs.{subtotal:.2f}")
    print(f"Discount: Rs.{discount:.2f}")
    print(f"GST (18%): Rs.{gst:.2f}")
    print("--------------------------------")
    print(f"Grand Total: Rs.{grand_total:.2f}")
    print("================================")


# Main Function
def main():
    while True:
        print("\n====== SHOPPING CART SYSTEM ======")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. Remove from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            view_products()

        elif choice == "2":
            add_to_cart()

        elif choice == "3":
            remove_from_cart()

        elif choice == "4":
            view_cart()

        elif choice == "5":
            checkout()

        elif choice == "6":
            print("Thank you for shopping!")
            break

        else:
            print("Invalid choice. Please try again.")


# Program Execution
if __name__ == "__main__":
    main()