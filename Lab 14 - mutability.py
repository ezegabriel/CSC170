'''
Gabriel Eze
CSC 170 - b
Lab - 13
Lab Prtner - Ethan
A program containing two functions
First sorts a copy of an original list
Second sorts the actual list
'''
def sorted_list(lst):
    '''
    Arranges a list in non - decreasing order
    without modifying the original list.
    Paramters:
        lst: [list] list to be arranged.
    Return:
        l_list: [lsit] a copy of an arranged list.
    '''
    
    l_list = lst.copy() # Make a copy
    for i_pos in range(15): # Run through the list multiple times
        for i_index in range(len(l_list) - 1):
            # Shifts places of the two adjacent objects 
            if l_list[i_index] > l_list[i_index + 1]:
                # A temporary variale that stores
                # the maximum of the two objects
                i_tmp = l_list[i_index]
                l_list[i_index] = l_list[i_index + 1]
                l_list[i_index + 1] = i_tmp
    print("Test Case 1:")
    print("Original:", lst)
    return l_list

def sort_in_place(l_list):
    '''
    Arranges a list in non - decreasing order
    by modifying the original list.
    Paramters:
        lst: [list] list to be arranged.
    '''
    for i_index in range(15): # Run through the list multiple times
        for i_index in range(len(l_list) - 1):
            # Shifts places of the two adjacent objects
            if l_list[i_index] > l_list[i_index + 1]:
                # A temporary variale that stores
                # the maximum of the two objects
                i_tmp = l_list[i_index]
                l_list[i_index] = l_list[i_index + 1]
                l_list[i_index + 1] = i_tmp
    print("Sorted: ", l_list)

def main():
    list_1 = [1, 2, 74, 12, 34, 89, 36]
    list_2 = [5, 5, 734, 71, 71, 56, 28]
    print("Sorted:", sorted_list(list_1), "\n")
    print("Test Case 2:")
    print("Original:", list_2)
    sort_in_place(list_2)

if __name__ == "__main__":
    main()

'''
The problem is from the assignment on the last line.
After the programs  sorts all objects in the right place,
it assigns l_unsorts to l_sort which breaks the link between what list plugged
in the parameter and the sorted list.
'''

