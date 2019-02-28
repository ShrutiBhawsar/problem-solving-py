# 1. Write a Class Painting with method calculatePaintingCost.
# Write a Class FlatPainting with noOfRooms which is inheritated from Class Painting.
# Override calculatePaintingCost.(Assume per room painting cost is 10000)
# Write a Class BulidingPainting with noOfFlats which is inheritated from Class Painting.
# Override calculatePaintingCost.(Assume per room painting cost is 25000)
# Write main() method to accpet painting assignment with option 1.Flat 2.Building and then
# calculate the cost according to the type.



class Painting:
    def __init__(self, cost = 0):
        self._cost = cost



    def calculatePaintingCost(self):
        # self._cost =  self._room * 1000
        pass

    def printCost(self):
        # return 'Painting cost for {} room is {}'.format(self._room, self._cost)
        pass


class FlatPainting(Painting):

    def __init__(self, room, cost=0):
        Painting.__init__(self, cost)
        self._room = room


    def calculatePaintingCost(self):
        self._cost =  int(self._room) * 10000
        print(' Painting cost for {} room is {}'.format(self._room, self._cost))



class BuildingPainting(Painting):

    def __init__(self, flat, cost=0):
        Painting.__init__(self, cost)
        self._flat = flat

    def calculatePaintingCost(self):
        self._cost = int (self._flat) * 25000
        print(' Painting cost for {} flat is {}'.format(self._flat, self._cost))


def main_function():
    input_option = input(" Enter the option   1.Flat     2.Building : ")
    if input_option == '1':
        print(" ................Flat Painting Cost..................... ")
        input_room = input(" Enter the no of rooms : ")
        f1 = FlatPainting(input_room)
        f1.calculatePaintingCost()
    elif input_option == '2':
        print(" ................Building Painting Cost.................. ")
        input_flat = input(" Enter the no of flats : ")
        b1 = FlatPainting(input_flat)
        b1.calculatePaintingCost()
    else:
        print(" You have entered the wrong option !!!!!")

main_function()










