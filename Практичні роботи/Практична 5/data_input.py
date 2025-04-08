def input_product():
    products = {}
    while True:
        name = input("Enter product name (or 'stop' to finish): ").strip()
        if name.lower() == 'stop':
            break
        try:
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            products[name] = {'price': price, 'quantity': quantity}
        except ValueError:
            print("Invalid input. Please enter numeric values for price and quantity.")
    return products