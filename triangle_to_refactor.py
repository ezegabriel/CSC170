# William Bailey - March 18, 2022
# Computes the area of a triangle defined by three points.

# ASSIGNMENT: Refactor this program to:
# - reduce repeated code
# - promote reusability
# - remove global variables

# You will want to introduce some function for this. You may also want to change
# how the program works, without changing it's functionality. Remember, from the
# user's perspective, only the inputs and outputs are visable.

# Get the points:
f_x1 = float(input("Point 1 x: "))
f_y1 = float(input("Point 1 y: "))

f_x2 = float(input("Point 2 x: "))
f_y2 = float(input("Point 2 y: "))

f_x3 = float(input("Point 3 x: "))
f_y3 = float(input("Point 3 y: "))

# To use Heron's formula:
#      ______________________
# A = √(s - a)(s - b)(s - c)s
#
# We need:
#  - the lengths of each side of the triangle: a, b, and c,
#  - the semi-perimiter s = (a+b+c)/2

# Side lenghts (using the Pythagorean theorem):
# Side a (point 1 -- point 2)
f_a = ((f_x1-f_x2) ** 2 + (f_y1-f_y2) ** 2) ** 0.5 # power 1/2 == square root

# Side b (point 2 -- point 3)
f_b = ((f_x2-f_x3) ** 2 + (f_y2-f_y3) ** 2) ** 0.5

# Side c (point 3 -- point 1)
f_c = ((f_x3-f_x1) ** 2 + (f_y3-f_y1) ** 2) ** 0.5

# Semi-perimiter:
f_s = (f_a + f_b + f_c) / 2

# Area:
f_Area = ((f_s - f_a) * (f_s - f_b) * (f_s - f_c) * f_s) ** 0.5

print("The area defined by the points:")
print(f"({f_x1}, {f_y1})")
print(f"({f_x2}, {f_y2})")
print(f"({f_x3}, {f_y3})", end="\n\n")
print("is", f_Area)
