18. Write a function to check if a list is sorted.
def is_sorted(lst):
    return lst == sorted(lst)

print(is_sorted([1, 2, 3]))  # Output: True
