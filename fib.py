
i_num = int(input("Please enter your nth term of Fibonacci sequence: "))



l_list = [0, 1]

if i_num > 1:
    # A definite loop to add the last 2 numbers in the sequence
    for i_fib in range(2, (i_num + 1)):
        i_append = l_list[i_fib - 1] + l_list[i_fib - 2]
        l_list.append(i_append)
    print("Fibonacci number:", l_list[-1])
    print("Fibonacci sequence:", l_list)
elif i_num == 1:
    print("1")
elif i_num == 0:
    print("0")
elif i_num < 0:
    print("Please enter a positive integer!")

