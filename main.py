from index import Attendance
import numpy as np


if __name__ == "__main__":

    # read input from the list
    inputs = [5, 10]
    for n in inputs:
        obj = Attendance(n)
        obj.printSolution()

    # read from input file
    data = np.loadtxt('input.txt', dtype=int)
    for n in data:
        obj = Attendance(n)
        obj.printSolution()
        
