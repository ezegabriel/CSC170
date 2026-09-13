'''
Gabriel Eze
CSC 170 - b
Lab 11 - for loops and indexing
Lab Partner - Iris
A word guessing game played between two players
Player 1 chooses a secret word
Player 2 has an infinite number of rounds to guess the letters in words
letter guessed correctly by player 2 are revealed on the console
while other letters are replaced with an underscore (_)
'''

# Ask player 1 to enter a secret word
word = input("Player 1, enter your word: ")
print()
l_word = list(word) # A list holding each character for mutation

# A blank
# This blanks conceals unguessed letters with underscores
# and replaces blanks with correctly guessed letters
l_console = list("_") * len(word) 
print("_" * len(word), "Letter to try:", end = " ")

# Ask Player 2 to guess one letter at a time
letter = input("")
# Variable to keep track of attempts
i_count = 0

# A loop to stop the program if player 2 gets the word
while l_console != l_word:
    # If player 2 guesses a letter correctly, go through every word
    for i_index in range(len(word)):
        # Replacing the blank(s) with the word(s)
        if l_word[i_index] == letter:
            l_console[i_index] = letter
    i_count += 1
    print()
    # Immediately after a guess, if the blank is filled up
    # stop the program; show the word; show the attempts
    if l_console == l_word:
        print(word)
        print()
        print("Well done, it took you", i_count, "rounds.")
    else:
        # Show the current blanks and ask for a letter guess
        print("".join(l_console), "Letter to try:", end = " ")
        letter = input("")
        



word = "hello word"
l_word = list(word)
for i_index in range(1, len(word) - 1):
    l_word[i_index] = "*"
print("".join(l_word))
