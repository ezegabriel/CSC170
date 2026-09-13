# Demonstrate functions and mutability

def my_function(l_list):
    l_list += [10000]

def find_max(l_list):
    '''Find and return the largest item in the list.'''
    # l_list = l_list + [] # copy
    # l_list = l_list.copy()
    l_list = l_list[::]
    i_max = l_list[0]
    while len(l_list) > 0:
        i_value = l_list[0]
        del l_list[0]
        if i_value > i_max:
            i_max = i_value
    return i_max

def sum_of_1_to_n(x):
    '''Finds the sum of the integers from 1 to i_num.'''
    if x < 0:
        return 0
    i_total = 0
    while x > 0:
        i_total = i_total + x
        x -= 1
    print("x =", x)
    return i_total

def main():
    a = [1, 2, 3, 4, 5]
    my_function(a)
    print(a)
    i_big = find_max(a)
    print(i_big)
    print(a)
    x = 42
    i_total = sum_of_1_to_n(x) # does this change x?
    print("total =", i_total) # 1 + 2 + 3 + ... + 41 + 42
    print("x =", x) 

if __name__ == '__main__':
    main()

