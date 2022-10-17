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
print(num(5, 8), "\n")

# 19. Convert (8) to regular function.

# (8)
# foo = lambda x, y, z: z if y < x and x > z else y

print("19.")


def foo(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y


print(foo(14, 13, 15), "\n")

# 20. Sort lst_to_sort from min to max.

print("20.")
lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
print("Sort from min to max", sorted(lst_to_sort), "\n")

# 21. Sort lst_to_sort from max to min.

print("21.")
print("Sort from max to min", sorted(lst_to_sort, reverse=True), "\n")

# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2.

print("22.")
lst = list(map(lambda x: x * 2, lst_to_sort))
print(lst, "\n")

# 23. Raise each list number to the corresponding number on another list:

print("23.")
list_A = [2, 3, 4]
list_B = [5, 6, 7]

# Raising to a power:
# lst_pow = list(map(pow, list_B, list_A))
# print(lst_pow, "\n")

# Raise each list number to the corresponding number on another list:
lst_2 = list(map(lambda x, y: x * 0 + y, list_A, list_B))
print(lst_2, "\n")

# Second variant:
# lst_2 = list(map(lambda x: x + 3, list_A))
# print(lst_2, "\n")

# 24. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.

print("24.")
lst_3 = list(filter(lambda x: (x % 2 == 1), lst_to_sort))
print(lst_3, "\n")

# 25. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.

print("25.")
b = range(-10, 10)
values = list(filter(lambda x: x < 0, b))
print(values, "\n")

# 26. Using the filter function, find the values that are common to the two lists:

print("26.")
list_1 = [1, 2, 3, 5, 7, 9]
list_2 = [2, 3, 5, 6, 7, 8]

filtered = list(filter(lambda x: x in list_1, list_2))
print(filtered)
