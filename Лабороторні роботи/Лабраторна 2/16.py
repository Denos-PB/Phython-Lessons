def format_date(day, month, year):
    # Days in each month (non-leap year)
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Validate year
    if year < 1:
        return "Incorrect year"

    # Validate month
    if month < 1 or month > 12:
        return "Incorrect month"

    # Account for leap year in February
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        days_in_month[1] = 29

    # Validate day
    if day < 1 or day > days_in_month[month - 1]:
        return "Incorrect day"

    # Format date with leading zeros
    return f"{day:02d}.{month:02d}.{year:04d}"


# Demonstration of function
print(format_date(15, 3, 2025))  # Valid date
print(format_date(29, 2, 2024))  # Leap year
print(format_date(29, 2, 2025))  # Invalid date
print(format_date(31, 4, 2025))  # Invalid day for April
print(format_date(0, 5, 2025))  # Invalid day
print(format_date(15, 13, 2025))  # Invalid month