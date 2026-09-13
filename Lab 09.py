'''
Gabriel Eze
Lab 09 - Sorting
Lab partner: Pranjal

'''
# Create an empty list to append 10 random numbers
l_list = []

# Indefinite loop to create list of 10 numbers
while len(l_list) < 10:
    # Import a new random while the loop runs
    import random
    i_random = random.randint(1, 100)
    l_list.append(i_random)
# Display the resulting list on the console
print("Random:", l_list)

# Bubble sort
# Runs through the loop, shifting the maximum number to the end
for i_count in range(0, 10):
    for i_index in range(0, 9):
        if l_list[i_index] > l_list[i_index + 1]:
            # A temporary variale that stores
            # the maximum of the two comparisons
            i_switch = l_list[i_index]
            l_list[i_index] = l_list[i_index + 1]
            l_list[i_index + 1] = i_switch
# A sorted list in ascending order displayed on the console
print("Sorted:", l_list)

print()
s_word = input("Please input your choice of phrase: ")
l_word = s_word.split(" ")
print("Original:", s_word)

# Bubble sort
# Runs through the loop, sorting the list in increasing alphabetical order
for i_index in range(0, 15):
    for i_index in range(len(l_word) - 1):
        if l_word[i_index] > l_word[i_index + 1]:
            # A temporary variale that stores
            # the maximum of the two comparisons
            i_tmp = l_word[i_index]
            l_word[i_index] = l_word[i_index + 1]
            l_word[i_index + 1] = i_tmp
# A string of words in ialphabetical order displayed on the console
print("Sorted:", " ".join(l_word), sep = "")
