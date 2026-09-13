print("Welcome to the Arithmetic Operator!")
print("\n")
# Ask the user if he wants his first problem
s_prompt = input("Do you want to practice arithmetic? (Y/n) ")

while s_prompt == "Y" or s_prompt == "y":
    import random
    i_rand_num_1 = random.randint(1, 20) # First random number
    i_rand_num_2 = random.randint(1, 20) # Second random number
    i_rand_operator = random.randint(0, 2) # Each number corresponds with an operator
    i_attempt = 3


    # Addition loop
    if i_rand_operator == 0:
        i_result = i_rand_num_1 + i_rand_num_2
        print()
        # Display equation on console; wait for input from user
        print(i_rand_num_1, "+", i_rand_num_2, "=", end = " ")
        i_result_console = int(input(""))

        # Command for getting the answer at first attempt
        if i_result_console == i_result:
            print()
            print("Correct!")
            print()
            s_prompt = input("Continue practicing? (Y/n) ")
            # Stop the tutor if the user types "N" or "n"
            if s_prompt == "N" or s_prompt == "n":
                print()
                print("Bye!")

        # Command for first and second incorrect answer; second trial
        else:
            while i_attempt > 1 and i_result_console != i_result:
                i_attempt -= 1
                print()
                print("Sorry, that's incorrect!")
                print()
                # Display equation on console; wait for input from user
                print(i_rand_num_1, "+", i_rand_num_2, "=", end = " ")
                i_result_console = int(input(""))

                # Command for getting the answer without exhaution of attempts;
                # second & third trial
                if i_attempt >= 1 and i_result_console == i_result:
                    print()
                    print("Correct!")
                    print()
                    s_prompt = input("Continue practicing? (Y/n) ")
                    # Stop the tutor if the user types "N" or "n"
                    if s_prompt == "N" or s_prompt == "n":
                        print()
                        print("Bye!")
                        print()

                # Command for exhaution of attempts
                else:
                    if i_attempt == 1 and i_result_console != i_result:
                        print()
                        print("Sorry that's incorrect.", end = " ")
                        print("The correct answer is", i_result)
                        print()
                        s_prompt = input("Continue practicing? (Y/n) ")
                        # Stop the tutor if the user types "N" or "n"
                        if s_prompt == "N" or s_prompt == "n":
                            print()
                            print("Bye!")
                            print()


    # Multiplication loop
    elif i_rand_operator == 1:
        i_result = i_rand_num_1 * i_rand_num_2
        print()
        # Display equation on console; wait for input from user
        print(i_rand_num_1, "*", i_rand_num_2, "=", end = " ")
        i_result_console = int(input(""))

        # Command for getting the answer at first attempt
        if i_result_console == i_result:
            print()
            print("Correct!")
            print()
            s_prompt = input("Continue practicing? (Y/n) ")
            # Stop the tutor if the user types "N" or "n"
            if s_prompt == "N" or s_prompt == "n":
                print()
                print("Bye!")

        # Command for first & second incorrect answer;
        # second trial
        else:
            while i_attempt > 1 and i_result_console != i_result:
                i_attempt -= 1
                print()
                print("Sorry, that's incorrect!")
                print()
                print(i_rand_num_1, "*", i_rand_num_2, "=", end = " ")
                i_result_console = int(input(""))

                # Command for getting the answer without exhaution of attempts;
                # second & third trial
                if i_attempt >= 1 and i_result_console == i_result:
                    print()
                    print("Correct!")
                    print()
                    s_prompt = input("Continue practicing? (Y/n) ")
                    # Stop the tutor if the user types "N" or "n"
                    if s_prompt == "N" or s_prompt == "n":
                        print()
                        print("Bye!")
                        print()
                # Command for exhaution of attempts
                else:
                    if i_attempt == 1 and i_result_console != i_result:
                        print()
                        print("Sorry that's incorrect.", end = " ")
                        print("The correct answer is", i_result)
                        print()
                        s_prompt = input("Continue practicing? (Y/n) ")
                        # Stop the tutor if the user types "N" or "n"
                        if s_prompt == "N" or s_prompt == "n":
                            print()
                            print("Bye!")
                            print()


    # Subtraction loop
    elif i_rand_operator == 2:
        # Allow for only positive results
        i_result = abs(i_rand_num_1 - i_rand_num_2)
        print()
        # Modify the equation, with the maximum number coming first
        # Display equation on console; wait for input from user
        if i_rand_num_2 > i_rand_num_1:
            print(i_rand_num_2, "-", i_rand_num_1, "=", end = " ")
            i_result_console = int(input(""))
        else:
            print(i_rand_num_1, "-", i_rand_num_2, "=", end = " ")
            i_result_console = int(input(""))
        if i_result_console == i_result:
            print()
            print("Correct!")
            print()
            s_prompt = input("Continue practicing? (Y/n) ")
            # Stop the tutor if the user types "N" or "n"
            if s_prompt == "N" or s_prompt == "n":
                print()
                print("Bye!")

        # Command for first & second incorrect answer; second trial
        else:
            while i_attempt > 1 and i_result_console != i_result:
                i_attempt -= 1
                print()
                print("Sorry, that's incorrect!")
                print()
                if i_rand_num_2 > i_rand_num_1:
                    print(i_rand_num_2, "-", i_rand_num_1, "=", end = " ")
                    i_result_console = int(input(""))
                else:
                    print(i_rand_num_1, "-", i_rand_num_2, "=", end = " ")
                    i_result_console = int(input(""))

                # Command for getting the answer without exhaution of attempts;
                # second & third trial
                if i_attempt >= 1 and i_result_console == i_result:
                    print()
                    print("Correct!")
                    print()
                    s_prompt = input("Continue practicing? (Y/n) ")
                    # Stop the tutor if the user types "N" or "n"
                    if s_prompt == "N" or s_prompt == "n":
                        print()
                        print("Bye!")
                        print()

                # Command for exhaution of attempts
                else:
                    if i_attempt == 1 and i_result_console != i_result:
                        print()
                        print("Sorry that's incorrect.", end = " ")
                        print("The correct answer is", i_result)
                        print()
                        s_prompt = input("Continue practicing? (Y/n) ")
                        # Stop the tutor if the user types "N" or "n"
                        if s_prompt == "N" or s_prompt == "n":
                            print()
                            print("Bye!")
                            print()
# If the user chooses not to use the tutor, end the program
if s_prompt == "N" or s_prompt =="n":
    print()
    print("Bye!")
