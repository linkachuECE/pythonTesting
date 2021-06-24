from typing import List
from DataStructureExamples import *
from functionBenchmarkComparison import *
import random

mytree = BinaryTree("language")

mytree.insertLeft("compiled")
mytree.getLeftChild().insertLeft("C")
mytree.getLeftChild().insertRight("Java")
mytree.insertRight("interpreted")
mytree.getRightChild().insertLeft("Python")
mytree.getRightChild().insertRight("Scheme")