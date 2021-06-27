from typing import List
from DataStructureExamples import *
from functionBenchmarkComparison import *
import random

mytree = BinarySearchTree()
mytree[25] = 25
mytree[15] = 15
mytree[10] = 10
mytree[20] = 20
mytree[40] = 40
mytree[35] = 35
mytree[50] = 50

mytree.postOrderTraversal()