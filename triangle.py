# Create the variable that makes the outline.
s_star = "*"

# Ask the user to enter the height of the triangle
i_height = int(input("Enter height of triangle: "))
i_count = 0

# Compute the code for a right angled triangle.
while i_count < i_height:
    i_count += 1
    print(s_star * i_count)
print("Here is your triangle!")
