print(0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 + 0.1 - 1.0)

print(0.1 + 0.1 + 0.1 + 0.1 + 0.1 - 0.5)

import decimal

# Встановлюємо високу точність
decimal.getcontext().prec = 28

# Перший вираз з модулем decimal
print(sum(decimal.Decimal('0.1') for _ in range(10)) - decimal.Decimal('1.0'))

# Другий вираз з модулем decimal
print(sum(decimal.Decimal('0.1') for _ in range(5)) - decimal.Decimal('0.5'))