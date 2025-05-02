import random

def find_median(lst):
    length = len(lst)
    if length == 0:
        return None
    if length % 2 == 0:
        mid_right = length // 2
        mid_left = mid_right - 1
        return [lst[mid_left], lst[mid_right]]
    else:
        mid = length // 2
        return [lst[mid - 1], lst[mid], lst[mid + 1]]

lst = [random.randint(1, 10) for _ in range(random.randint(1, 15))]
lst.sort()

print(f"Original list: {lst}")

length = len(lst)

if length % 2 == 0:
    print(f"List length is EVEN (size = {length})")
    median = find_median(lst)
    print(f"Median (two middle numbers): {median}")
else:
    print(f"List length is ODD (size = {length})")
    median = find_median(lst)
    print(f"Median (middle number): {median}")