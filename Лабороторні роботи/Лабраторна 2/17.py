import math
def demonstrate_special_values():
    # Create NaN (Not a Number)
    nan_value = float('nan')
    # Create Positive Infinity
    pos_infinity = float('inf')
    # Create Negative Infinity
    neg_infinity = float('-inf')
    # Demonstrate the values
    print("NaN (Not a Number):")
    print(f"Value: {nan_value}")
    print(f"Is NaN? {math.isnan(nan_value)}")

    print("\nPositive Infinity:")
    print(f"Value: {pos_infinity}")
    print(f"Is infinite? {math.isinf(pos_infinity)}")

    print("\nNegative Infinity:")
    print(f"Value: {neg_infinity}")
    print(f"Is infinite? {math.isinf(neg_infinity)}")
    # Some operations demonstrating these special values
    print("\nOperations with special values:")
    print(f"NaN == NaN: {nan_value == nan_value}")  # Always False
    print(f"NaN + 5: {nan_value + 5}")
    print(f"Infinity + Infinity: {pos_infinity + pos_infinity}")
    print(f"Infinity - Infinity: {pos_infinity - pos_infinity}")
# Run the demonstration
demonstrate_special_values()