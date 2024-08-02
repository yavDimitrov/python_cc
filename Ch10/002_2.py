long_str = "This is a very long string!" \
           "We can escape symbols with \""

long_str2 = """This is a very
            long string!
            We can escape symbols with \""""

print(long_str)
print(type(long_str))
print(type(long_str) == str)
print(id(long_str))

print(long_str2)
print(type(long_str2))
print(type(long_str2) == str)
print(id(long_str2))
