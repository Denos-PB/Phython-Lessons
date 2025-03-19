def input_3d_point():
    x = float(input("Enter x coordinate: "))
    y = float(input("Enter y coordinate: "))
    z = float(input("Enter z coordinate: "))
    return x, y, z


def output_3d_point(x, y, z):
    print(f"Point Coordinates:")
    print(f"X: {x:10.2f}")
    print(f"Y: {y:10.2f}")
    print(f"Z: {z:10.2f}")


def main():
    print("3D Point Coordinate Input")
    print("-" * 30)

    # Input point coordinates
    point_x, point_y, point_z = input_3d_point()

    # Output point coordinates
    print("\nCoordinate Details:")
    output_3d_point(point_x, point_y, point_z)


# Run the main program
if __name__ == "__main__":
    main()