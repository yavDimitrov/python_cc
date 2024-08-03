db_is_available = False
name = 'Bogdan'
db_is_available = True

if db_is_available and name:
    print("Is available!")

print(not db_is_available and name)

print(db_is_available and name)
