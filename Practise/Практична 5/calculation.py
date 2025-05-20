def calculate_stock_value(products):
    total_value = 0
    for product, details in products.items():
        total_value += details['price'] * details['quantity']
    print(f"Total stock value for {products}: {total_value}")

def calculate_discount(products):
    for product_name, details in products.items():
        if details['quantity'] < 10:
            discount = details['price'] * 0.05
            print(f"Discount for {product_name}: {discount}")
        else:
            print(f"Discount for {product_name} not available because of quantity: {details['quantity']}")