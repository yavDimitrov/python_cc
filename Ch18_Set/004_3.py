my_set = {10, 2, 10, 5, 7}
other_set = {34, 1, 10, 5}

print(my_set.union(other_set))
print(other_set.union(my_set))
print(my_set.union(other_set) == other_set.union(my_set))
print(my_set | other_set)
