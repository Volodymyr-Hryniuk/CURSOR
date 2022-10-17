# String formatting:

# Replace the placeholders with a value:
# "Anna has ___ apples and ___ peaches."

# 5. With .format and curly braces {}.

print("5.")
print("Anna has {} apples and {} peaches.".format(16, 8))

# 6. By passing index numbers into the curly braces.

print("\n6.")
print("Anna has {0} apples and {1} peaches.".format(10, 11))

# 7. By using keyword arguments into the curly braces.

print("\n7.")
print("Anna has {apples} apples and {peaches} peaches.".format(apples=5, peaches=7))

# 8. With indicators of field size (5 chars for the first and 3 for the second).

print("\n8.")
print("Anna has {0:1d} apples and {1:1d} peaches." .format(6, 8))

# 9. With f-strings and variables.

print("\n9.")
apples = 3
peaches = 7
print(f"Anna has {apples} apples and {peaches} peaches.")

# 10. With % operator

print("\n10.")
print("Anna has %s apples and %s peaches." % (apples, peaches))

# 11. With variable substitutions by name (hint: by using dict).

print("\n11.")
count_fruit = {'apple': 7, 'peach': 4}
print(f"Anna has {count_fruit['apple']} apples and {count_fruit['peach']} peaches.")
