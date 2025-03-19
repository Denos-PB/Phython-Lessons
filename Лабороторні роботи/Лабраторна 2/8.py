import math

# Asking the user for the number of characters after the period
digits = int(input("Enter the number of characters after the period: "))

# a) The value of sqrt(2) in a fixed-point format
sqrt_2 = math.sqrt(2)
print(f"a) {sqrt_2:.{digits}f}")

# б) Value of (2.5)**1.6 in normalized format
value = 2.5**1.6
print(f"б) {value:.{digits}e}")

# в) The sum of pi and e in fixed-point format
pi_e_sum = math.pi + math.e
print(f"в) {pi_e_sum:.{digits}f}")