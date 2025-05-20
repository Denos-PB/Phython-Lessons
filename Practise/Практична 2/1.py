user_input = input("Будь ласка введіть список чисел, розідлених комами: ")
numbers_list = [int(item) for item in user_input.split(',')]
numbers_list.sort()
n = len(numbers_list)
if n % 2 == 1:
    median = numbers_list[int(n // 2)]
else:
    median = (numbers_list[n // 2 - 1] + numbers_list[n // 2]) / 2

print(f"Медіана {median}")
