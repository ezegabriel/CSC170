'''
Gabriel Eze
CSC 170 - b
Lab - 15
Lab Partner - Ethan
A lab that practices reading texts from files with a function:
uses the function to compute the number of unique words in file.
'''

def count(lst):
    '''
    Computes the number of unique words from an input file
    by creating another list to accept only unique words.
    Parameters:
        lst: [list] holds all the words.
    Return:
        len(lst): the number of unique words.
    '''
    l_list = [] # Empty list to hold unique words.
    for s_word in lst:
        if s_word not in l_list:
            l_list.append(s_word)

    return(l_list)

def main():
    s_name = input("Please enter name of file: ")
    file = open(s_name, mode = "r") # Open the file.
    s_poem = file.read() # Read the entire file into one string.
    s_poem = s_poem.lower() # Correct all letters to lower case for efficient comparison.

    # A variable preventing these punctuation from passing through.
    i_punc = '''.'';'?:",()-!_[]\|''' 
    word = "" # A variable to store the poem without punctuations.
    for s_char in s_poem: # Iterate over every character in the poem.
        if s_char not in i_punc:
            word += s_char # Concatenate only letters and spaces.
    l_word = word.split() # Create a list of substrings of words.
    unique = count(l_word)

    d_dict = {}
    for s_word in unique:
        i_count = 0
        for s_element in l_word:
            if s_word == s_element:
                i_count += 1
        d_dict[s_word] = i_count
    print(d_dict)
    print(len(d_dict))
    values = d_dict.values()
    values = list(values)
    print(sum(values))
    #print("There are", len(l_word), "words in the file!")
    #print("There are", unique, "unique words in the file!!")

    file.close() # Close the file.

if "__main__" == __name__:
    main()
    

