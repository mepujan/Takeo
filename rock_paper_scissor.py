import random

# list of game choices
data = ['rock', 'paper', 'scissor']

# taking input from the user
user_input = input("Input Rock / Paper / Scissor: ")

# converting user input to lowercase
user_input = user_input.lower()

# making computer choice to compare the data
computer_input = random.choice(data)

while user_input != 'rock' and user_input != 'paper' and user_input != 'scissor':
    print("Invalid User Input. Try again....")
    # taking input from the user
    user_input = input("Input Rock / Paper / Scissor: ")

    # converting user input to lowercase
user_input = user_input.lower()

# printing the user and computer choice

print('------------------------------------------------------------')
print("USER -> ", user_input)
print("Computer -> ", computer_input)
print('------------------------------------------------------------')


# using elif ladder to check the condition and printing the relevant result.
if user_input == 'rock' and computer_input == 'paper':
    print("Paper covers rock. Computer win...")

elif user_input == 'rock' and computer_input == 'scissor':
    print("Rock breaks scissor. You win...")

elif user_input == 'paper' and computer_input == 'scissor':
    print("Scissor cuts paper. Computer win...")
elif user_input == 'paper' and computer_input == 'rock':
    print("Paper covers rock. You win...")
elif user_input == 'scissor' and computer_input == 'rock':
    print("Rock breaks scissor. Computer win...")

elif user_input == 'scissor' and computer_input == 'paper':
    print("Scissor cuts paper. You win...")
else:
    print("Game Tie.")

print("Game Over.")
