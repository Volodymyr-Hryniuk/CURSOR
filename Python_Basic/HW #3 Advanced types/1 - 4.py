# 1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print("1.")
print(f"int_a = {int_a} \t\t\t\t\t\t  id: {id(int_a)} \n"
      f"str_b = {str_b} \t\t\t\t\t  id: {id(str_b)} \n" 
      f"set_c = {set_c} \t\t\t\t  id: {id(set_c)} \n"
      f"lst_d = {lst_d} \t\t\t\t  id: {id(lst_d)} \n"
      f"dict_e = {dict_e} id: {id(dict_e)}")

# 2. Append 4 and 5 to the lst_d and define the id one more time.

print("\n2.")
print(f"lst_d: {lst_d}\t\t- lst_d id: {id(lst_d)}")

lst_d.append(4)
lst_d.append(5)

print(f"lst_d: {lst_d}  - lst_d id: {id(lst_d)}")

# 3. Define the type of each object from step 1.

print("\n3.")
print(f"int_a = {int_a} \t\t\t\t\t\t  type: {type(int_a)} \n"
      f"str_b = {str_b} \t\t\t\t\t  type: {type(str_b)} \n" 
      f"set_c = {set_c} \t\t\t\t  type: {type(set_c)} \n"
      f"lst_d = {lst_d} \t\t  type: {type(lst_d)} \n"
      f"dict_e = {dict_e} type: {type(dict_e)}")

# 4. Check the type of the objects by using isinstance.

print("\n4.")
print(f"instance of int_a = {int_a} \t\t\t\t\t\t  is an integer? {isinstance(int_a, int)}")
print(f"instance of str_b = {str_b} \t\t\t\t\t  is an string?  {isinstance(str_b, str)}")
print(f"instance of set_c = {set_c} \t\t\t\t  is an set? \t {isinstance(set_c, set)}")
print(f"instance of lst_d = {lst_d} \t\t  is an list?\t {isinstance(lst_d, list)}")
print(f"instance of dict_e = {dict_e} is an dict?\t {isinstance(dict_e, dict)}")
