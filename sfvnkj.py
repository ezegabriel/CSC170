i_num = int(input("Enter a number: "))
l_list = [0,1]

if i_num > 2:
    for i_fib in range (2, (i_num + 1)):
        i_append = l_list[i_fib - 1] + l_list[i_fib - 2]
        l_list.append(i_append)
print(l_list)
