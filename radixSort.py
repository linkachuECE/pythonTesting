from DataStructureExamples import Queue

def radixSort(numList):
	maxDigitLength = 0
	numStringList = [str(num) for num in numList]
	resultString = ""

	mainBin = Queue()
	digitBinList = []

	for i in range(10):
		digitBinList.append(Queue())

	for num in numStringList:
		if len(num) > maxDigitLength:
			maxDigitLength = len(num)
		mainBin.enqueue(num)	

	for place in range(maxDigitLength):
		for i in range(mainBin.size()):
			temp = mainBin.dequeue()
			if len(temp) <= place:
				digitBinList[0].enqueue(temp)
				print("enqueing {} to bin 0".format(temp))
			else:
				value = int(temp[-place - 1])
				digitBinList[value].enqueue(temp)
				print("enqueuing {} to bin {}".format(temp, value))
		
		for digitBinIndex in range(len(digitBinList)):
			for number in range(digitBinList[digitBinIndex].size()):
				temp = digitBinList[digitBinIndex].dequeue()
				mainBin.enqueue(temp)
				print("enqueueing {} to main bin from digitBin {}".format(temp, digitBinIndex))

	for i in range(mainBin.size()):
		resultString += mainBin.dequeue()
		resultString += " "

	return resultString

print(radixSort([1, 45, 789, 3, 90182, 78, 982, 7]))