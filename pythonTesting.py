from typing import List
from DataStructureExamples import *
from functionBenchmarkComparison import *
import random
import 

mytree = BinMaxHeap()
testList = []
for i in range(0,31):
    testList.append(random.randint(0,100))

mytree.buildHeap(testList)
print(mytree)