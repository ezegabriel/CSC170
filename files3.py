# More fun with files(Day 2)

def main():
    # open the file
    input_file = open("scores.csv", mode="r")

    # process the file (input)
    # method 1: .read()
    # s_whole_file = input_file.read()
    # print(s_whole_file)

    # method 2: .readline()
    '''
    s_line = input_file.readline()
    while s_line != "":
        s_line = s_line.rstrip('\n')
        print(s_line)
        s_line = input_file.readline()
    '''

    # method 3: .readlines()
    # l_lines = input_file.readlines()
    # print(type(l_lines))
    # print(l_lines)

    # method 4: for (each) loop
    for s_line in input_file:
        s_line = s_line.rstrip('\n')
        print(s_line)
    
    # close the file
    input_file.close()

if __name__ == '__main__':
    main()
