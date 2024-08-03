my_ratings = [2.5, 5.0]
other_ratings = [3.7, 4.5, 4.9]

all_ratings = my_ratings + other_ratings
print(all_ratings)

first_two_ratings = all_ratings[:2]
print(first_two_ratings)

middle_ratings = all_ratings[1:-1]
print(middle_ratings)

last_two_ratings = all_ratings[-2:]
print(last_two_ratings)

my_ratings.append(7.7)
print(my_ratings)

other_ratings.pop()
print(other_ratings)
