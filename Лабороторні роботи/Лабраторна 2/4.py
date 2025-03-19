def get_point_coordinates():
  x = float(input("Enter coordinates x: "))
  y = float(input("Enter coordinates y: "))
  return x, y

def print_point(x, y):

  print(f"Coordinates: ({x}, {y})")

# Example of use
x, y = get_point_coordinates()
print_point(x, y)