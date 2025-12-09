def unique_names(names1, names2):
    unique_set = set(names1) | set(names2)
    return list(unique_set)

result = unique_names(['Ava', 'Emma', 'Olivia'], ['Olivia', 'Sophia', 'Emma'])
print(result)
0