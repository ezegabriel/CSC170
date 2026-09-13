'''
September 2, 2022
Gabriel Eze
Lab02
CSC 170-b
'''

# Enter amount to be changed
cents = int(input("Please input money: "))

# Calculate how much quarter is needed
quarters = cents // 25
rem = cents % 25

# Caluclate how much dime needed
dime = rem // 10
rem = rem % 10

# Calculate how much nickel is needed
nickel = rem // 5

# Calculate how much penny is needed
penny = rem % 5


print (quarters, " quarter(s)", "\n", dime, " dime(s)", "\n",
        nickel, " nickle(s)", "\n", penny, " pennies", sep = "")


