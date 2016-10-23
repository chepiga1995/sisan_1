__author__ = 'craig'

import re
from numpy import *

class DataContainer:
    def __init__(self, inputfile, Dim_x1, Dim_x2, Dim_x3, Dim_y, selection_range):
        self.ERROR = False
        self.data_x1 = []
        self.data_x2 = []
        self.data_x3 = []
        self.data_y = []
        self.parse(inputfile, Dim_x1, Dim_x2, Dim_x3, Dim_y, selection_range)

    def parse(self, inputfile, Dim_x1, Dim_x2, Dim_x3, Dim_y, selection_range):
        f = open(inputfile, "r")
        buff = []
        for i in range(0, selection_range):
            line = f.readline()
            if line == "":
                print("Your input file have empty line")
                self.ERROR = True
                return 0
            spelling = re.split('\t|\s*', line.replace(',', '.'))
            spelling = filter(lambda s: len(s) > 0, spelling)
            line = list(map(float, spelling))
            buff.append(line)

        buff = list(map(list, zip(*buff)))
        # read X1
        buff1 = array(buff)
        if buff1.shape[0] < Dim_x1+Dim_x2+Dim_x3+Dim_y:
            print("Your input file don't have enough colomns")
            self.ERROR = True
            return 0
        for i in range(0, Dim_x1):
            self.data_x1.append(self.normalize(buff[i]))
        for i in range(0, Dim_x2):
            self.data_x2.append(self.normalize(buff[Dim_x1+i]))
        for i in range(0, Dim_x3):
            self.data_x3.append(self.normalize(buff[Dim_x1+Dim_x2+i]))
        for i in range(0, Dim_y):
            self.data_y.append(self.normalize(buff[Dim_x1+Dim_x2+Dim_x3+i]))

        self.data_x1 = list(map(list, zip(*self.data_x1)))
        self.data_x2 = list(map(list, zip(*self.data_x2)))
        self.data_x3 = list(map(list, zip(*self.data_x3)))
        self.data_y = list(map(list, zip(*self.data_y)))

    def normalize(self, lst):
        v_max = max(lst)
        v_min = min(lst)
        return list(map(lambda x: (x - v_min) / (v_max - v_min), lst))

