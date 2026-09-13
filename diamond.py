i_count_odd = -1
i_count_even = 1

# Create the variable that makes the outline.
s_diamond = "*"

# Ask the user to input the height of the diamond.
i_diamond = int(input("Please enter height of diamond: "))
i_space = i_diamond

# If the user enters an odd number,
# compute & create the diamond.
if i_diamond % 2 == 1:
    # Program for the top half.
    while i_count_odd < i_diamond:
        i_count_odd += 2
        i_space -= 1
        print(" " * i_space, end = "")
        print(s_diamond * i_count_odd)
    # Program for the bottom half.
    while i_count_odd > 1:
        i_count_odd -= 2
        i_space += 1
        print(" " * i_space, end = "")
        print(s_diamond * i_count_odd)
    print("Here lies your diamond!")

# If the users enters an even number,
# compute & create the diamond.
else:
    # Program for the top half.
    while i_count_even < i_diamond:
        print(" " * i_space, end = "")
        print(s_diamond * i_count_even)
        i_count_even += 2
        i_space -= 1
    # Program for the bottom half.
    while i_count_even > 1:
        i_count_even -= 2
        i_space += 1
        print(" " * i_space, end = "")
        print(s_diamond * i_count_even)
    print("Here lies your diamond!")
