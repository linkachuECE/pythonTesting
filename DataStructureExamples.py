class Stack:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items)-1]

	def size(self):
		return len(self.items)

class Queue:
	def __init__(self):
		self.items = []

	def isEmpty():
		return self.items == []

	def enqueue(self, items):
		self.items.insert(0,items)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

class Deque:
	def __init__(self):
		self.items = []
	
	def isEmpty(self):
		return self.items == []

	def addFront(self, item):
		self.items.insert(item)

	def addRear(self, item):
		self.items.insert(0, item)

	def removeFront(self):
		return self.items.pop()

	def removeRear(self):
		return self.items.pop(0)

	def size(self):
		return len(self.items)

class Node:
	def __init__(self, initdata):
		self.data = initdata
		self.next = None

	def getData(self):
		return self.data

	def getNext(self):
		return self.next
	
	def setData(self,newdata):
		self.data = newdata

	def setNext(self,newNext):
		self.next = newNext

class DoubleNode(Node):
	def __init__(self, initdata):
		super().__init__(initdata)
		self.back = None

	def getBack(self):
		return self.back

	def setBack(self, newdata):
		self.back = newData

class LinkedList:
	def __init__(self):
		self.head = Node(0)
		self.head.setNext(Node(None))

	def __str__(self):
		dataList = []
		current = self.head.getNext()
		for i in range(self.size()):
			dataList.append(current.getData())
			current = current.getNext()
		return "[" + ", ".join(str(num) for num in dataList) + "]"
	
	def isEmpty(self):
		return self.head.getData == 0

	def size(self):
		return self.head.getData()
	
	def search(self,item):
		current = self.head
		found = False
		while current != None and not found:
			if current.getData() == item:
				found = True
			else:
				current = current.getNext()
		return found

	def remove(self,item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == item:
				found = True
			elif current.getNext() == None:
				return False
			else:
				previous = current
				current = current.getNext()

		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())

	def index(self,item):
		if self.search(item):
			current = self.head.getNext()
			for i in range(self.size()):
				print("testing", current.getData(), "at index", i)
				if item == current.getData(): return i
				current = current.getNext()
		else: return -1

	def getFrontData(self):
		if self.head.getData() != 0:
			temp = self.head.getNext()
			return temp.getData()

	def pop(self, index=None):
		if index == None:
			index = self.size() - 1
		current = self.head.getNext()
		previous = None
		for i in range(index):
			previous = current
			current = current.getNext()

		value = current.getData()

		if previous != None:
			previous.setNext(current.getNext())
		else:
			self.head.setNext(current.getNext())

		self.head.setData(self.head.getData()-1)
		return value

	def slice(self, start=0, stop=None):
		copyList = []
		if stop == None:
			stop = self.size()
		current = self.head.getNext()

		for i in range(start):
			current = current.getNext()
		
		for j in range(stop - start):
			copyList.append(current.getData())
			current=current.getNext()

		return copyList

class UnorderedList(LinkedList):
	def __init__(self):
		super().__init__()

	def add(self,item):
		newNode = Node(item)
		newNode.setNext(self.head.getNext())
		self.head.setNext(newNode)
		self.head.setData(self.head.getData()+1)

	def append(self,item):
		current = self.head
		for i in range(self.size() + 1):
			current = current.getNext()
		current.setData(item)
		current.setNext(Node(None))
		self.head.setData(self.head.getData()+1)

	def insert(self, item, index=None):
		if index==None: 
			self.add(item)
			return
		newNode = Node(item)
		current = self.head.getNext()

		for i in range(index):
			previous = current
			current = current.getNext()

		previous.setNext(newNode)
		newNode.setNext(current)
		self.head.setData(self.head.getData()+1)

class OrderedList(LinkedList):
	def __init__(self):
		super().__init__()

	def search(self,item):
		current = self.head
		found = False
		stop = False
		while current != None and not found and not stop:
			if current.getData() == item:
				found = True
			else:
				if current.getData() > item:
					stop = True
				else:
					current = current.getNext()
		return found
	
	def add(self,item):
		current = self.head.getNext()

		if current.getData() == None:
			temp = Node(item)
			self.head.setNext(temp)
			temp.setNext(current)
			self.head.setData(self.head.getData() + 1)
			return

		previous = None
		stop = False

		while current.getData() != None and not stop:
			if current.getData() > item:
				stop = True
			else:
				previous = current
				current = current.getNext()

		temp = Node(item)
		temp.setNext(current)
		if previous == None:
			self.head.setNext(temp)
		else:
			previous.setNext(temp)

		self.head.setData(self.head.getData() + 1)

	def remove(self,item):
		current = self.head
		previous = None
		found = False
		while not found:
			if current.getData() == item:
				found = True
			elif current.next() == None:
				return False
			elif current.next() > item:
				return False
			else:
				previous = current
				current = current.getNext()

		if previous == None:
			self.head = current.getNext()
		else:
			previous.setNext(current.getNext())

class LinkedListQueue:
	def __init__(self):
		self.items = UnorderedList()

	def isEmpty():
		return self.items.isEmpty()

	def enqueue(self, item):
		self.items.add(item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return self.items.size()

class LinkedListStack:
	def __init__(self):
		self.items = UnorderedList()

	def isEmpty(self):
		return self.items.isEmpty()

	def push(self, item):
		self.items.add(item)

	def pop(self):
		return self.items.pop(0)

	def peek(self):
		return self.items.getFrontData()

	def size(self):
		return self.items.size()

class LinkedListDeque:
	def __init__(self):
		self.items = UnorderedList()
	
	def isEmpty(self):
		return self.items.isEmpty()

	def addFront(self, item):
		self.items.add(item)

	def addRear(self, item):
		self.items.append(item)

	def removeFront(self):
		return self.items.pop(0)

	def removeRear(self):
		return self.items.pop()

	def size(self):
		return self.items.size()

class HashTable:
	def __init__(self):
		self.size = 11
		self.slots = [None] * self.size
		self.data = [None] * self.size
	
	def put(self,key,data=None):
		hashvalue = self.hashfunction(key,len(self.slots))
		if data == None:
			data = key
		
		if self.slots[hashvalue] == None:
			self.slots[hashvalue] = key
			self.data[hashvalue] = data
		else:
			if self.slots[hashvalue] == key:
				self.data[hashvalue] = data
			else:
				nextslot = self.rehash(hashvalue,len(self.slots))
				while self.slots[nextslot] != None and self.slots[nextslot] != key:
					nextslot = self.rehash(nextslot, len(self.slots))
				
				if self.slots[nextslot] == None:
					self.slots[nextslot] = key
					self.data[nextslot] = data
					
	def hashfunction(self,key,size):
		if isinstance(key, str):
			totalOrd = 0
			for char in key:
				totalOrd += ord(char)
			return totalOrd%size
		else:
			return key%size
	
	def rehash(self,oldhash,size):
		return (oldhash+1)%size
	
	def get(self,key):
		startslot = self.hashfunction(key,len(self.slots))

		data = None
		stop = False
		found = False
		position = startslot
		while self.slots[position] != None and not found and not stop:
			if self.slots[position] == key:
				found = True
				data = self.data[position]
			else:
				position=self.rehash(position, len(self.slots))
				if position == startslot:
					stop = True
		return position
	
	def __getitem__(self,key):
		return self.get(key)
	
	def __setitem__(self,key,data):
		self.put(key,data)

def shortBubbleSort(alist):
	exchanges = True
	passnum = len(alist)-1
	while passnum > 0 and exchanges:
		exchanges = False
		for i in range(passnum):
			if alist[i]>alist[i+1]:
				exchanges = True
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp
		passnum = passnum-1
	return alist

def selectionSort(alist):
	for fillslot in range(len(alist)-1,0,-1):
		positionOfMax=0
		for location in range(1,fillslot+1):
			if alist[location]>alist[positionOfMax]:
				positionOfMax = location

		temp = alist[fillslot]
		alist[fillslot] = alist[positionOfMax]
		alist[positionOfMax] = temp
	return alist

def insertionSort(alist):
	for index in range(1,len(alist)):
		currentvalue = alist[index]
		position = index

		while position>0 and alist[position-1]>currentvalue:
			alist[position]=alist[position-1]
			position = position-1

		alist[position]=currentvalue
	return alist

def shellSort(alist):
	sublistcount = len(alist)//2
	while sublistcount > 0:

		for startposition in range(sublistcount):
			gapInsertionSort(alist,startposition,sublistcount)

		print("After increments of size",sublistcount,"The list is",alist)

		sublistcount = sublistcount // 2
	return alist

def gapInsertionSort(alist,start,gap):
	for i in range(start+gap,len(alist),gap):

		currentvalue = alist[i]
		position = i

		while position>=gap and alist[position-gap]>currentvalue:
			alist[position]=alist[position-gap]
			position = position-gap

		alist[position]=currentvalue

def mergeSort(alist):
	print("Splitting ",alist)
	if len(alist)>1:
		mid = len(alist)//2
		lefthalf = alist[:mid]
		righthalf = alist[mid:]

		mergeSort(lefthalf)
		mergeSort(righthalf)

		i=0
		j=0
		k=0
		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] <= righthalf[j]:
				alist[k]=lefthalf[i]
				i=i+1
			else:
				alist[k]=righthalf[j]
				j=j+1
			k=k+1

		while i < len(lefthalf):
			alist[k]=lefthalf[i]
			i=i+1	
			k=k+1

		while j < len(righthalf):
			alist[k]=righthalf[j]
			j=j+1
			k=k+1
	print("Merging ",alist)

def quickSort(alist):
	quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
	if first<last:

		splitpoint = partition(alist,first,last)

		quickSortHelper(alist,first,splitpoint-1)
		quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
	pivotvalue = alist[first]

	leftmark = first+1
	rightmark = last

	done = False
	while not done:

		while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
			leftmark = leftmark + 1

		while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
			rightmark = rightmark -1

		if rightmark < leftmark:
			done = True
		else:
			temp = alist[leftmark]
			alist[leftmark] = alist[rightmark]
			alist[rightmark] = temp

	temp = alist[first]
	alist[first] = alist[rightmark]
	alist[rightmark] = temp

	return rightmark

