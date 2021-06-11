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