'''
Gabriel Eze
CSC 170 - b
Project 1
A program that can accurately compare the STR repetition counts to many in a database.
Thus, finding DNA matches.
'''


def s_file(filename):
    '''
    Fuction that open and reads DNA sequence.
    Parameters:
        filename: [str] name of the file to be read.
    Return:
        dna_sequence: [str] variable holding DNA sequence.
    '''
    candidate = open(filename, mode = "r") # Open sequence file
    dna_sequence = candidate.read() # Read all content
    candidate.close() # Close sequence file
    
    return dna_sequence


def scrub(dna):
    '''
    Major bulk of computational program.
    Takes the sequence of DNA, and creates every possible str repitition using 2D lists.
    Then, it cleans it up, by finding the right DNA sequences.
    Paramaters:
        dna: [str] one big string holding the entire DNA.
    return:
        l_scrub: [list] list of all correct DNA sequences.
    '''
    seq_1, seq_2, seq_3 = list("AGAT"), list("AATG"), list("TATC")
    l_temp, l_list2D, l_scrub = [], [], []
    i_start, i_end = 0, 4 # Set limits for the iterations

    while i_start <= len(dna) - 4: # Stop the loop if gotten to the last 4 DNA strings
        for i_index in range(i_start, i_end): # Create a 2D list of every possible DNA string repitition
            l_temp.append(dna[i_index])
        l_list2D.append(l_temp) # Concatenate the list into the 2D list
        l_temp = []
        i_start += 1
        i_end += 1

    # Scrub the list of every anomaly
    for i_index in range(len(l_list2D)):
        if l_list2D[i_index] == seq_1 or l_list2D[i_index] == seq_2 or l_list2D[i_index] == seq_3:

            # Add the first DNA string to the scrubbed list
            if l_scrub == []:
                l_scrub.append(l_list2D[i_index]) 
            else:

                # Check the previous DNA string to confirm that it is a repitition
                if l_list2D[i_index] == l_scrub[-1]: 
                    if l_list2D[i_index - 4] == seq_1 or l_list2D[i_index - 4] == seq_2 or l_list2D[i_index - 4] == seq_3:
                        l_scrub.append(l_list2D[i_index])
                else: # Confirm every new DNA string repitition is unique

                    if not l_list2D[i_index] in l_scrub:
                        # Check if a DNA string has zero repitition
                        if not (l_list2D[i_index] == l_list2D[i_index - 4] and l_list2D[i_index] == l_list2D[i_index + 4]):
                            l_scrub.append(l_list2D[i_index])
                        elif l_list2D[i_index + 4] == seq_1 or l_list2D[i_index + 4] == seq_2 or l_list2D[i_index + 4] == seq_3:
                            l_scrub.append(l_list2D[i_index])

    return l_scrub


def troubleshooting(l_list, testfile):
    '''
    Compares accurately the number of repititive DNA strings  with the CSV file
    and outputs the match.
    Parameters:
        l_list: [list] list of all repititive DNA strings.
        testfile: [str] name of CSV file
    '''
    test = open(testfile, mode = "r") #Open file
    header, test_1, test_2, test_3 = [], [], [], []
    test.readline()

    for s_line in test: # Read every line into lists
        s_line = s_line.rstrip()
        l_line = s_line.split(",")
        header.append(l_line[0]) # Name of test subjects
        test_1.append(l_line[1]) # Count for "AGAT" in a every sequence 
        test_2.append(l_line[2]) # Count for "AATG" in a every sequence
        test_3.append(l_line[3]) # Count for "TATC" in a every sequence
    test.close() # Close the file

    test_1a, test_1b, test_1c = 0, 0, 0 # Variable for counts of 3 DNA sequences from the program's computation
    for s_element in l_list:
        if s_element == list("AGAT"):
            test_1a += 1
        elif s_element == list("AATG"):
            test_1b += 1
        elif s_element == list("TATC"):
            test_1c += 1

    # If program's computation matches the CSV's, show its accurate match
    if test_1a == int(test_1[0]) and test_1b == int(test_2[0]) and test_1c == int(test_3[0]):
        print("DNA sequence matches ", header[0], "'s", sep = "")
    elif test_1a == int(test_1[1]) and test_1b == int(test_2[1]) and test_1c == int(test_3[1]):
        print("DNA sequence matches ", header[1], "'s", sep = "")
    elif test_1a == int(test_1[2]) and test_1b == int(test_2[2]) and test_1c == int(test_3[2]):
        print("DNA sequence matches ", header[2], "'s", sep = "")
    else:
        print("DNA sequence shows no match") # Anomaly case for sequence4

                            
def main():
    filename = input("Please enter the name of file: ")

    while filename != "STOP":
        dna = s_file(filename) # Read the sequence file
        troubleshooting(scrub(dna), "dna_data.csv")
        print()
        filename = input("Enter sequence file to be analyzed(Enter STOP to end): ")
    print("DNA Ananlysis terminated!")

if "__main__" == __name__:
    main()
