'''
Gabrel Eze
Lab05
CSC 170-b
Part 1 , 2 , 3 & Challenge Problem 1

'''


''' Part 1 - Average '''

# Creat variables to store the sum and freq of numbers.
i_count = 0
i_total = 0

# Ask the user to enter any number.
i_number = int(input("Please enter a number: "))

# When the user enter a negative integer,
# Find the average of all the previous numbers. 
while i_number > 0:
    i_count = i_count + 1
    i_total = i_total + i_number
    i_number = int(input("Please enter a number: "))
average = i_total / i_count
print("The average of the postive integers is", str(average), "\n")


''' Part 2 - Guessing Game '''

# Ask Python to import a random number.
import random

i_rand = random.randint(1,10)
print(i_rand)
print("I'm thinking of a number between 1 and 10. You have 3 guesses")

# Create a variable that makes the program stop after 3 trials.
i_count = 0
i_number = int(input("Guess a number between 1 and 10: "))

# Compute the program for the game.
while i_number != i_rand  and i_count < 2:
    i_count = i_count + 1
    if i_number > i_rand :
        print("Your number is higher than the guess")
        i_number = int(input("Guess a number between 1 and 10: "))
    elif i_number < i_rand :
        print("Your number is lower than the guess")
        i_number = int(input("Guess a number between 1 and 10: "))
if i_count == 2 and i_number != i_rand:
    print("Sorry, you didn't guess the number. The number was", i_rand)

# If the user guesses correctly,
# Award an accolade and end the game.
if i_number == i_rand:
    print("You win! You guessed correctly.", "\n")


''' Part 3 - Printing a Triangle '''

# Create the variable that makes the outline.
s_star = "*"

# Ask the user to enter the height of the triangle.
i_height = int(input("Please enter height of triangle: "))
i_count = 0

# Compute the code for a right angled triangle.
while i_count < i_height:
    i_count += 1
    print(s_star * i_count)
print("Here lies your triangle!", "\n")

