input_str = input("Please enter a number: ")
print(type(input_str))

try:
    input_num = int(input_str)
    print(type(input_num))

except ValueError:
    print("Not able to convert to int().")
