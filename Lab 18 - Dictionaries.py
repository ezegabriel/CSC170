'''
Gabriel Eze
CSC 170 - b
Lab - 18
Lab Partner - Ben
A revised program of File, Input & Output lab using a dictionary.
'''

def dictionary(name):
    '''
    Creates a dictionary with every word and their tally.
    Parameter:
        name: [str] name of input file.
    Return:
        d_dict: [dict] dictionary of all unique words in the file.
    '''
    file = open(name, mode = "r") # Open the file.

    s_poem = file.read() # Read the entire file into one string.
    s_poem = s_poem.lower() # Correct all letters to lower case for efficient comparison.
    # A variable preventing these punctuation from passing through.
    s_punc = '''.'';'?:",()-!_[]\|''' 
    word = ""
    for i_char in s_poem:
        if i_char not in s_punc:
            word += i_char # Concantenate only letters.
    l_word = word.split() # Create a list of substrings of all words.

    d_dict = {} # Initiate the dictionary to store unique words.
    for s_key in l_word:
        i_value = 0 # Reset counter after each loop.

        # Loop to find and add every occurrence of s_key.
        for s_element in l_word: 
            if s_key == s_element:
                i_value += 1 # Increment the number times s_key is found.
        d_dict[s_key] = i_value # Add (key, value) to the dictionary.
        
    file.close() # Close the file.
    return d_dict

def main():
    s_name = input("Please enter name of file: ")
    d_dict = dictionary(s_name)
    values = d_dict.values() # The frequencey of words.

    print("There are", sum(values), "words in the file!")
    print("There are", len(d_dict), "unique words in the file!!")
    print(d_dict)
 
main()
