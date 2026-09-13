'''
Gabriel Eze
CSC 170 - b
Lab - 21
Lab Partner - Vedant
An introductory lab into Object Oriented Programming.
'''

class TrainCar:
    '''
    UML Class design
    
    TrainCar
    --------------------------------------------------------------

    - color: string
    - car_type: string
    - length: integer

    --------------------------------------------------------------

    + __init__(color: string, car_type: string, length: integer)
    + set_color(color: string): void
    + get_car_type(): string
    + set_car_type(car_type: string): void
    + get_length(): integer
    + set_length(length: integer): void

    --------------------------------------------------------------
    Create 5 unique objects from this class.

    '''
    # Constructor
    def __init__(self, color, car_type, length):
        self.__s_color = color
        self.__s_car_type = car_type
        self.__i_length = length
        self.previous = None
        self.next = None

    # Mutator (setters)
    def set_color(self, color):
        self.__s_color = color

    def set_car_type(self, car_type):
        self.__s_car_type = car_type

    def set_length(self, length):
        self.__i_length = length

    # Accessor (getters)
    def get_color(self):
        return self.__s_color

    def get_car_type(self):
        return self.__s_car_type

    def get_length(self):
        return self.__i_length

    # Special method (system)
    def __str__(self):
        s_string_rep = "Color: " + self.__s_color + ", Type of Car: " + self.__s_car_type + \
                   ", Length (ft): " + str(self.__i_length)
        return s_string_rep
    

class Engine(TrainCar):
    def __init__(self, length):
        TrainCar.__init__(self, "Black", "Engine", length)

class Caboose(TrainCar):
    def __init__(self, length):
        TrainCar.__init__(self, "Cyan", "Caboose", length)
    
def main():
    
    # First unique instance
    red_Honda = TrainCar("Red", "Honda", 60) 

    # Second unique instance
    black_Porsche = TrainCar("Black", "Porsche", 78)

    # Third unique instance
    blue_Ford = TrainCar("Blue", "Ford", 70)

    # Fourth unique instance
    orange_Ginetta = TrainCar("Orange", "Ginetta", 80)

    # Fifth unique instance
    grey_Mazda = TrainCar("Grey", "Mazda", 55)

    l_list = [red_Honda, black_Porsche, blue_Ford, orange_Ginetta, grey_Mazda]
    # Display contents of the list: 5 unique objects
##    for s_objects in l_list:
##        print(s_objects, "\n")

    engine = Engine(80)
    caboose = Caboose(70)
    print(caboose)
    print(type(l_list))

    if type(l_list) == "list":
        print("1")
    print(type(engine))
if "__main__" == __name__:
    main()
