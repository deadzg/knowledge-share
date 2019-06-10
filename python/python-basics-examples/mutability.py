#!/bin/python3


my_list = [1,2,3]
print (id(my_list))

my_list.append(4)
print(id(my_list)) # The address remains same

my_list_1 = [1,2,3]
print(id(my_list_1)) # This has different address then my_list as python creates a different object in memory

my_list_1 = my_list_1 + [4]
print(id(my_list)) # This is not same as append, as python evaluates the expression on right hand side and create a different object altogether

my_dict = dict(key1 =4, key =5)
print (my_dict)
print(id(my_dict))

my_dict['key3'] = 34.56
print(id(my_dict)) # Memory address remains same



# t is immutable. Also the internal state reffered by t is immutable because all of them are integers
t = (1,2,3)

a = [1,2,3]
b = [5, 2, 45]

# t is immutable, but the elements it's comprised of are mutable, thus the state of t can be changed
t = (a, b)
print (t)

a.append(56)
print ('Tuple got changed')
print (t)
