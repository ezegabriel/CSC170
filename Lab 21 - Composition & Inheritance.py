'''
Gabriel Eze
CSC 170 - b
Lab - 21
Lab Partner - Vedant
A lab that inherits from the TrainCar parent.
'''

from TrainCar import * # Import from TrainCar.py file

class FreightTrain:
    # Constructor
    def __init__(self, engine, caboose):
        self.engine = engine
        self.caboose = caboose
        engine.next = caboose
        caboose.previous = engine
        self.number_cars = 0

    def add_car(self, new_car):
        self.caboose.previous.next = new_car
        new_car.previous = self.caboose.previous
        new_car.next = self.caboose
        self.caboose.previous = new_car
        self.number_cars += 1

    # Getter
    def get_number_cars(self):
        return self.number_cars

    def get_total_length(self):
        '''Returns the total length in feet of all cars including engine and caboose.'''
        total = 0
        car = self.engine
        while not(car is None):
            total += car.get_length()
            car = car.next
        return total
    
    def print_train(self):
        '''prints all cars to the console.'''
        car = self.engine
        while not (car is None):
            print(car)
            car = car.next
    


def main():
    engine = Engine(80)
    caboose = Caboose(70)
    
    train = FreightTrain(engine, caboose)

    dining = TrainCar("brown", "Dining car", 100)
    hopper = TrainCar("black", "hopper", 60)
    train.add_car(hopper)
    train.add_car(dining)
    
    train.print_train()

    print("Number of cars:", train.get_number_cars())
    print("Total length:", train.get_total_length())

if "__main__" == __name__:
    main()
