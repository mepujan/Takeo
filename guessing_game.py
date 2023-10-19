from game_data import data
from random import choices

#  1. Generate two random option from the game data.
generated_options = choices(data, k=2)

for option in generated_options:
    print(option)


user_guess = input("Can you guess which of them has highest followers: ")

for option in generated_options:
    if option['name'] == user_guess:
        print(option['follower_count'])
