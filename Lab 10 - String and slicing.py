'''
Gabriel Eze
CSC 170-b
Lab10
A program to mutate all middle characters
of non-palindromic to asteriks (*)
Lab partner - Pranjal

'''

# Ask the user to enter a phrase
s_phrase = input("Please enter a phrase: ")
s_slice = s_phrase[: : -1] # Reverse every character
l_list = [1, 2, 3]
l_list = l_list[: : -1]
print(l_list)

s_temp_hold = "" # A temporary variable to compare palindromic strings
# Ignore the spaces and concatenate all characters
for s_char in s_phrase:
    if s_char != " ":
        s_temp_hold += s_char

# Palindromic strings
s_reversed = ""
for i_index in range(len(s_temp_hold) - 1, -1, -1):
    s_reversed += s_temp_hold[i_index]
if s_reversed == s_temp_hold:
    print(s_phrase)
    print('"', s_phrase, '"', " is a palindrome", sep = "")

# Non - palindromic strings
else:
    print(s_slice)
    l_word_list = [] # List holding each word
    s_word_hold = "" # String holding each word before concatenation

    # Split string into words
    for s_char in s_phrase:
        if s_char != " ":
            s_word_hold += s_char # Hold characters before a space
        else:
            l_word_list.append(s_word_hold) # Then append
            s_word_hold = "" # Empty the string variable for repeatition
    l_word_list.append(s_word_hold) # Add the last word
    # Variable to concatenate characters at the end
    s_char_join = "" 

    # Split string into characters
    for s_word in l_word_list:
        l_char_list = [] 
        for s_char in s_word:
            # List holding every character of each word
            l_char_list.append(s_char)
        # Mutate middle characters to asteriks
        for i_index in range(1, len(l_char_list) - 1):
            l_char_list[i_index] = "*"
        # Proceed to concatenate every character
        for s_char in l_char_list:
            s_char_join += s_char
        # Print a space after the last charater
        # Ignore space after the last character of last word
        s_char_join += " "
    # Display result on console
    print(s_char_join)
    print("It's not palindromic")





