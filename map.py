# a grid map used for path planning
import random

class Map:

    map = []

    def __init__(self,size):
        self.map = [[0 for x in range(size)] for y in range(size)]
        self.setStart()
        self.setGoal()
        print(self.map)

    def setStart(self):
        self.map[1][1] = 'S'

    def setGoal(self):
        self.map[7][7] = 'G'
    