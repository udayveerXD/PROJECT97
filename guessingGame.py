

import random

print("Number guessing game")

# radiant function to generate the random number between 1 to 9
number = random.randint(1, 9)

# number of chances to be given to the user to guess the number
# or it is inputs given by user into input box here number of chances are 5
chances = 0

print("Guess a number(Between 1 and 9):")

# While loop to count the number of chances
while chances < 5:

    # enter a number between 1 to 9
    guess = int(input("enter your guess:- "))

    # compare the user entered number with the number to be gussed

    if guess == number:
        # if number entered by user is the same as generated
        # number by randint function then break from loop using loop
        # control statement "break"
        print("Congratulations YOU WON!!!")
        break

    # check if the user entered number is smaller than the generated number
    elif guess < number:
        print("Your guess was too low: guess a higher number than", guess)

    # the user entered number is greater than the generated number
    else:
        print("Your guess was too high: guess a lower number than", guess)
    
    # increase value of chance by 1
    chances += 1


#check weather or not the user guessed the correct number
if not chances < 5:
    print:("YOU LOOSE!! the number is", number)