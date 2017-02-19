from BinaryHeap import BinaryHeap
import math
import StartGoalVertex
global start
global goal
global fringe
global fringeList

def getStart(grid_list):
	for x in range(120):
		for y in range(160):
			if grid_list[(x*160+y)].status == "s":
				return grid_list[(x*160+y)]


def getGoal(grid_list):
	for x in range(120):
		for y in range(160):
			if grid_list[(x*160+y)].status == "g":
				return grid_list[(x*160+y)]

def get_heuristic(current):
	x1 = current.address[0]
	y1 = current.address[1]
	x2 = goal.address[0]
	y2 = goal.address[1]

	return math.sqrt((x2-x1)**2 + (y2-y1)**2)


grid_list = StartGoalVertex.start_and_goal()
start = getStart(grid_list)
start.distance = 0
#self.start.address[0]
goal = getGoal(grid_list)
fringe = BinaryHeap()
closed = []
fringeList = []
fringe.insert(start,(start.distance + get_heuristic(start)))
fringeList.append(start)



		# need to finish


def get_distance(current):
	(x1, y1) = current
	(x2, y2) = start
	return math.sqrt((x2-x1)^2 + (y2-y1)^2)
            


def update_vertex(current, nextVertex):
	direction = ""
	if nextVertex == grid_list[((current.address[0]-1)*160)+(current.address[1]+1)] or nextVertex == grid_list[((current.address[0]-1)*160)+(current.address[1]-1)] or nextVertex == grid_list[((current.address[0]+1)*160)+(current.address[1]+1)] or nextVertex == grid_list[((current.address[0]+1)*160)+(current.address[1]-1)]:
		direction = "diagonally"
	if (current.distance + get_cost(current,nextVertex,direction)) < nextVertex.distance:
		nextVertex.distance = current.distance + get_cost(current,nextVertex,direction)
		#need to change parent here
		if nextVertex in fringeList:
			fringe.remove(nextVertex)
		fringe.insert(nextVertex,(nextVertex.distance + get_heuristic(nextVertex)))
		fringeList.append(nextVertex)


def get_cost(current, nextVertex, direction):
	#need to figure out way to get status of tile

	if direction != "diagonally":

		if current.status == 1 and nextVertex.status == 1:
			return 1

		elif current.status == 2 and nextVertex.status ==2:
			return 2
		elif (current.status == 1 and nextVertex.status == 2) or (current.status == 2 and nextVertex.status == 1):
			return 1.5

	else:
		if current.status == 1 and nextVertex.status == 1:
			return 1

		elif current.status == 2 and nextVertex.status ==2:
			return math.sqrt(8)
		elif (current.status == 1 and nextVertex.status == 2) or (current.status == 2 and nextVertex.status == 1):
			return ((math.sqrt(2) + math.sqrt(8))/2)

	return 0


def neighbors(current):
	neighbors = []
	x = current.address[0]
	y = current.address[1]
	if grid_list[(x*160)+(y+1)]:
		neighbors.append(grid_list[(x*160)+(y+1)]) # tile to right
	if grid_list[(x*160)+(y-1)]:
		neighbors.append(grid_list[(x*160)+(y-1)]) # tile to left
	if grid_list[((x+1)*160)+(y)]:
		neighbors.append(grid_list[((x+1)*160)+(y)]) # tile below
	if grid_list[((x-1)*160)+(y)]:
		neighbors.append(grid_list[((x-1)*160)+(y)]) # tile above
	if grid_list[((x-1)*160)+(y+1)]:
		neighbors.append(grid_list[((x-1)*160)+(y+1)]) # tile top right
	if grid_list[((x-1)*160)+(y-1)]:
		neighbors.append(grid_list[((x-1)*160)+(y-1)]) # tile top left
	if grid_list[((x+1)*160)+(y+1)]:
		neighbors.append(grid_list[((x+1)*160)+(y+1)]) # tile bottom right
	if grid_list[((x+1)*160)+(y-1)]:
		neighbors.append(grid_list[((x+1)*160)+(y-1)]) # tile bottom left
	return neighbors



def Main():
	while not fringe.empty():
		current = fringe.pop()
		if current == goal:
			return "path found"
		closed.append(current)
		for n in neighbors(current): # !!!!need to get a way to return a list of adjacent squares
			if n not in closed:
				if n not in fringeList:
					n.distance = float('inf')
					#need to update parent here. see a star psedocode in assignment details
				update_vertex(current,n)
	return "no path found"


Main()