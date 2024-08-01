print(id(print))

my_name = 'Yavor'
print(id(my_name))

my_num = 666
print(id(my_num))

other_num = my_num
print(id(other_num))

print(id(my_num) == id(other_num))

my_num = 'Yavor'

print(id(my_num) == id(my_name))
print(id(my_num))
