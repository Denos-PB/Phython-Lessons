def print_product_name(product_names):
    for name in product_names:
        print(name)


def find_product(products, search_name):
    search_name = search_name.lower()
    matches = {name: details for name, details in products.items() if search_name in name.lower()}

    if matches:
        for name, details in matches.items():
            print(f"Product '{name}' - Price: {details['price']}, Quantity: {details['quantity']}")
    else:
        print(f"No products found matching '{search_name}'.")