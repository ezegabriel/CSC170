'''
Gabriel
CSC 170 - b
Lab 12 - Intro to functions
A python file that imports another python file holding a series of created functions
Then tests each function in two cases, then calls help() for every function.
'''
import my_utilities

upper_bound_1 = my_utilities.ceiling(8.1) # well-behaved
upper_bound_2 = my_utilities.ceiling(2) # edge-case
help(my_utilities.ceiling)

lower_bound_1 = my_utilities.floor(6.6) # well-behaved
lower_bound_2 = my_utilities.floor(4) # edge-case
help(my_utilities.floor)

circle_1 = my_utilities.circle_area(15.4) # well-behaved
circle_2 = my_utilities.circle_area(0) # edge-case
help(my_utilities.circle_area)

sphere_1 = my_utilities.sphere_volume(3) # well-behaved
sphere_2 = my_utilities.sphere_volume(0) # edge-case
help(my_utilities.sphere_volume)

rect_1 = my_utilities.rect_area(2, 5.5) # well-behaved
rect_2 = my_utilities.rect_area(0, 3) # edge-case
help(my_utilities.rect_area)

box_1 = my_utilities.volume_box(36, 4, 9) # well-behaved
box_2 = my_utilities.volume_box(23, 1, 0) # edge-case
help(my_utilities.volume_box)

word_1 = my_utilities.censor("rodney") # well-behaved
word_2 = my_utilities.censor("c") # edge-case
help(my_utilities.censor)


