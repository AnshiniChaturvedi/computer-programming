19. Flatten a nested list
Question: Flatten the nested list [[1, 2], [3, 4], [5]].
nested_lst = [[1, 2], [3, 4], [5]]
flattened_lst = [item for sublist in nested_lst for item in sublist]
print(flattened_lst) 