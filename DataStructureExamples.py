from typing import SupportsFloat


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
				#print("testing", current.getData(), "at index", i)
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
	def __init__(self,size=11):
		self.size = size
		self.slots = [None] * self.size
		self.data = [None] * self.size
	
	def __len__(self):
		return self.size
	
	def __contains__(self, key):
		if isinstance(self.get(key), int):
			return True
		else:
			return False
	
	def __delitem__(self, key):
		position = self.linearProbe(self.hashfunction(key), key)
		if position == None:
			print("No item at that index")
		else:
			self.slots[position] = None
			self.data[position] = None
	
	def put(self,key,data=None):
		hashvalue = self.linearProbe(self.hashfunction(key))

		if hashvalue == None:
			self.size = self.size + 1
			self.slots.append(key)
			self.data.append(data)
		else:
			self.slots[hashvalue] = key
			self.data[hashvalue] = data
	
	def linearProbe(self, slot, key=None, firstProbe=None):
		if firstProbe == None:
			firstProbe = slot
			if self.slots[slot] == key:
				return slot
		
		nextSlot = self.rehash(slot)

		if self.slots[nextSlot] == key:
			return nextSlot
		elif nextSlot == firstProbe:
			return None
		elif self.slots[nextSlot] == len(self.slots):
			return self.linearProbe(0, key, firstProbe)
		else:
			return self.linearProbe(nextSlot, key, firstProbe)
					
	def hashfunction(self,key):
		if isinstance(key, str):
			totalOrd = 0
			for char in key:
				totalOrd += ord(char)
			return totalOrd%self.size
		else:
			return key%self.size
	
	def rehash(self,oldhash):
		return (oldhash+1)%len(self.slots)
	
	def get(self,key):

		position = self.linearProbe(self.hashfunction(key),key)
		if position == None:
			return "Item not found"
		else:
			return self.data[position]
	
	def __getitem__(self,key):
		return self.get(key)
	
	def __setitem__(self,key,data):
		self.put(key,data)

class ListToSort:

	def __init__(self, list):
		self.list = list
		self.isString = False
		self.checkForString()
	
	def checkForString(self):
		if isinstance(self.list, str):
			self.ordinalStringList()
			self.isString = True

	def shortBubbleSort(self):
		exchanges = True
		passnum = len(self.list)-1
		while passnum > 0 and exchanges:
			exchanges = False
			for i in range(passnum):
				if self.list[i]>self.list[i+1]:
					exchanges = True
					self.list[i], self.list[i+1] = self.list[i+1], self.list[i]
			passnum = passnum-1
		
		return self.returnFinalList()
	
	def doubleBubbleSort(self,searchDirection=1):
		exchanges = False
		if searchDirection > 0:
			for i in range(len(self.list)-1):
				if self.list[i]>self.list[i+1]:
					exchanges = True
					self.list[i], self.list[i+1] = self.list[i+1], self.list[i]
			if exchanges:
				self.doubleBubbleSort(-1)
		else:
			for i in range(-1, -len(self.list), -1):
				if self.list[i]<self.list[i-1]:
					exchanges = True
					self.list[i], self.list[i-1] = self.list[i-1], self.list[i]
			if exchanges:
				self.doubleBubbleSort(1)

	def selectionSort(self):
		for fillslot in range(len(self.list)-1,0,-1):
			positionOfMax=0
			for location in range(1,fillslot+1):
				if self.list[location]>self.list[positionOfMax]:
					positionOfMax = location

			self.list[fillslot], self.list[positionOfMax] = \
				self.list[positionOfMax], self.list[fillslot]

		return self.returnFinalList()

	def insertionSort(self):
		for index in range(1,len(self.list)):
			currentvalue = self.list[index]
			position = index

			while position>0 and self.list[position-1]>currentvalue:
				self.list[position]=self.list[position-1]
				position = position-1

			self.list[position]=currentvalue
		
		return self.returnFinalList()

	def shellSort(self):
		sublistcount = len(self.list)//2
		while sublistcount > 0:

			for startposition in range(sublistcount):
				self.gapInsertionSort(startposition,sublistcount)

			#print("After increments of size",sublistcount,"The list is",self.list)

			sublistcount = sublistcount // 2

		return self.returnFinalList()

	def gapInsertionSort(self,start,gap):
		for i in range(start+gap,len(self.list),gap):

			currentvalue = self.list[i]
			position = i

			while position>=gap and self.list[position-gap]>currentvalue:
				self.list[position]=self.list[position-gap]
				position = position-gap

			self.list[position]=currentvalue

	def mergeSort(self, blist=None):
		if blist == None:
			alist = self.list
		else:
			alist = blist

		if len(alist)>1:
			#print("Splitting ",alist)
			mid = len(alist)//2
			lefthalf = alist[:mid]
			righthalf = alist[mid:]

			self.mergeSort(lefthalf)
			self.mergeSort(righthalf)

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
			#print("Merging ",alist)
		
		if len(alist) == len(self.list):
			self.list = alist
			return self.returnFinalList()

	def quickSort(self):
		if len(self.list) > 5:
			self.quickSortHelper(self.list,0,len(self.list)-1)
			return self.returnFinalList()
		else:
			return self.selectionSort()

	def quickSortHelper(self,alist,first,last):
		if first<last:

			splitpoint = self.partition(alist,first,last)

			self.quickSortHelper(alist,first,splitpoint-1)
			self.quickSortHelper(alist,splitpoint+1,last)

		if last == len(self.list)-1:
			self.list = alist

	def partition(self,alist,first,last):
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

	def ordinalStringList(self):
		noSpace = self.list.replace(" ", "")
		stringList = [ord(letter) for letter in noSpace]
		self.list = stringList

	def returnFinalList(self):
		if self.isString:
			return "".join([chr(uni) for uni in self.list])
		else:
			return self.list

class ListToSearch(ListToSort):

	def __init__(self, list):
		super().__init__(list)
		self.found = False
		self.pos = None
		self.item = None
	
	def __str__(self):
		if self.found:
			return "{} found at position {}".format(self.item, self.pos)
		else:
			return "Item not found"
	
	def sequentialSearch(self, item):
		self.item = item
		pos = 0

		while pos < len(self.list) and not self.found:
			if self.list[pos] == item:
				self.found = True
			else:
				pos = pos+1
		
		if self.found:
			self.pos = pos

		return self.__str__()

	def iterativeBinarySearch(self, item):
		self.mergeSort(self.list)
		#print("Sorted the list:", self.list)
		self.item = item

		first = 0
		last = len(self.list)-1
		midpoint = None
		self.found = False

		while first <=last and not self.found:
			midpoint = (first + last)//2
			if self.list[midpoint] == self.item:
				self.found = True
			else:
				if self.item < self.list[midpoint]:
					last = midpoint - 1
				else:
					first = midpoint + 1
		self.pos = midpoint

		return self.__str__()
	
	def recursiveBinarySearch(self, item, alist=None, posOfMidPoint=None):
		if alist == None:
			self.mergeSort(self.list)
			#print("Sorted the list:", self.list)
			alist = self.list
			posOfMidPoint = len(alist)//2
			self.item = item
		
		if len(alist) == 0:
			return self.__str__()
		else: 
			midpoint = len(alist)//2
			if alist[midpoint]==item:
				self.pos = posOfMidPoint
				self.found = True
				return self.__str__()
			else:
				if item<alist[midpoint]:
					return self.recursiveBinarySearch(item, alist[:midpoint],
					(posOfMidPoint - midpoint//2)-1)
				else:
					return self.recursiveBinarySearch(item, alist[midpoint+1:],
					(posOfMidPoint + midpoint//2 + 1))

class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

class BinHeap:
	def __init__(self):
		self.heapList = [0]
		self.currentSize = 0
	
	def percUp(self,i):
		while i // 2 > 0:
			if self.heapList[i] < self.heapList[i//2]:
				tmp = self.heapList[i//2]
				self.heapList[i//2] = self.heapList[i]
				self.heapList[i] = tmp
			i = i//2
	
	def insert(self,k):
		self.heapList.append(k)
		self.currentSize = self.currentSize + 1
		self.percUp(self.currentSize)
	
	def percDown(self,i):
		while (i * 2) <= self.currentSize:
			mc = self.minChild(i)
			if self.heapList[i] > self.heapList[mc]:
				tmp = self.heapList[i]
				self.heapList[i] = self.heapList[mc]
			i = mc
	
	def minChild(self,i):
		if i * 2 + 1 > self.currentSize:
			return i * 2
		else:
			if self.heapList[i*2] < self.heapList[i*2+1]:
				return i * 2
			else:
				if self.heapList[i*2] < self.heapList[i*2+1]:
					return i * 2
				else:
					return i * 2 + 1
	
	def delMin(self):
		retval = self.heapList[1]
		self.heapList[1] = self.heapList[self.currentSize]
		self.currentSize = self.currentSize - 1
		self.heapList.pop()
		self.percDown(1)
		return retval
	
	def buildHeap(self,alist):
		i = len(alist) // 2
		self.currentSize = len(alist)
		self.heapList = [0] + alist[:]
		while (i > 0):
			self.percDown(i)
			i = i - 1
	
	def remove(self,currentNode):
		if currentNode.isLeaf():
			if currentNode == currentNode.parent.leftChild:
				currentNode.parent.leftChild = None
			else:
				currentNode.parent.rightChild = None
		elif currentNode.hasBothChildren():
			succ = currentNode.findSuccessor()
			succ.spliceOut()
			currentNode.key = succ.key
			currentNode.payload = succ.payload
		else:
			if currentNode.hasLeftChild():
				if currentNode.isLeftChild():
					currentNode.leftChild.parent = currentNode.parent
					currentNode.parent.leftChild = currentNode.leftChild
				elif currentNode.isRightChild():
					currentNode.leftChild.parent = currentNode.parent
					currentNode.parent.rightChild = currentNode.leftChild
				else:
					currentNode.replaceNodeData(currentNode.leftChild.key,
											currentNode.leftChild.payload,
											currentNode.leftChild.leftChild,
											currentNode.leftChild.rightChild)
			else:
				if currentNode.isLeftChild():
					currentNode.rightChild.parent = currentNode.parent
					currentNode.parent.leftChild = currentNode.rightChild
				elif currentNode.isRightChild():
					currentNode.rightChild.parent = currentNode.parent
					currentNode.parent.rightchild = currentNode.rightChild
				else:
					currentNode.replaceNodeData(currentNode.rightChild.key,
												currentNode.rightChild.payload,
												currentNode.rightChild.leftChild,
												currentNode.rightChild.rightChild)

class BinarySearchTree:

	def __init__(self):
		self.root = None
		self.size = 0
	
	def length(self):
		return self.size
	
	def __len__(self):
		return self.size
	
	def __iter__(self):
		return self.root.__iter__()

	def __setitem__(self,k,v):
		self.put(k,v)
	
	def __getitem__(self,key):
		return self.get(key)
	
	def __contains__(self,key):
		if self._get(key,self.root):
			return True
		else:
			return False
	
	def put(self,key,val):
		if self.root:
			self._put(key,val,self.root)
		else:
			self.root = TreeNode(key,val)
		self.size = self.size + 1
	
	def _put(self,key,val,currentNode):
		if key < currentNode.key:
			if currentNode.hasLeftChild():
				self._put(key,val,currentNode.leftChild)
			else:
				currentNode.leftChild = \
					TreeNode(key,val,parent=currentNode)
		else:
			if currentNode.hasRightChild():
				self._put(key,val,currentNode.rightChild)
			else:
				currentNode.rightChild = \
					TreeNode(key,val,parent=currentNode)
	
	def get(self,key):
		if self.root:
			res = self._get(key,self.root)
			if res:
				return res.payload
			else: 
				return None
		else:
			return None
	
	def _get(self,key,currentNode):
		if not currentNode:
			return None
		elif currentNode.key == key:
			return currentNode
		elif key < currentNode.key:
			return self._get(key,currentNode.leftChild)
		else:
			return self._get(key,currentNode.rightChild)
	
	def delete(self,key):
		if self.size > 1:
			nodeToRemove = self._get(key,self.root)
			if nodeToRemove:
				self.remove(nodeToRemove)
				self.size = self.size-1
			else:
				raise KeyError('Error, key not in tree')
		elif self.size == 1 and self.root.key == key:
			self.root = None
			self.size = self.size - 1
		else:
			raise KeyError('Error, key not in tree')
	
	def __delitem__(self,key):
		self.delete(key)

class TreeNode:
	def __init__(self,key,val,left=None,right=None,parent=None):
		self.key = key
		self.payload = val
		self.leftChild = left
		self.rightChild = right
		self.parent = parent
	
	def hasLeftChild(self):
		return self.leftChild

	def hasRightChild(self):
		return self.rightChild
	
	def isLeftChild(self):
		return self.parent and self.parent.leftChild == self
	
	def isRightChild(self):
		return self.parent and self.parent.rightChild == self
	
	def isRoot(self):
		return not self.parent
	
	def isLeaf(self):
		return not (self.rightChild or self.leftChild)
	
	def hasAnyChildren(self):
		return self.rightChild or self.leftChild
	
	def hasBothChildren(self):
		return self.leftChild and self.rightChild
	
	def spliceOut(self):
		if self.isLeaf():
			if self.isLeftChild():
				self.parent.leftChild = None
			else:
				self.parent.rightChild = None
		elif self.hasAnyChildren():
			if self.hasLeftChild():
				if self.isLeftChild():
					self.parent.leftChild = self.leftChild
				else:
					self.parent.rightChild = self.leftChild
				self.leftChild.parent = self.parent
			else:
				if self.isLeftChild():
					self.parent.leftchild = self.rightChild
				else:
					self.parent.rightChild = self.rightChild
				self.rightChild.parent = self.parent
	
	def findSuccessor(self):
		succ = None
		if self.hasRightChild():
			succ = self.rightChild.findMin()
		else:
			if self.parent:
				if self.parent:
					if self.isLeftChild():
						succ = self.parent
					else:
						self.parent.rightChild = None
						succ = self.parent.findSuccessor()
						self.parent.rightChild = self
		return succ
	
	def findMin(self):
		current = self
		while current.hasLeftChild():
			current = current.leftChild
		return current
	
	def replaceNodeData(self,key,value,lc,rc):
		self.key = key
		self.payload = value
		self.leftChild = lc
		self.rightChild = rc
		if self.hasLeftChild():
			self.leftChild.parent = self
		if self.hasRightChild.parent:
			self.rightChild.parent = self
