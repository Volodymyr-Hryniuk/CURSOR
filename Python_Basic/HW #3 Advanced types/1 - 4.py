#1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print("#1.")
print("int_a id:", id(int_a),"\n" "str_b id:", id(str_b),
      "\n" "set_c id:", id(set_c),"\n" "lst_d id:", id(lst_d),
      "\n" "dict_e id:", id(dict_e), "\n")

#2. Append 4 and 5 to the lst_d and define the id one more time.

print("#2.")
print("lst_d:", lst_d, "- lst_d id:",id(lst_d))

lst_d.append(4)
lst_d.append(5)

print("lst_d:", lst_d, "- lst_d id:",id(lst_d), "\n")

#3. Define the type of each object from step 1.

print("#3.")
print("int_a type:", type(int_a),"\n" "str_b type:", type(str_b),
      "\n" "set_c type:", type(set_c),"\n" "lst_d type:", type(lst_d),
      "\n" "dict_e type:", type(dict_e), "\n")

#4. Check the type of the objects by using isinstance.

print("#4.")
print("instance of int_a is an integer?",isinstance(int_a, int))
print("instance of str_b is an string?",isinstance(str_b, str))
print("instance of set_c is an set?",isinstance(set_c, set))
print("instance of lst_d is an list?",isinstance(lst_d, list))
print("instance of dict_e is an dict?",isinstance(dict_e, dict))