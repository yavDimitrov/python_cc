my_list = [10, 'abc', True]
copy_list = my_list[:]

copy_list.insert(2, 100)
print(my_list)
print(copy_list)
print(id(my_list) == id(copy_list))
print(id(my_list))
print(id(copy_list))
