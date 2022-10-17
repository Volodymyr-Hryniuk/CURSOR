# Lambda:

# 18. Convert (7) to lambda function.

# (7)
# def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y

print("18.")
num = (lambda x, y: x if x < y else y)
print(num(5, 8))

# 19. Convert (8) to regular function.

# (8)
# foo = lambda x, y, z: z if y < x and x > z else y

print("\n19.")


def foo(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y


print(foo(14, 13, 15))

# 20. Sort lst_to_sort from min to max.

print("\n20.")
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print("List to sort:", lst_to_sort)
print("Sort from min to max", sorted(lst_to_sort))

# 21. Sort lst_to_sort from max to min.

print("\n21.")
print("List to sort:", lst_to_sort)
print("Sort from max to min", sorted(lst_to_sort, reverse=True))

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2.

print("\n22.")
lst = list(map(lambda x: x * 2, lst_to_sort))
print(lst)

# 23. Raise each list number to the corresponding number on another list:

print("\n23.")
list_A = [2, 3, 4]
list_B = [5, 6, 7]

# Raising to a power:
lst_pow = list(map(pow, list_B, list_A))
print("The first variant 'Raising to a power'", lst_pow)

# Raising list number to the corresponding number on another list:
lst_2 = list(map(lambda x: x + 3, list_A))
print("The second variant 'Raising list number to the corresponding number on another list'", lst_2)

# The third variant:
# lst_3 = list(map(lambda x, y: x * 0 + y, list_A, list_B))
# print("The third variant", lst_3)

# 24. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.

print("\n24.")
lst_4 = list(filter(lambda x: x % 2 == 1, lst_to_sort))
print(lst_4)

# 25. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.

print("\n25.")
b = range(-10, 10)
values = list(filter(lambda x: x < 0, b))
print(values)

# 26. Using the filter function, find the values that are common to the two lists:

print("\n26.")
list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]

filtered = list(filter(lambda x: x in list_1, list_2))
print(filtered)
