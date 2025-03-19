import math
def calculate_circle_circumference(radius):
    circumference = 2 * math.pi * radius
    return circumference
def calculate_circle_area(radius):
    area = math.pi * radius ** 2
    return area
# Input radius
while True:
    try:
        radius = float(input("Enter the radius of the circle (positive number): "))

        # Validate radius
        if radius <= 0:
            print("The radius must be a positive number. Try again.")
            continue

        # Calculate circumference and area
        circumference = calculate_circle_circumference(radius)
        area = calculate_circle_area(radius)

        # Display results
        print("\nResults:")
        print(f"Radius of a circle: {radius}")
        print(f"Length of the circle: {circumference:.2f}")
        print(f"Circle Square: {area:.2f}")

        break
    except ValueError:
        print("Incorrect input. Enter a number.")