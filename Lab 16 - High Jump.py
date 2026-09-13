'''
Gabriel Eze
CSC 170 - b
Lab - 16
Lab Partner - Adrien
A program designed to manage file: the coache's file on PR on his/her athelete.
This program can lookup, add, remove, and update athletes information.

PB: For efficient tase case based on my data structures,
your test file should have a comma after the Athlete's name.
'''


def file_list(filename):
    '''
    This take the old or modified file, turns in into a list for further modification.
    Allows for other fuctions to operate.
    Parameters:
        filename: [str] name of the file.
    Return:
        l_file: [list] list of all contents in the file.
    '''
    s_file = open(filename, mode = "r") # Open the file.
    l_file = [] # Empty file to hold existing content of the file.
    s_line = s_file.readline() # Variable to read every line in the file.

    while not (s_line == "" or s_line == "\n"):
        l_line = s_line.split(",") # Create a list of elements from every line.
        # Append all elements from respective lines to the list of file.
        l_file.append(l_line[0])
        l_file.append(l_line[1])
        s_line = s_file.readline()

    s_file.close() # Close the file
    return l_file


def scrub(f_list):
    '''
    Cleans up whitespaces and removes excess strings to reduce bugs during comparison.
    This is done before the request of the user.
    Parameter:
        f_list: [list] list of all contents in the file.
    Return:
        f_list: [list] list of all scrubbed elements to be compared with user's requests.
    '''
    for i_index in range(0, len(f_list), 2):
        f_list[i_index] = f_list[i_index].strip(",") # Strips all commas from athlete's name

    for i_index in range(1, len(f_list), 2):
        f_list[i_index] = f_list[i_index].strip() # Strips all white - space and new line from scores

    return f_list


def addNew(f_list, score, student):
    '''
    Function that adds non - existent atheletes to the file.
    Parameters:
        f_list: [list] list of all contents in the file.
        score: [str] student's score.
        student: [str] student's name.
    Return:
        f_list: [list] list of all modified contents to be in the file.
    '''
    if student in f_list:
        print("This athlete has an existing data")

    else: # Add the new student to the list
        f_list.append(student)
        f_list.append(score)
        print("This file has been updated")
    print()
        
    return f_list


def graduate(f_list, student):
    '''
    Removes graduated students from the list
    Parameters:
        f_list: [list] list of all contents in the file.
        student: [str] student's name.
    Return:
        f_list: [list] list of all modified contents to be in the file.
    '''
    if student in f_list:
        # Remove the athlete aloong with his PR
        i_pos = f_list.index(student)
        f_list.remove(student)
        f_list.remove(f_list[i_pos])
        print("File has been updated")
    else:
        print("Athelete not found")
    print()
    
    return f_list

            
def lookup(f_list, student):
    '''
    Finds the name of an existing athlete, and prints his PR.
    Parameters:
        f_list: [list] list of all contents in the file.
        student: [str] student's name.
    '''
    if student in f_list:
        i_pos = f_list.index(student) + 1
        print(student, "'s PR = ", f_list[i_pos], " centimeters", sep = "")
    else:
        print("Athelete not found")
    print()


def update(f_list, score, student):
    '''
    Updates an existing athlete's PR with only a higher score.
    Parameters:
        f_list: [list] list of all contents in the file.
        student: [str] student's name.
    Return:
        f_list: [list] list of all modified contents to be in the file.
    '''
    if student in f_list:
        i_pos = f_list.index(student) + 1
        if score > int(f_list[i_pos]):
            f_list[i_pos] = str(score)
            print("File has been updated")
        else:
            print("Can only modify with a higher score")
    else:
        print("Athlete not found")
    print()

    return f_list


def arrange(f_list):
    '''
    Adds required commas, whitespaces, and new lines to the file string.
    This function constructs the final outlook of the file.
    Parameter:
        f_list: [list] list with athelete's names and scores.
    Return:
        f_list: [list] final construct for the file.
    '''
    for i_index in range(len(f_list)):

        # Add commas at the end of the athlete's name
        if i_index % 2 == 0 and "," not in f_list[i_index]:
            f_list[i_index] += ","

        # Add a whitespace and new - line at the beginning and end of athlete's score
        elif i_index % 2 == 1 and "\n" not in f_list[i_index]:
            f_list[i_index] += "\n"
            if " " not in f_list[i_index]:
                f_list[i_index] = " " + f_list[i_index]

    return f_list


def file_design(f_list, filename):
    '''
    Function that overwrites the file with updated elements.
    Parameters:
        f_list: [list] list of all modified contents to be in the file.
        filename: [str] name of the file.
    '''
    s_new_file = open(filename, mode = "w") # Open the file

    for s_element in f_list:
        s_new_file.write(s_element)   

    s_new_file.close() # Close the file

    
def main():
    f_name = input("Name of File: ")
    print("\n")
    s_purpose = input("Do you want to Lookup, Add, Graduate, or Update your file? Enter (Close) to close the file: ")
    lst = file_list(f_name)

    while not s_purpose == "Close":

        if s_purpose != "Lookup" and s_purpose == "" and s_purpose != "Add" and s_purpose != "Graduate" and s_purpose != "Update":
            s_purpose = input("Do you want to Lookup, Add, Graduate, or Update your file? Enter (Close) to close the file: ")
        
        if s_purpose == "Lookup":
            print()
            s_student_name = input("Student's name: ")
            print()
            l_before = scrub(lst)
            lookup(l_before, s_student_name)
            
        elif s_purpose == "Add":
            print()
            s_score = input("Student's score: ")
            s_student_name = input("Student's name: ")
            print()
            l_before = scrub(lst)
            l_new_file = addNew(l_before, s_score, s_student_name)
            file_design(arrange(l_new_file), f_name)
            
        elif s_purpose == "Graduate":
            print()
            s_student_name = input("Student's name: ")
            print()
            l_before = scrub(lst)
            l_remove = graduate(l_before, s_student_name)
            file_design(arrange(l_remove), f_name)
       
        elif s_purpose == "Update":
            print()
            i_score = int(input("Student's score: "))
            s_student_name = input("Student's name: ")
            print()
            l_before = scrub(lst)
            l_update = update(l_before, i_score, s_student_name)
            file_design(arrange(l_update), f_name)

        s_purpose = input("Do you want to Lookup, Add, Graduate, or Update your file? Enter (Close) to close the file: ")
    print()
    print("You have successfully closed the file!")
    
if __name__ == "__main__":
    main()
