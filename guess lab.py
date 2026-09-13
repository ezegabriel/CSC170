'''
Gabriel Eze
CSC170
'''
import random

i_rand = random.randint(1,10)
print(i_rand )
print("I'm thinking of a number between 1 and 10. You have 3 guesses")

i_count = 0
i_number = int(input("Guess a number between 1 and 10: "))
while i_number != i_rand  and i_count < 2:
    i_count = i_count + 1
    if i_number > i_rand :
        print("Your number is higher than the guess")
        i_number = int(input("Guess a number between 1 and 10: "))
    elif i_number < i_rand :
        print("Your number is lower than the guess")
        i_number = int(input("Guess a number between 1 and 10: "))
if i_number == i_rand:
    print("You win! You guessed correctly.")
