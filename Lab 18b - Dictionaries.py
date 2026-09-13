'''
Gabriel Eze
CSC 170 - b
Lab - 18
Lab Partner - Ben
A revised program of High Jump lab using dictionery.
'''

def dictionary(filename):
    '''
    This take the old or modified file and stores it in a dictionary for further modification.
    Allows other fuctions to operate.
    Parameters:
        filename: [str] name of the file.
    Return:
        d_dict: [dict] dictionary of all contents in the file.
    '''
    s_file = open(filename, mode = "r") # Open the file.
    d_dict = {} # Initialize dictionary to hold all contents of the file.
    s_line = s_file.readline() # Read first line in the file.

    while not(s_line == "" or s_line == "\n"):
        s_line = s_line.strip("\n") # Strip every new - line.
        l_line = s_line.split(",") # Create a list of elements from every line.
        d_dict[l_line[0]] = int(l_line[1].strip()) # Strip for efficient conversion to integer.
        s_line = s_file.readline() # Read next line (if there's one).

    s_file.close() # Close the file.
    return d_dict

def addNew(d_dict, score, student):
    '''
    Function that adds non - existent atheletes to the dictionary.
    Parameters:
        d_dict: [dict] dictionary of all contents in the file.
        score: [int] student's score.
        student: [str] student's name.
    Return:
        d_dict: [dict] dictionary of all modified contents to be in the file.
    '''
    if student in d_dict:
        print("This athlete has an existing data")
    else:
        d_dict[student] = score # Add the new student to the dictionary.
        print("This file has been updated")
    print()

    return d_dict

def graduate(d_dict, student):
    '''
    Removes graduated students from the dictionary.
    Parameters:
        d_dict: [dict] dictionary of all contents in the file.
        student: [str] student's name.
    Return:
        d_dict: [dict] dictionary of all modified contents to be in the file.
    '''    
    if student in d_dict:
        del d_dict[student] # Remove the athlete aloong with his PR.
        print("File has been updated")
    else:
        print("Athelete not found")
    print()
    
    return d_dict

def lookup(d_dict, student):
    '''
    Finds the name of an existing athlete, and prints his PR.
    Parameters:
        d_dict: [dict] dictionary of all contents in the file.
        student: [str] student's name.
    '''
    if student in d_dict:
        print(student, "'s PR = ", d_dict[student], " centimeters", sep = "")
    else:
        print("Athelete not found")
    print()
    
def update(d_dict, score, student):
    '''
    Updates an existing athlete's PR with only a higher score.
    Parameters:
        d_dict: [dict] dictionary of all contents in the file.
        score: [int] student's score.
        student: [str] student's name.
    Return:
        d_dict: [dict] dictionary of all modified contents to be in the file.
    '''
    if student in d_dict:
        i_value = d_dict[student] # Find the athelete's score.
        if score > i_value: # Only modify with a higher PR.
            d_dict[student] = score
            print("File has been updated")
        else:
            print("Can only modify with a higher score")
    else:
        print("Athlete not found")
    print()

    return d_dict

def file_design(d_dict, filename):
    '''
    Function that overwrites the file with updated elements.
    Parameters:
        d_dict: [dict] dictionary of all contents in the file.
        filename: [str] name of the file.
    '''
    s_new_file = open(filename, mode = "w") # Open the file.

    # Overwrite every element in dictionary to the file.
    for s_key in d_dict:
        s_new_file.write(s_key + ", " + str(d_dict[s_key]) + "\n")

    s_new_file.close() # Close the file.

def main():
    f_name = input("Name of File: ")
    print("\n")
    s_purpose = input("Do you want to Lookup, Add, Graduate, or Update your file? Enter (Close) to close the file: ")
    d_dict = dictionary(f_name)

    while not s_purpose == "Close":

        if s_purpose != "Lookup" and s_purpose == "" and s_purpose != "Add" and s_purpose != "Graduate" and s_purpose != "Update":
            s_purpose = input("Do you want to Lookup, Add, Graduate, or Update your file? Enter (Close) to close the file: ")

        if s_purpose == "Lookup":
            print()
            s_student_name = input("Student's name: ")
            print()
            lookup(d_dict, s_student_name)

        elif s_purpose == "Add":
            print()
            i_score = int(input("Student's score: "))
            s_student_name = input("Student's name: ")
            print()
            d_new_dict = addNew(d_dict, i_score, s_student_name)
            file_design(d_new_dict, f_name)

        elif s_purpose == "Graduate":
            print()
            s_student_name = input("Student's name: ")
            print()
            d_remove = graduate(d_dict, s_student_name)
            file_design(d_remove, f_name)

        elif s_purpose == "Update":
            print()
            i_score = int(input("Student's score: "))
            s_student_name = input("Student's name: ")
            print()
            d_update = update(d_dict, i_score, s_student_name)
            file_design(d_update, f_name)

        s_purpose = input("Do you want to Lookup, Add, Graduate, or Update your file? Enter (Close) to close the file: ")
    print()
    print("You have successfully closed the file!")
    
if __name__ == "__main__":
    main()
