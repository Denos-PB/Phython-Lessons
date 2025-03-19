def calculate_triangle_perimeter(side1, side2, side3):
  perimeter = side1 + side2 + side3
  return perimeter

side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

perimeter = calculate_triangle_perimeter(side1, side2, side3)
print("The perimeter of the tricut:", perimeter)