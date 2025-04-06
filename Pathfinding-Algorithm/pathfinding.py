import pygame
from queue import PriorityQueue
import math
from tkinter import *
import random
import copy




# root = Tk()

# root.title("Maze Select")

# root.geometry("400x400")

# mazeType = StringVar()

# mazeType.set("None")

# topText = Label(root, text = "Pick your default Maze Type!")

# topText.pack()

# drop = OptionMenu(root, mazeType, "None", "Random")

# drop.pack()

# submitButton = Button(root, text = "Start!")

# submitButton.pack()

# root.mainloop()


# def show():
# 	myLabel = Label(root, text=optionClicked.get())
# 	myLabel.pack()

# optionClicked = StringVar()
# optionClicked.set("Monday")

# drop = OptionMenu(root, optionClicked, "Monday", "Tuesday", "Wednesday")

# drop.pack()
# myLabel = tk.Label(root, text = "Hello World!")
# myLabel1 = tk.Label(root, text = "Hello World!")
# myLabel.grid(row = 0, column = 0)
# myLabel1.grid(row = 1, column = 1)

# myLabel.pack()

# def myClick():
# 	myLabel = Label(root, text = "You Clicked the Button")

# 	myLabel.pack()

# myButton = Button(root, text = "Click Me!", command = myClick, fg = "blue", bg = "blue")

# myButton.pack()



# myButton = Button(root, text="Show Selection", command = show).pack()


# root.mainloop()

pygame.init()


WIDTH = 800

BOARD_SIZE = 50

screen = pygame.display.set_mode((WIDTH, WIDTH))

WHITE = (255, 255, 255)

BLACK = (0, 0, 0)

GREEN = (0, 255, 0)

RED = (255, 0, 0)

BLUE = (0, 0, 255)

ORANGE = (255, 165, 0)

PURPLE = (255, 0, 255)




class Point:
	# START_DEFINED = False
	# END_DEFINED = False

	# @classmethod
	# def start_new(self, new):
	# 	self.START_DEFINED = new


	# def end_new(self, new):
	# 	self.END_DEFINED = new
	def __init__(self, x, y, setId, rows = 50, cols = 50, randomState = False):
		self.total_rows = rows
		self.total_cols = cols
		self.x = round(x)
		self.y = round(y)
		self.activated = True
		self.width = int(WIDTH/BOARD_SIZE)
		self.color = WHITE
		self.pressedBefore = False
		self.start = False
		self.end = False
		self.gScore = float('inf')
		self.cameFrom = None
		self.neighbors = []
		self.boardX = int(self.x/self.width)
		self.boardY = int(self.y/self.width)
		self.used = False
		self.visited = False
		self.neighborDirections = []
		self.setId = setId
		self.directionTo = None


		if randomState:
			if random.randint(0, 100) > 70:
				self.deactivate()


	def deactivate(self):
		self.activated = False
		self.color = BLACK

	def activate(self):
		self.activated = True
		self.color = WHITE


	def clicked(self):
		mouse = pygame.mouse.get_pos()
		click = pygame.mouse.get_pressed()

		if self.start and click[1] == 1 and not (self.x + self.width > mouse[0] > self.x and self.y + self.width > mouse[1] > self.y):
			self.start = False
			self.activate()

		if self.end and click[2] == 1 and not (self.x + self.width > mouse[0] > self.x and self.y + self.width > mouse[1] > self.y):
			self.end = False
			self.activate()




		if not self.pressedBefore:
			if click[0] == 1:
				if self.x + self.width > mouse[0] > self.x and self.y + self.width > mouse[1] > self.y:
					if self.activated:
						self.deactivate()

					else:
						self.activate()

					self.pressedBefore = [True, 0]


					return True


			elif click[1] == 1:
				if self.x + self.width > mouse[0] > self.x and self.y + self.width > mouse[1] > self.y:

					self.color = GREEN
					self.start = True

					self.pressedBefore = [True, 1]

					return True


			elif click[2] == 1:
				if self.x + self.width > mouse[0] > self.x and self.y + self.width > mouse[1] > self.y:
					self.color = RED
					self.end = True

					self.pressedBefore = [True, 2]

					return True





		else:
			if self.pressedBefore != False:
				if self.pressedBefore[1] == 0:
					if click[self.pressedBefore[1]] != 1:
						self.pressedBefore = False


				else:
					self.pressedBefore = False


	def findNeighbors(self, grid, increment = 1):
		self.neighbors = []
		self.neighborDirections = []


	
	
		if self.boardY < self.total_rows - increment and not grid[self.boardY + increment][self.boardX].visited:
			if grid[self.boardY + increment][self.boardX].activated:
				self.neighbors.append((grid[self.boardY + increment][self.boardX], 1))
				self.neighborDirections.append('Down')
		if self.boardY > increment - 1 and grid[self.boardY - increment][self.boardX].activated and not grid[self.boardY - increment][self.boardX].visited:
			self.neighbors.append((grid[self.boardY - increment][self.boardX], 1))
			self.neighborDirections.append('Up')
		if self.boardX < self.total_cols - increment:
			if grid[self.boardY][self.boardX + increment].activated and not grid[self.boardY][self.boardX + increment].visited:
				self.neighbors.append((grid[self.boardY][self.boardX + increment], 1))
				self.neighborDirections.append('Right')
		if self.boardX > increment - 1 and grid[self.boardY][self.boardX - increment].activated and not grid[self.boardY][self.boardX - increment].visited:
			self.neighbors.append((grid[self.boardY][self.boardX - increment], 1))
			self.neighborDirections.append('Left')




	def put_open(self):
		if not self.used:
			self.color = GREEN


	def put_closed(self):
		self.color = RED
		self.used = True


	def __lt__(self, other):
		return False


	def isPath(self):
		self.color = BLUE







	def draw(self):
		# if self.color == WHITE:
		# 	self.activated = True

		# elif self.color == BLACK:
		# 	self.activated = False
		clicked = self.clicked()


		pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.width))

		return clicked


def manhattanDistance(p1, p2):
	return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def dijkstra(p1, p2):
	return 0


def euclidean(p1, p2):
	x1, y1 = p1
	x2, y2 = p2

	return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def generateMazePrims(grid):



	activate = True

	unvisited = (round(len(grid)/2) * round(len(grid[0])/2))


	# if len(grid)%2 == 0:
	# 	unvisited -= len(grid)



	for index, y in enumerate(grid):
		activate = True

		for point in y:
			if index % 2 == 0:
				if not activate:
					point.deactivate()
					activate = True

				else:
					activate = False
					# unvisited += 1

			else:
				point.deactivate()






	current = grid[0][0]

	current.start = True

	current.color = GREEN




	for y in grid:
		for point in y:
			point.findNeighbors(grid, increment = 2)

			# if point.activated:
			# 	unvisited += 1
	

	walls = {}


	first = True

	# clock = pygame.time.Clock()

	while len(walls) > 0 or first:
		# clock.tick(1)
		first = False
		current.visited = True
		current.findNeighbors(grid, increment = 2)



		for index, choiceDirection in enumerate(current.neighborDirections):
			if choiceDirection == 'Right':
				new = grid[current.boardY][current.boardX + 1]

			elif choiceDirection == 'Left':
				new = grid[current.boardY][current.boardX - 1]

			elif choiceDirection == 'Down':
				new = grid[current.boardY + 1][current.boardX]

			elif choiceDirection == 'Up':
				new = grid[current.boardY - 1][current.boardX]



			walls[new] = [current, current.neighbors[index][0]]



		# current.visited = True
		# unvisited = 0
		# for y in grid:
		# 	for point in y:
		# 		point.findNeighbors(grid, increment = 2)
		# current.findNeighbors(grid, increment = 2)


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
				break


	

		# walls.extend(current.neighbors)



	
		randomWall = random.choice(list(walls.keys()))

		randomWallBorder = walls[randomWall]


		if ((randomWallBorder[0].visited) or (randomWallBorder[1].visited)) and not ((randomWallBorder[0].visited) and (randomWallBorder[1].visited)):
			randomWall.activate()
			# current.color = ORANGE
			if randomWallBorder[0].visited:
				current = randomWallBorder[1]


			else:
				current = randomWallBorder[0]




		walls.pop(randomWall)


		# new = current.neighbors[choiceInd][0]








		# current.neighbors.pop(choiceInd)

		# current.neighborDirections.pop(choiceInd)


		# current = new

		# unvisited -= 1


			



		# current.color = PURPLE
			# unvisited -= 1




			

		


		# for i in grid:
		# 	for point in i:
		# 		point.draw()


		# pygame.display.update()

	current = grid[-2][-2]

	current.end = True

	current.color = RED



	return grid





# COULD BE DONE RECURSIVELY

def generateMazeRecursiveDFS(grid, current):
	current.visited = True

	current.findNeighbors(grid, increment = 2)

	# for i in grid:
	# 	for point in i:
	# 		point.draw()


	# pygame.display.update()


	
	while len(current.neighbors) > 0:
		# current.color = PURPLE

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
				break
		

		neighbor, weight = random.choice(current.neighbors)


		choiceInd = current.neighbors.index((neighbor, weight))

		choiceDirection = current.neighborDirections[choiceInd]


		if choiceDirection == 'Right':
				grid[current.boardY][current.boardX + 1].activate()

		elif choiceDirection == 'Left':
			grid[current.boardY][current.boardX - 1].activate()

		elif choiceDirection == 'Down':
			grid[current.boardY + 1][current.boardX].activate()

		elif choiceDirection == 'Up':
			grid[current.boardY - 1][current.boardX].activate()
		# neighbor.neighbors.remove((current, weight))
		# current.neighbors.remove((neighbor, weight))

		# neighbor.neighborDirections.pop(neighbor.index(current))
		# current.neighborDirections.pop(current.index(neighbor))

		# current.color = ORANGE


		generateMazeRecursiveDFS(grid, neighbor)

		current.findNeighbors(grid, increment = 2)



def generateMazeRecursiveDFSMain(grid):
	activate = True

	unvisited = (round(len(grid)/2) * round(len(grid[0])/2))


	# if len(grid)%2 == 0:
	# 	unvisited -= len(grid)



	for index, y in enumerate(grid):
		activate = True

		for point in y:
			if index % 2 == 0:
				if not activate:
					point.deactivate()
					activate = True

				else:
					activate = False
					# unvisited += 1

			else:
				point.deactivate()






	current = grid[0][0]

	current.start = True

	current.color = GREEN

	stack = []

	for y in grid:
		for point in y:
			point.findNeighbors(grid, increment = 2)


	generateMazeRecursiveDFS(grid, current)

	grid[-2][-2].end = True

	grid[-2][-2].color = RED






def generateMazeIterativeDFS(grid):
	activate = True

	unvisited = (round(len(grid)/2) * round(len(grid[0])/2))


	# if len(grid)%2 == 0:
	# 	unvisited -= len(grid)



	for index, y in enumerate(grid):
		activate = True

		for point in y:
			if index % 2 == 0:
				if not activate:
					point.deactivate()
					activate = True

				else:
					activate = False
					# unvisited += 1

			else:
				point.deactivate()






	current = grid[0][0]

	current.start = True

	current.color = GREEN

	stack = []

	for y in grid:
		for point in y:
			point.findNeighbors(grid, increment = 2)

			# if point.activated:
			# 	unvisited += 1
	




	while unvisited > 1:
		current.visited = True


		# current.visited = True
		# unvisited = 0
		# for y in grid:
		# 	for point in y:
		# 		point.findNeighbors(grid, increment = 2)
		# current.findNeighbors(grid, increment = 2)


		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
				break


		current.findNeighbors(grid, increment = 2)



		if len(current.neighbors) > 0:
			stack.append(current)
		
			choiceInd = random.randint(0, len(current.neighbors) - 1)
			choiceDirection = current.neighborDirections[choiceInd]

			if choiceDirection == 'Right':
				grid[current.boardY][current.boardX + 1].activate()

			elif choiceDirection == 'Left':
				grid[current.boardY][current.boardX - 1].activate()

			elif choiceDirection == 'Down':
				grid[current.boardY + 1][current.boardX].activate()

			elif choiceDirection == 'Up':
				grid[current.boardY - 1][current.boardX].activate()



			new = current.neighbors[choiceInd][0]








			current.neighbors.pop(choiceInd)

			current.neighborDirections.pop(choiceInd)


			current = new

			unvisited -= 1


			



			# current.color = PURPLE
			# unvisited -= 1


		elif len(stack) > 0:

			current = stack.pop(-1)

			

		


		# for i in grid:
		# 	for point in i:
		# 		point.draw()


		# pygame.display.update()

	current = grid[-2][-2]

	current.end = True

	current.color = RED



	return grid



def addSet(sets, key, new, used = []):

	sets[key].add(new)

	used.append(key)



	

	for val in sets[key]:
		if val not in used:
			addSet(sets, val, new, used)

	


def kruskalsAlgorithm(grid):

	activate = True

	for index, y in enumerate(grid):
		activate = True

		for point in y:
			if index % 2 == 0:
				if not activate:
					point.deactivate()
					activate = True

				else:
					activate = False

			else:
				point.deactivate()







	wallsOld = {}


	for y in grid:
		for point in y:
			point.findNeighbors(grid, increment = 2)
			for index, choiceDirection in enumerate(point.neighborDirections):
				if choiceDirection == 'Right':
					curWall = grid[point.boardY][point.boardX + 1]

				elif choiceDirection == 'Left':
					curWall = grid[point.boardY][point.boardX - 1]

				elif choiceDirection == 'Down':
					curWall = grid[point.boardY + 1][point.boardX]

				elif choiceDirection == 'Up':
					curWall = grid[point.boardY - 1][point.boardX]

				wallsOld[curWall] = [point, point.neighbors[index][0]]


	walls = {}

	keys = list(wallsOld.keys())

	random.shuffle(keys)


	for key in keys:
		walls[key] = wallsOld[key]



	# # random.shuffle(walls)

	for wall in walls:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()


		if walls[wall][0].setId != walls[wall][1].setId:

			wall.activate()

			# walls[wall][0].color, walls[wall][1].color = BLUE, BLUE



			for row in grid:
				for point in row:
					if point.setId == walls[wall][0].setId:
						point.setId = walls[wall][1].setId


	# 	if walls[wall][1] not in sets[walls[wall][0]] and walls[wall][0] not in sets[walls[wall][1]]:

	# 		wall.activate()


	# 		sets[walls[wall][0]].add(walls[wall][1])

	# 		sets[walls[wall][1]].add(walls[wall][0])

			


	# 		for i in sets[walls[wall][0]]:
	# 			# sets[i].add(walls[wall][1])
	# 			addSet(sets, i, walls[wall][1])

	# 		for i in sets[walls[wall][1]]:
	# 			addSet(sets, i, walls[wall][0])


			
	# 		for i in sets:
	# 			print(len(sets[i]), end = ' ')
	# 		print('\n')



		for row in grid:
			for point in row:
				# point.color = ((point.setId%255)/3, (point.setId%255)/8, (point.setId%255)/5)
				point.draw()


		pygame.display.update()



				




			# print(wall)



def checkPossible(grid, current, hitCycle):
	for index, val in enumerate(current.neighbors):

		neighbor = val[0]

		if neighbor in hitCycle:
			current.neighbors.pop(index)

			current.neighborDirections.pop(index)


	if len(neighbor.neighbors) == 0:
		newElement.neighbors.pop(index)

		newElement.neighborDirections.pop(index)

		return False

	else:

		for val, _ in current.neighbors:
			if not checkPossible(grid, val, hitCycle):
				return False


		return True



def wilsonsAlgorithm(grid):
	activate = True
	total = 0

	for index, y in enumerate(grid):
		activate = True

		for point in y:
		
			if index % 2 == 0:
				if not activate:
					point.deactivate()
					activate = True
					

				else:
					activate = False
					total += 1
					

			else:
				point.deactivate()



	for y in grid:
		for point in y:
			point.findNeighbors(grid, increment = 2)


	# for i in grid:
	# 	for point in i:
	# 		if point.color == BLACK and point.activated:
	# 			print("WHAT")



	startRow = random.randint(0, len(grid) - 1)

	startCol = random.randint(0, len(grid[0]) - 1)



	while not grid[startRow][startCol].activated:


		startRow = random.randint(0, len(grid) - 1)

		startCol = random.randint(0, len(grid[0]) - 1)

	UST = set()

	UST.add(grid[startRow][startCol])

	ustNodes = set()
	ustNodes.add(grid[startRow][startCol])

	# grid[startRow][startCol].color = GREEN

	oppositeDirections = {'Up' : 'Down', 'Left' : 'Right', 'Right' : 'Left', 'Down' : 'Up'}
	iteration = 0
	while len(ustNodes) < total:

		iteration += 1
		for y in grid:
			for point in y:
				point.direction = None
				point.findNeighbors(grid, increment = 2)
		randomRow = random.randint(0, len(grid) - 1)
		randomCol = random.randint(0, len(grid[0]) - 1)



		while (not grid[randomRow][randomCol].activated) or grid[randomRow][randomCol] in UST:
			

			randomRow = random.randint(0, len(grid) - 1)

			randomCol = random.randint(0, len(grid[0]) - 1)



		generated = True

		# print("Grid", grid[randomRow][randomCol] in UST, grid[randomRow][randomCol].color, grid[randomRow][randomCol].activated)



		newElement = grid[randomRow][randomCol]
		hitSelf = False
		hitCycle = []
		while newElement not in UST:
			# print(len(UST))

			# for neighbor, weight in newElement.neighbors:
			# 	if len(neighbor.neighbors) == 0:
			# 		newElement.neighborDirections.pop(newElement.neighbors.index((neighbor, weight)))
			# 		newElement.neighbors.remove((neighbor, weight))

			# copyNeighbors = newElement.neighbors
			# copyDirections = newElement.neighborDirections


			# if newElement.direction != None:
			# 	hitSelf = True
			# 	hitCycle.append(newElement)

			# if hitSelf == True:


			# 	if newElement.direction != None:
			# 		for index, val in enumerate(newElement.neighbors):

			# 			neighbor = val[0]

			# 			if neighbor in hitCycle:
			# 				newElement.neighbors.pop(index)

			# 				newElement.neighborDirections.pop(index)


			# 			else:
			# 				if not checkPossible(grid, neighbor, hitCycle):
			# 					newElement.neighbors.pop(index)

			# 					newElement.neighborDirections.pop(index)







			# 	else:
			# 		hitSelf = False
			# 		hitCycle = []

				# for index, element in enumerate(newElement.neighbors):
				# 	element = element[0]

				# 	if element.direction != None:
				# 		newElement.neighborDirections.pop(index)
				# 		newElement.neighbors.pop(index)


			# if len(newElement.neighbors) == 0:
			# 	newElement.neighbors = copyNeighbors

			# 	newElement.neighborDirections = copyDirections

			# for i in grid:
			# 	for point in i:
			# 		print(len(point.neighbors))

			# newElement.color = PURPLE

			# for event in pygame.event.get():
			# 	if event.type == pygame.QUIT:
			# 		pygame.quit()
			# 		exit()

			newElementInd = random.randint(0, len(newElement.neighbors) - 1)
			newElement.direction = newElement.neighborDirections[newElementInd]

			newElement = newElement.neighbors[newElementInd][0]

			

			# newElement.neighbors.pop(newElementInd)

			# newElement.neighborDirections.pop(newElementInd)


			# newElement.color = RED

			# if iteration  > 3:

			# 	for i in grid:
			# 		for point in i:
			# 			point.draw()



			# 	pygame.display.update()


		endNode = newElement


		newElement = grid[randomRow][randomCol]




		while newElement != endNode:

			# for event in pygame.event.get():
			# 	if event.type == pygame.QUIT:
			# 		pygame.quit()
			# 		exit()


			# newElement.color = RED


			UST.add(newElement)
			ustNodes.add(newElement)

			if newElement.direction == 'Right':
				curWall = grid[newElement.boardY][newElement.boardX + 1]
				newElement = grid[newElement.boardY][newElement.boardX + 2]


			elif newElement.direction == 'Left':
				curWall = grid[newElement.boardY][newElement.boardX - 1]
				newElement = grid[newElement.boardY][newElement.boardX - 2]

			elif newElement.direction == 'Down':
				curWall = grid[newElement.boardY + 1][newElement.boardX]
				newElement = grid[newElement.boardY + 2][newElement.boardX]

			elif newElement.direction == 'Up':
				curWall = grid[newElement.boardY - 1][newElement.boardX]
				newElement = grid[newElement.boardY - 2][newElement.boardX]


			curWall.activate()

			UST.add(curWall)





			# for i in grid:
			# 	for point in i:
			# 		point.draw()
			# 		# point.color = PURPLE



			# pygame.display.update()













	grid[0][0].color = GREEN
	grid[0][0].start = True

	grid[-2][-2].color = RED
	grid[-2][-2].end = True









def algorithm(grid, distanceFunc, dfs = False, greedy = False):

	open_set = PriorityQueue()
	showSteps = False
	current = None

	for i in grid:
		for point in i:
			point.visited = False
	

	if dfs:
		distanceFunc = dijkstra

	for row in grid:
		for point in row:
		
			point.findNeighbors(grid, 1)
			if point.start == True:
				start = point


			if point.end == True:
				end = point




	count = 0

	if dfs:
		count = len(grid) * len(grid[0])






	g_score = {point : float('inf') for row in grid for point in row}
	g_score[start] = 0
	f_score = {point : float('inf') for row in grid for point in row}
	f_score[start] = distanceFunc((start.boardX, start.boardY), (end.boardX, end.boardY))
	came_from = {point : None for row in grid for point in row}

	curOpenSet = {start}
	if dfs:
		open_set.put((count, start))
	else:
		open_set.put((f_score[start], count, start))

	while not open_set.empty():

		# count = 0
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				exit()
				break

		if dfs:
			current = open_set.get()[1]

		else:
			current = open_set.get()[2]




		if current == end:
			print("End")
			curPoint = current
			while curPoint != start:
				curPoint.isPath()
				curPoint = came_from[curPoint]
			return True



		for neighbor, weight in current.neighbors:


			temp_g_score = g_score[current] + weight
			if temp_g_score < g_score[neighbor]:


				g_score[neighbor] = temp_g_score
				came_from[neighbor] = current
				f_score[neighbor] = temp_g_score + distanceFunc((neighbor.boardX, neighbor.boardY), (end.boardX, end.boardY))
				if greedy:
					f_score[neighbor] = distanceFunc((neighbor.boardX, neighbor.boardY), (end.boardX, end.boardY))

				if neighbor not in curOpenSet:
					count += 1
					if dfs:
						count -= 2

		
					if dfs:
						open_set.put((count, neighbor))
					else:
						open_set.put((f_score[neighbor], count, neighbor))
					curOpenSet.add(neighbor)
					if showSteps:
						neighbor.put_open()

					




		if showSteps:
			for row in grid:
				for point in row:
					point.draw()


			pygame.display.update()


		if current != start and showSteps:
			current.put_closed()


























typ = "Random"
def createBoard(size):
	curId = 0
	randomMaze = False
	if typ == "Random":
		randomMaze = True


	
	lst = []

	for y in range(size):
		append = []
		for x in range(size):
			append.append(Point(x * WIDTH/BOARD_SIZE, y * WIDTH/BOARD_SIZE, curId, 50, 50, randomState = randomMaze))
			curId += 1

		lst.append(append)




	return lst






# def main():
	# screen.fill(BLACK)
board = createBoard(50)

running = True

generateMazePrims(board)


# board = generateMazeRecursiveDFSMain(board)


while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()
			exit()
			break


		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:



				def algorithmRun():

					distanceFunc = None


					typeDist = distanceType.get()

					if typeDist == 'Manhattan':
						distanceFunc = manhattanDistance

					else:
						distanceFunc = euclidean

					typeAlg = algorithmType.get()

					if typeAlg == 'A Star':
						algorithm(board, distanceFunc)

					elif typeAlg == 'Dijkstra' or typeAlg == "Bredth First Search":
						algorithm(board, distanceFunc)

					elif typeAlg == 'Depth First Search':
						algorithm(board, distanceFunc, dfs = True)

					else:
						algorithm(board, distanceFunc, greedy = True)



				def createNewMessage(*args):
					typeAlg = algorithmType.get()
					global infoLabel, dropDistance, midText, submitButton
					submitButton.forget()
					infoLabel.destroy()
					if typeAlg == 'A Star':
						infoLabel = Label(root, text = "A Star is a Weighted Algorithm and is gaurenteed to find the shortest path each time. The distance formula is relevent in this algorithm.")
						midText.pack()
						dropDistance.pack()
						infoLabel.pack()
						

					elif typeAlg == 'Dijkstra':
						midText.forget()
						infoLabel = Label(root, text = "Dijkstra is a Weighted Algorithm and is gaurenteed to find the shortest path each time. The distance formula isn't relevent in this algorithm.")
						infoLabel.pack()
						dropDistance.forget()

					elif typeAlg == "Bredth First Search":
						midText.forget()
						infoLabel = Label(root, text = "Bredth First Search isn't a Weighted Algorithm and is gaurenteed to find the shortest path each time. The distance formula isn't relevent in this algorithm.")
						infoLabel.pack()
						dropDistance.forget()

					elif typeAlg == 'Depth First Search':
						midText.forget()
						infoLabel = Label(root, text = "Depth First Search is a Weighted Algorithm and isn't gaurenteed to find the shortest path each time. The distance formula isn't relevent in this algorithm.")
						infoLabel.pack()
						dropDistance.forget()

					else:
						midText.pack()
						infoLabel = Label(root, text = "The Greedy Algorithm is a Weighted Algorithm and isn't gaurenteed to find the shortest path each time. The distance formula is relevent in this algorithm.")
						dropDistance.pack()
						infoLabel.pack()
						


					submitButton.pack()

				root = Tk()

				root.title("Algorithm Select")

				root.geometry("400x400")

				infoLabel = Label(root, text= "")

				infoLabel.pack()

				algorithmType = StringVar()

				distanceType = StringVar()

				algorithmType.set('A Star')

				distanceType.set("Euclidean")



				algorithmType.trace('w', createNewMessage)

				topText = Label(root, text = "Pick your algorithm!")

				topText.pack()

				drop = OptionMenu(root, algorithmType, "A Star", "Dijkstra", "Bredth First Search", "Depth First Search", "Greedy")

				drop.pack()

				midText = Label(root, text = "Pick your distance!")

				midText.pack()

				dropDistance = OptionMenu(root, distanceType, "Euclidean", "Manhattan")

				dropDistance.pack()

				submitButton = Button(root, text = "Visualize", command = algorithmRun)

				submitButton.pack()

				root.mainloop()
				

				



				




				# algorithm(board, manhattanDistance)

	done = False
	for y in board:
		if not done:
			for point in y:
				if point.draw():
					done = True
					break


	pygame.display.update()


	