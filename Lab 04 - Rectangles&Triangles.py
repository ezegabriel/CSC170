'''

Gabriel Eze
Lab-04
CSC-170b
Program to calculate the area of a rectangle and triangle


'''

#        *------------*(x2,y2)
#        |            |
# (x1,y1)*------------*

print("Program to calculate area of a rectangle", "\n")

f_x1 = float(input('Enter the first x coordinate: '))
f_y1 = float(input('Enter the first y coordinate: '))

f_x2 = float(input('Enter the second x coordinate: '))
f_y2 = float(input('Ender the second y coordinate: '))
print("\n")

# Area computation:
f_length = (f_x2 - f_x1)
f_height = (f_y2 - f_y1)

if f_length == f_height:
    b_is_square = True
else:
    b_is_square = False

f_rect_area = f_length * f_height

# Print the result to two decimal places.
print('Area: ' + str(f_rect_area) + " square units")

if b_is_square == True:
    print('Your rectangle is also square')


# Ask the user the input length of three sides
print("\n")
print("Program to calculate area of a triangle", "\n")

a = float(input("Please enter length of the side: "))
b = float(input("Please enter length of the side: "))
c = float(input("Please enter length of the side: "))
print("\n")

# Area computation
s = (a + b + c) / 2
area = (s * (s-a) * (s-b) * (s-c)) ** 0.5

if a == b == c:
    print("The area of your equilateral triangle is", str(area), "square units")
else:
    print("The area of your scalene triangle is", str(area), "square units")


