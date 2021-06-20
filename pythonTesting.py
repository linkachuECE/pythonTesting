from DataStructureExamples import *
from random import randint, randrange
from functionBenchmarkComparison import *

def iterativeBinarySearchTest():
    list = ListToSearch([randint(0,9) for x in range(randint(3,10))])
    #print(list.binarySearch(5))

def recursiveBinarySearchTest():
    list = ListToSearch([randint(0,9) for x in range(randint(3,10))])
    #print(list.recursiveBinarySearch(5))

# print(timeit.timeit(iterativeBinarySearchTest, number=1000000))
# print(timeit.timeit(recursiveBinarySearchTest, number=1000000))

compareFunctions(10000, iterativeBinarySearchTest, recursiveBinarySearchTest)