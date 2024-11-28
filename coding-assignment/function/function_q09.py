9. Write a function to merge two sorted lists.
def merge_sorted_lists(a, b):
    return sorted(a + b)

print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  # Output: [1, 2, 3, 4, 5, 6]
