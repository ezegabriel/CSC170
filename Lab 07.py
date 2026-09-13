'''
Gabriel Eze
Lab07 - for loops
CSC 170-b
Lab Partner: Pranjal
Apparantly, Pranjal refused my help,
so I would like to make a plea of exemption towards his lab

'''

#Part 1a

#Copy and paste the numbers from moodle into a list
l_list = [99, 48, 58, 72, 85, 34, 42, 72, 19]
i_pos = l_list.index(85)
print(i_pos)

# Select a benchmark to compare the minimum and maximum number
i_min = l_list[3]
i_max = l_list[1]

# To determine the mean, tally the numbers and find its sum
i_freq = len(l_list)
i_sum = 0

# Make use of a definite loop
# To find the minimun, maximum, and mean of numbers
for i_number in l_list:
    if i_number < i_min:
        i_min = i_number
    elif i_number > i_max:
        i_max = i_number
    i_sum += i_number
print("The minimum number is", i_min)
print("The maximum number is", i_max)
print("The mean of your numbers is", i_sum / i_freq, "\n")

# Part 1b

print("You have the freedom to create your own list")
print("The list must contain only numbers")

# Ask the user to enter a number
# Assign "0" to the sum variable to find the new sum
s_new_number = input("Please add a number to the existing list: ")
i_sum = 0
l_list = []

# An indefinite loop to terminate the program if a number is not entered
while bool(s_new_number) == True:
    i_number = int(s_new_number)
    l_list.append(i_number)
    s_new_number = input("Please add a number to the existing list: ")
print(l_list)

# A definite loop
# To find the minimun, maximum, and mean of numbers
for i_number in l_list:
    i_freq = len(l_list)
    i_sum += i_number
print("The minimum number is", min(l_list))
print("The maximum number is", max(l_list))
print("The mean of your numbers is", i_sum / i_freq, "\n")

# Part 2

# Create variables for the Fibonacci sequence
i_fib_0 = 0
i_fib_1 = 1
i_fib = 0

# Ask the user the enter the position of number
# In the Fibonacci sequence that is suited to Python syntax
i_num = int(input("Please enter your nth term of Fibonacci sequence: "))
while i_num < 0:
    i_num = int(input("Please enter your nth term of Fibonacci sequence: "))
# While loop to add the last 2 numbers in the sequence
if i_num > 1:
    while i_num > 1:
        i_fib = i_fib_0 + i_fib_1
        i_fib_0 = i_fib_1
        i_fib_1 = i_fib
        i_num -= 1
    print("Fibonacci number:", i_fib) 
elif i_num == 0:
    print("Fibonacci number:", i_fib_0)
elif i_num == 1:
    print("Fibonacci number:", i_fib_1)
