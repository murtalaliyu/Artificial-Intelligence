from BinaryHeap import BinaryHeap
import math
import StartGoalVertex
global start
global goal
global fringe
global fringeList
global path
grid_list = StartGoalVertex.start_and_goal()

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

def calculate_distances(grid_list):
	start_x = start.address[0]
	start_y = start.address[1]

	for x in range(120):
		for y in range(160):
			if grid_list[(x*160+y)].status != "s" and grid_list[(x*160+y)].status != "g":
				grid_list[(x*160+y)].distance = math.sqrt((x-start_x)**2 + (y-start_y)**2)


start = getStart(grid_list)
#calculate_distances(grid_list)
start.distance = 0
#self.start.address[0]
goal = getGoal(grid_list)
fringe = BinaryHeap()
closed = []
fringeList = []
path = []
fringe.insert(start,(start.distance + get_heuristic(start)))
fringeList.append(start)


				

	
            


def update_vertex(current, nextVertex):
	direction = ""
	if nextVertex == grid_list[((current.address[0]-1)*160)+(current.address[1]+1)] or nextVertex == grid_list[((current.address[0]-1)*160)+(current.address[1]-1)] or nextVertex == grid_list[((current.address[0]+1)*160)+(current.address[1]+1)] or nextVertex == grid_list[((current.address[0]+1)*160)+(current.address[1]-1)]:
		direction = "diagonally"
	if (current.distance + get_cost(current,nextVertex,direction)) < nextVertex.distance:
		nextVertex.distance = current.distance + get_cost(current,nextVertex,direction)
		#need to change parent here
		if nextVertex in fringeList:
			fringe.remove(nextVertex)
			fringeList.remove(nextVertex)
		fringe.insert(nextVertex,(nextVertex.distance + get_heuristic(nextVertex)))
		fringeList.append(nextVertex)


def get_cost(current, nextVertex, direction):
	#need to figure out way to get status of tile

	if direction != "diagonally":

		if current.status == "1" and nextVertex.status == "1":
			return 1

		elif current.status == "2" and nextVertex.status =="2":
			return 2
		elif (current.status == "1" and nextVertex.status == "2") or (current.status == "2" and nextVertex.status == "1"):
			return 1.5

	elif direction == "straight":
		if current.status == "1" and nextVertex.status == "1":
			return 1

		elif current.status == "2" and nextVertex.status =="2":
			return math.sqrt(8)
		elif (current.status == "1" and nextVertex.status == "2") or (current.status == "2" and nextVertex.status == "1"):
			return ((math.sqrt(2) + math.sqrt(8))/2)

	return 0


def neighbors(current):
	neighbors = []
	x = current.address[0]
	y = current.address[1]

	if grid_list[(x*160)+(y+1)] and grid_list[(x*160)+(y+1)].status != "0":
		neighbors.append(grid_list[(x*160)+(y+1)]) # tile to right
	if grid_list[(x*160)+(y-1)] and grid_list[(x*160)+(y-1)].status != "0":
		neighbors.append(grid_list[(x*160)+(y-1)]) # tile to left
	if grid_list[((x+1)*160)+(y)] and grid_list[((x+1)*160)+(y)].status != "0":
		neighbors.append(grid_list[((x+1)*160)+(y)]) # tile below
	if grid_list[((x-1)*160)+(y)] and grid_list[((x-1)*160)+(y)].status != "0":
		neighbors.append(grid_list[((x-1)*160)+(y)]) # tile above
	if grid_list[((x-1)*160)+(y+1)] and grid_list[((x-1)*160)+(y+1)].status != "0":
		neighbors.append(grid_list[((x-1)*160)+(y+1)]) # tile top right
	if grid_list[((x-1)*160)+(y-1)] and grid_list[((x-1)*160)+(y-1)].status != "0":
		neighbors.append(grid_list[((x-1)*160)+(y-1)]) # tile top left
	if grid_list[((x+1)*160)+(y+1)] and grid_list[((x+1)*160)+(y+1)].status != "0":
		neighbors.append(grid_list[((x+1)*160)+(y+1)]) # tile bottom right
	if grid_list[((x+1)*160)+(y-1)] and grid_list[((x+1)*160)+(y-1)].status != "0":
		neighbors.append(grid_list[((x+1)*160)+(y-1)]) # tile bottom left
	return neighbors



def Main():
	print "start node:", start.address
	print "goal node:", goal.address

	while not fringe.empty():
		current = fringe.pop()
		path.append(current.address)
		print "current tile:", current.address
		if current == goal:
			print "path found"

			for tile in path:
				
				x = tile[0]
				y = tile[1]
				if grid_list[(x*160)+y].status != "s" and grid_list[(x*160)+y].status != "g":
					grid_list[(x*160)+y].status = "w"



			return grid_list
		closed.append(current)
		for n in neighbors(current): # !!!!need to get a way to return a list of adjacent squares
			if n not in closed:
				if n not in fringeList:
					n.distance = float('inf')
					#need to update parent here. see a star psedocode in assignment details
				update_vertex(current,n)
	print "no path found"
	return "no path found"

#Main()