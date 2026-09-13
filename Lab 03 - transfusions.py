'''
Gabriel Eze
CSC 170-b
Lab03 - Transfusions
Partner: Bryan

'''
# Ask user to input blood group and rhesus factor
dbg = input("Please input donor's blood group: ")
drf = input("Plese input donor's rhesus factor: ")
rbg = input("Please input recipient's blood group: ")
rrf = input("Please input recipient's rhesus factor: ")


# Create and compute the variable that calculates all the possibilities

result = (dbg == "O" and drf == "-")\
      or (dbg == "O" and drf == "+" and rrf == "+")\
      or (dbg == "A" and drf == "-" and (rbg == "A" or rbg == "AB"))\
      or (dbg == "A" and drf == "+" and (rbg == "A" or rbg == "AB") and rrf == "+")\
      or (dbg == "B" and drf == "-" and (rbg == "B" or rbg == "AB"))\
      or (dbg == "B" and drf == "+" and (rbg == "B" or rbg == "AB") and rrf == "+")\
      or (dbg == "AB" and drf == "-" and rbg == "AB")\
      or (dbg == "AB" and drf == "+" and rbg == "AB" and rrf == "+")


# Show result to determine compatibility

print("The Human Blood Compatibility is", str(result))

