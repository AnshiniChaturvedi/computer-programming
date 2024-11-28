15. Write a function to flatten a nested list.
def flatten_list(nested_list):
    flat_list = []
    for i in nested_list:
        if isinstance(i, list):
            flat_list.extend(flatten_list(i))
        else:
            flat_list.append(i)
    return flat_list

print(flatten_list([[1, 2], [3, [4, 5]]]))  # Output: [1, 2, 3, 4, 5]
