'''
Gabriel Eze
CSC 170 - b
Lab - 13
Lab Partner - Iris
A program containing a function
that computes the area of a triangle defined by three points.
'''

def distance(x, y):
    '''
    Computes the distances between all points.
    Parameters:
        x: [list] three points of the x - axis.
        y: [list] three points of the y - axis.
    Return:
        dist_list: [list] three side length of the triangle.
    '''
    dist_list = []
    for i_index in range(3): # Distance between two points
        if i_index == 2: # Third side of the triangle
            d = ((x[0] - x[-1]) ** 2 + \
                (y[0] - y[-1]) ** 2) ** 0.5
            dist_list.append(d)
        else: # Two sides of the triangle
            d = ((x[i_index] - x[i_index + 1]) ** 2 + \
                (y[i_index] - y[i_index + 1]) ** 2) ** 0.5
            dist_list.append(d)
    #print("x - coordinates: ", x, "\n", "y - coordinates: ", y, sep = "")
    return dist_list

def triangle_area(dist_list):
    '''
    Computes the area of the triangle using Heron's formula.
    Heron's formula uses the length of the three sides and semi - perimeter.
    Parameters:
        dist_list: [list] three side length of the triangle.
    Return:
        Area: [float] Area of the triangle.
    '''
    perimeter = 0
    for i_element in dist_list: # Perimeter of the triangle
        perimeter += i_element
    f_sp = perimeter / 2 # Semi - perimeter
    # Heron's formula, A = √(s - a)(s - b)(s - c)s
    area = ((f_sp - dist_list[0]) * \
           (f_sp - dist_list[1]) * \
           (f_sp - dist_list[2]) * f_sp) ** 0.5
    return area

# ...Any points of your choice:
area = triangle_area(distance([1, 8, 14], [20, 13, 16])) 
#print("\n", "The area defined by the points in square units is: ", area, sep = "")

