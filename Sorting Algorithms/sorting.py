import pygame
import random
import math
import copy
import time
import sys
import resource

class recursionlimit:
 	 def __init__(self, limit):
 	 	 	 self.limit = limit
 	 	 	 self.old_limit = sys.getrecursionlimit()

 	 def __enter__(self):
 	 	 	 sys.setrecursionlimit(self.limit)

 	 def __exit__(self, type, value, tb):
 	 	 	 sys.setrecursionlimit(self.old_limit)

width = 800

height = 600


screen = pygame.display.set_mode((width, height))



toBeSorted = []

BLACK = (0, 0, 0)

RED = (255, 0, 0)

WHITE = (255, 255, 255)

GREEN = (0, 255, 0)



class object:
	def __init__(self, totalPieces):


		self.width = round(height/totalPieces)
		self.height = random.randint(0, height)
		self.y = height - self.height
		self.x = len(toBeSorted) * self.width
		self.sorted = False
		self.color = RED if self.sorted else WHITE

		toBeSorted.append(self)


	def draw(self):
		pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))


	def __int__(self):
		return self.height


def selectionSort(lst, objectUsage = False, visualize = False):
	for numDone in range(len(lst)):




		curMin = lst[numDone]
		curMinInd = numDone
		for index, num in enumerate(lst[numDone + 1:]):

			if int(curMin) > int(num):
				curMin = int(num)
				curMinInd = index + numDone + 1



		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()


		lst[numDone], lst[curMinInd] = lst[curMinInd], lst[numDone]



		if objectUsage:

			lst[numDone].x = numDone * lst[numDone].width

			lst[curMinInd].x = curMinInd * lst[curMinInd].width

			lst[curMinInd].color, lst[numDone].color = RED, RED



			if visualize:

				screen.fill(BLACK)

				for piece in lst:
					piece.draw()

				pygame.display.update()

				lst[curMinInd].color, lst[numDone].color = WHITE, GREEN





	return lst


def bubbleSort(lst, objectUsage = False, visualize = False):
	for k in range(len(lst) - 1):
		changed = False
		for i in range(len(lst) - 1 - k):

			screen.fill(BLACK)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()

			if int(lst[i]) > int(lst[i + 1]):
				changed = True
				lst[i], lst[i + 1] = lst[i + 1], lst[i]

				if objectUsage:
					lst[i].x, lst[i + 1].x = lst[i + 1].x, lst[i].x

					if visualize:
						lst[i].color = RED
						lst[i + 1].color = RED

					
				

			if visualize:
				for piece in toBeSorted:
					piece.draw()


				pygame.display.update()

				if int(lst[i]) > int(lst[i + 1]):

					lst[i].color, lst[i + 1].color = GREEN, WHITE

				else:
					lst[i].color, lst[i + 1].color = WHITE, GREEN


		if not changed:
			break


	return lst


def insertionSort(lst, objectUsage = False, visualize = False):

	for i in range(len(lst)):
		curVal = lst[i]
		hole = i

		while hole > 0 and int(lst[hole - 1]) > int(curVal):
			screen.fill(BLACK)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()




			lst[hole] = lst[hole - 1]

			if objectUsage:

				lst[hole - 1].x += lst[hole].width

				if visualize:
					lst[hole - 1].color, lst[hole].color = GREEN, GREEN


					for j in lst:
						j.draw()

					pygame.display.update()



					lst[hole - 1].color, lst[hole].color = WHITE, RED




			hole -= 1


		lst[hole] = curVal

		if objectUsage:
			lst[hole].x = hole * lst[hole].width
			lst[hole].color = RED

	return lst

# Binary Insertion Sort (More efficient than normal insertion sort)

def binarySearch(array, startPos, endPos, element):
 	
 	while True:

 	 	curGuess = math.floor((startPos + endPos)/2)

 	 	if array[curGuess] == element:
 	 	 	return curGuess
 	 	
 	 	elif element > array[curGuess]:
 	 	 	startPos = curGuess + 1

 	 	 	if startPos >= endPos:
 	 	 	 	return curGuess + 1

 	 	else:
 	 	 	endPos = curGuess - 1

 	 	 	if startPos >= endPos:
 	 	 	 	return curGuess


def binaryInsertionSort(array, startPos = 0, endInd = True):
 	if endInd:
 	 	endInd = len(array)

 	for i in range(startPos, len(array) - (len(array) - endInd)):
 	 	
 	 	curElement = array.pop(i)
 	 	array.insert(binarySearch(array, 0, startPos, curElement), curElement)
 	 	startPos += 1


 	return array


# Merge Sort

def merge(l, r, lst, leftOffset, rightOffset, fullLst = None, objectUsage = False, visualize = False):
	i = 0
	j = 0
	k = 0
	while i < len(l) and j < len(r):
		screen.fill(BLACK)
		if int(l[i]) < int(r[j]):
			lst[k] = l[i]
			if objectUsage:
				l[i].x = (k * l[i].width)# + leftOffset

			i += 1


		else:
			lst[k] = r[j]
			if objectUsage:
				r[j].x = (k * r[j].width)# + rightOffset

			j += 1

		k += 1

		if visualize and objectUsage:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					exit()


			for bar in fullLst:
				bar.draw()


			pygame.display.update()









	while i < len(l):
		screen.fill(BLACK)
		lst[k] = l[i]

		k += 1

		if objectUsage:
			l[i].x = (k * l[i].width)# + leftOffset


			if visualize:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						exit()

				for bar in fullLst:
					bar.draw()



				pygame.display.update()



		i += 1

		




	while j < len(r):
		screen.fill(BLACK)
		lst[k] = r[j]

		k += 1

		if objectUsage:
			r[j].x = (k * r[j].width)# + rightOffset


			if visualize:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						exit()


				for bar in fullLst:
					bar.draw()



				pygame.display.update()

				# fullLst[k - 1 + offset].color = WHITE


		j += 1

		
	for i in fullLst:
		i.color = WHITE

	return lst


def mergeSort(lst, main = True, offset = 0, objectUsage = False, visualize = False):
	n = len(lst)

	if main:
		global fullLst
		fullLst = lst.copy()

		

	if n == 1:
		return lst

	left = lst[:round(n/2)]

	right = lst[round(n/2):]

	left = mergeSort(left, main = False, offset = offset, objectUsage = objectUsage, visualize = visualize)

	right = mergeSort(right, main = False, offset = round(n/2) + offset, objectUsage = objectUsage, visualize = visualize)

	lst = merge(left, right, lst, offset, offset + round(n/2), fullLst = fullLst, objectUsage = objectUsage, visualize = visualize)

	if visualize:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()

		for i in fullLst:

			i.draw()

		pygame.display.update()


	return lst

# Heap Sort
def findChildrenSwap(array, index, maxHeap = True, numSorted = 0):
	childrenInd = []
	if (index + 1) * 2 - 1 < len(array) - numSorted:
		childrenInd.append((index + 1) * 2 - 1)
	if ((index + 1) * 2) < len(array) - numSorted:
		childrenInd.append(((index + 1) * 2))

	if len(childrenInd) > 0:
		curHighInd = childrenInd[0]

		for i in childrenInd[1:]:
			if (int(array[i]) > int(array[curHighInd]) and maxHeap) or (int(array[i]) < int(array[curHighInd]) and not maxHeap):
				curHighInd = i

		if (int(array[curHighInd]) > int(array[index]) and maxHeap) or (int(array[curHighInd]) < int(array[index]) and not maxHeap):
			array[curHighInd], array[index] = array[index], array[curHighInd]

			findChildrenSwap(array, curHighInd, maxHeap = maxHeap, numSorted = numSorted)




def heapify(array, maxHeap = True):
	for index in range(len(array) - 1, -1, -1):

		findChildrenSwap(array, index, maxHeap = maxHeap)


	return array


def deleteHeap(heap, maxHeap = True, numSorted = 0):
	curMax = heap[0]

	last = heap.pop(-(numSorted + 1))

	heap.append(curMax)

	heap[0] = last

	findChildrenSwap(heap, 0, maxHeap = maxHeap, numSorted = numSorted + 1)

	return heap

def heapSort(array, maxHeap = True, objectUsage = False, visualize = False):
	array = heapify(array, maxHeap = maxHeap)

	for i in range(len(array) - 2):

		array = deleteHeap(array, maxHeap = maxHeap, numSorted = i)

		if objectUsage:
			array[-1].x = array[-1].width * i

	array.append(array.pop(0))
	array.append(array.pop(0))

	return array


# Counting Sort

def countingSort(array, objectUsage = False, visualize = False, exp = 1, maxData = True, minData = True, start = 0):
	if maxData or minData:

		minData = array[0]
		maxData = array[0]

		for i in array[1:]:
			if int(i) < int(minData):
				minData = i

			elif int(i) > int(maxData):
				maxData = i

	rangeOfElements = int(maxData) - int(minData) + 1

	count_arr = [0 for _ in range(rangeOfElements)] 
	output_arr = [0 for _ in range(len(array))]

	for i in range(len(array)):
		count_arr[math.floor(int(float(str(math.floor((int(array[i]) - int(minData))/exp))[start: ])))] += 1

	for i in range(1, len(count_arr)):
		count_arr[i] += count_arr[i - 1]

	for i in range(len(array) - 1, -1, -1):
		output_arr[count_arr[int(float(str(math.floor((int(array[i]) - int(minData))/exp))[start: ]))] - 1] = array[i]
		if objectUsage:
			array[i].x = count_arr[int(float(str(math.floor((int(array[i]) - int(minData))/exp))[start: ]))] * array[i].width
		
		count_arr[int(float(str(math.floor((int(array[i]) - int(minData))/exp))[start: ]))] -= 1


	return output_arr


def radixSortLSD(array, objectUsage = False, visualize = False):
	maxData = array[1]


	for i in array[1:]:
		if int(i) > int(maxData):
			maxData = i

	exp = 1

	while int(maxData)/int(exp) >= 1:
		array = countingSort(array, objectUsage = objectUsage, visualize = visualize, exp = exp, maxData = 9, minData = 0, start = -1)
		exp *= 10

	return array


def countingSortMSD(array, objectUsage = False, visualize = False, exp = 1, maxData = True, minData = True, start = 0, begin = 0, end = None):
	sections = {}
	if maxData or minData:

		minData = array[begin]
		maxData = array[begin]

		for i in array[begin:end]:
			if int(i) < int(minData):
				minData = i

			elif int(i) > int(maxData):
				maxData = i

	rangeOfElements = int(maxData) - int(minData) + 1

	count_arr = [0 for _ in range(rangeOfElements)]
	output_arr = [0 for _ in range(len(array))]

	if end != None:
		output_arr = [] 
		for i in range(begin):
			output_arr.append(array[i])

		for i in range(end - begin + 1):
			output_arr.append(0)

		for i in range(len(array) - (end + 1 if end != None else len(array))):
			output_arr.append(array[i + end + 1])



	for i in range(end - begin if end != None else len(array)):
		count_arr[math.floor(int(float(str(math.floor((int(array[begin + i]) - int(minData))/exp))[start: ])))] += 1
	for i in range(1, len(count_arr)):
		count_arr[i] += count_arr[i - 1]

	for i in range(((end - begin) if end != None else len(array)) - 1, -1, -1):
		curIndex = int(float(str(math.floor((int(array[begin + i]) - int(minData))/exp))[start: ]))
		output_arr[count_arr[curIndex] - 1] = array[begin + i]
		if objectUsage:
			array[begin + i].x = count_arr[curIndex] * array[begin + i].width

		if curIndex not in sections.keys():
			sections[curIndex] = [count_arr[curIndex] - minData, count_arr[curIndex] - minData]

		else:
			sections[curIndex][0] = count_arr[curIndex] - minData
		
		count_arr[curIndex] -= 1


	return output_arr, sections

def radixSortMSD(array, objectUsage = False, visualize = False, exp = None, begin = 0, end = None):
	maxData = array[begin]

	for i in array[begin + 1:end]:
		if int(i) > int(maxData):
			maxData = i
	if exp == None:
		exp = 10 ** (len(str(maxData)) - 1)


	print("Recieved", array, begin, end, exp)
	
	array, sections = countingSortMSD(array, objectUsage = objectUsage, visualize = visualize, exp = exp, maxData = 9, minData = 0, start = -1, begin = begin, end = end)

	print(array, begin, end, exp)

	if not len(sections) == 1 and exp != 1:
		for i in sections:

			print("sending", array, sections[i][0], sections[i][1], exp/10)
			radixSortMSD(array, objectUsage = objectUsage, visualize = visualize, exp = exp/10, begin = sections[i][0], end = sections[i][1])

	return array, sections



# Quicksort

def partion(array, start, end, objectUsage = False):
	pivot = array[end]
	pIndex = start - 1

	for i in range(start, end):
		if array[i] <= pivot:
			pIndex += 1
			array[pIndex], array[i] = array[i], array[pIndex]

			# if objectUsage == True:
			# 	array[pIndex].x, array[i].x = array[i].x, array[pIndex].x

			

	array[pIndex + 1], array[end] = array[end], array[pIndex + 1]
	# if objectUsage == True:
	# 	array[pIndex + 1].x, array[end].x = array[end].x, array[pIndex + 1].x


	return pIndex + 1


def quickSort(array, start, end, objectUsage = False, visualize = False):
	if start < end:

		pIndex = partion(array, start = start, end = end, objectUsage = objectUsage)

		quickSort(array, start = start, end = pIndex - 1, objectUsage = objectUsage)

		quickSort(array, start = pIndex + 1, end = end, objectUsage = objectUsage)


# Gnome Sort

def gnomeSort(array): 
	index = 0
	while index < len(array): 
		if index == 0: 
			index = index + 1
		if array[index] >= array[index - 1]: 
			index = index + 1
		else: 
			array[index], array[index-1] = array[index-1], array[index] 
			index = index - 1

	return array


# Bogo Sort

def isSorted(array):
	for i in range(1, len(array)):
		if array[i] < array[i - 1]:
			return False

	return True


def shuffle(array):
	random.shuffle(array)

def bogoSort(array):

	while not isSorted(array):
		shuffle(array)

	return array




totalPieces = 100

for i in range(totalPieces):
	object(totalPieces)
	



running = True

lst = []

for i in range(10):
	lst.append(random.randint(0, 1000))

start_time = time.time()

lst.copy().sort()

print("--- %s seconds for python sort ---" % (time.time() - start_time))

start_time = time.time()

print(radixSortMSD([1, 5, 1, 2, 523, 12, 5, 2]))

print("--- %s seconds for radix sort MSD ---" % (time.time() - start_time))

start_time = time.time()

with recursionlimit(10000):

	quickSort(lst.copy(), 0, len(lst) - 1)

print("--- %s seconds for quicksort sort ---" % (time.time() - start_time))

start_time = time.time()

radixSortLSD(lst.copy(), objectUsage = False, visualize = False)

print("--- %s seconds for radix sort LSD ---" % (time.time() - start_time))

start_time = time.time()

countingSort(lst.copy(), objectUsage = False, visualize=False)

print("--- %s seconds for count sort ---" % (time.time() - start_time))

start_time = time.time()

heapSort(lst.copy(), maxHeap = False, objectUsage = False, visualize=False)

print("--- %s seconds for heap sort ---" % (time.time() - start_time))

start_time = time.time()

insertionSort(lst.copy(), objectUsage = False, visualize=False)

print("--- %s seconds for insertion sort ---" % (time.time() - start_time))

start_time = time.time()

insertionSort(lst.copy())

print("--- %s seconds for binary insertion sort ---" % (time.time() - start_time))

start_time = time.time()

bubbleSort(lst.copy(), objectUsage = False, visualize=False)

print("--- %s seconds for bubble sort ---" % (time.time() - start_time))

start_time = time.time()

selectionSort(lst.copy(), objectUsage = False, visualize=False)

print("--- %s seconds for selection sort ---" % (time.time() - start_time))

start_time = time.time()

print(bogoSort(lst.copy()))

print("--- %s seconds for bogo sort ---" % (time.time() - start_time))

start_time = time.time()

gnomeSort(lst.copy())

print("--- %s seconds for gnome sort ---" % (time.time() - start_time))

while running:
	screen.fill(BLACK)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			exit()
			break


	for i in range(len(toBeSorted)):
		# if int(toBeSorted[i]) < int(toBeSorted[i - 1]):
		# 	print(i)
		toBeSorted[i].draw()


	pygame.display.update()











