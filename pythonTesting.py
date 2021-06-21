from DataStructureExamples import *
from functionBenchmarkComparison import *
import random

testHash = HashTable()
for i in range(testHash.size):
    testHash[i] = random.randint(0,20)

testHash[300] = 15
print(testHash[300])
