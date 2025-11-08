# Grocery Cart Checkout

# List of groceries with numbers, names : prices

groceries = {
    1:('Avocado': 1.50),
    2:('Banana': 0.75),
    3:('Carrot': 1.75),
    4:('Dates': 4.5),
    5:('Eggs': 5),
    6:('Fig': 4.99),
    7:('Grape': 3.75),
    8:('Honeydew': 5.50)
}

# Cart items: {item: quantity}

cart = {}

print(f'** Welcome to our Store! **')
print(f'Currently Avialable items:\n')
for item, price in groceries.items():
    print(f'{item.title()} - ${price:.2f}')

print("\nEnter the item you want to buy or enter 'checkout' to finish.\n")

while True:
    choice = input("Enter item name (or 'checkout'):").strip().lower

    if choice == 'Checkout':
       break
       
    if choice in groceries:
       try:
            quantity = int(input(f'Enter the amount of {choice}:'))
            if quantity > 0:
                cart[choice] = cart.get(choice, 0) + quantity
                print(f'addes {quantity} x {choice}(s) to cart')
            else:
                print(f'Quantity must be more than Zero') 
       except ValueError:
           print(f"Please enter valid number ")
                   


# Print a Receipt
# 
print(f'** Your Receipt **')
total = 0
for item, quantity in cart.items():
    price = groceries[item]
    subtotal = price * quantity
    print(f'{item.title()} (x{quantity}) - ${price:.2f} each = ${subtotal:.2f}')
    total += subtotal
print(f'\nTotal Amount : ${total:.2f}')
print(f'Thank you')    
            
               

