# my_utilities.py - Some functions for Lab 11. - William Bailey - March 2021

# Below are some examples of good style for docstrings.
'''
Gabriel Eze
CSC 170 - b
Lab 12 - Intro to Functions
Lab Partner - Iris
A python file holding a series of created function commands
'''

def distance_between(num1, num2):
    '''
    Comuptes the difference between num1 and num2. Uses absolute value.
    Parameters:
        num1: [int or float] (No interpretation, just a number)
        num2: [int or floar] (No interpretation, just a number)

    Returns:
        dst: [int or float] the absolute value of the difference between num1 and num2.
    '''
    if num1 < num2:
        num1, num2 = num2, num1

    dst = num1 - num2
    return dst


def square_area(edge_len):
    '''
    Computes the area of a string with sides of length edge_len.
    Parameters:
        edge_len: [int or float] length of one edge of a square

    Return:
        square_area: [int or float] area of the square, in square units.
    '''
    
    assert edge_len >= 0, "Negative lengths don't make sense."
    return edge_len ** 2


def ceiling(num):
    '''
    Computes the round up of a positive or negative float.
    Parameters:
        num : int or float.
    Return:
        Determines if num is a float and rounds it up to the nearest float
        Otherwise, leaves it as it is - integer.
    '''
    if num % 1 == 0:
        return num
    else:
        return num // 1 + 1
def floor(num):
    '''
    Computes the round down of a float positive or negative float.
    Parameters:
        num : int or float.
    Return:
        Determines if num is a float and rounds it down to the nearest integer
        Otherwise, leaves it as it is - integer.
    '''
    return num // 1


def circle_area(r):
    '''
    Computes the area of a circle with a positive radius.
    Imports the number, pi, from the math fuction
    in order to calcute the area with high accuracy.
    Parameter:
        radius(r): [int or float] distance from centre of circle to circumference.
    Return:
        circle_area: [float] area of the circle, in square units.
    '''
    if r > 0:
        import math
        return math.pi * r ** 2


def sphere_volume(r):
    '''
    Computes the volume of a sphere with a positive radius.
    Imports the number, pi, from the math fuction
    in order to calcute the volume with high accuracy.
    Parameter:
        radius(r): [int or float] distance from centre of sphere to elliptical surface.
    Return:
        sphere volume: [float] volume of a sphere , in cubic units.
    '''
    if r > 0:
        import math
        return 4/3 * math.pi * r ** 3


def rect_area(l, b):
    '''
    Computes the area of a rectangle using positive side lengths.
    Parameters:
        length(l): [int or float] Length of the rectangle
        breadth(b): [int or float] Breadth of the rectangle
    Return:
        rect_area: [int or float] area of the rectangle, in square units.
    '''
    if l > 0 and b > 0:
        return l * b


def volume_box(l, b, h):
    '''
    Computes the volume of the box using positive side lengths.
    Parameters:
        length(l): [int or float] Length of the box
        breadth(b): [int or float] Breadth of the box
        height(h): [int or float] Height of the box
    Return:
        volume_box: [int or float] area of the rectangle, in cubic units.
    '''
    if l > 0 and b > 0 and h > 0:
        return l * b * h


def censor(word):
    '''
    Mutates all characters of "word" with an asterisk (*) except for the first and last.
    Parameters:
        word: [str] a string literal converted to a list to be mutated.
    Return:
        word: [str] word now holds the all the characters joined after mutation.
    '''
    l_word = list(word)
    for i_index in range(1, len(word) - 1):
        l_word[i_index] = "*"
    word = "".join(l_word)
    return word
