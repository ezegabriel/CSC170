'''
Gabriel Eze
CSC 170-b
Lab6 - Roman Numerals

'''
# Ask the user to input a number.
i_roman = int(input("Please input number: "))

# Create a string variable that hold the conversion
s_roman = ""

s_numeric = i_roman

# Programs for numbers above 1000
while i_roman >= 1000:
    i_roman -= 1000
    s_roman += "M"

# Program for numbers above 500
while i_roman >= 500:
    if i_roman >= 900:
        i_roman -= 900
        s_roman += "CM"
    else:
        i_roman -= 500
        s_roman += "D"

# Program for numbers above 100
while i_roman >= 100:
    if i_roman >= 400:
        i_roman -= 400
        s_roman += "CD"
    else:
        i_roman -= 100
        s_roman += "C"

# Program for numbers above 50
while i_roman >= 50:
    if i_roman >= 90:
        i_roman -= 90
        s_roman += "XC"
    else:
        i_roman -= 50
        s_roman += "L"

# Program for numbers above 10
while i_roman >= 10:
    if i_roman >= 40:
        i_roman -= 40
        s_roman += "XL"
    else:
        i_roman -= 10
        s_roman += "X"

# Program for numbers above 5
while i_roman >= 5:
    if i_roman >= 9:
        i_roman -= 9
        s_roman += "IX"
    else:
        i_roman -= 5
        s_roman += "V"

# Program for numbers above 1
if i_roman >= 1:
    if i_roman >= 4:
        i_roman -= 4
        s_roman += "IV"
    else:
        s_roman += "I" * i_roman
print(s_numeric, "is", s_roman, "in Roman Numerals.")
    
    
