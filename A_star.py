import BinaryHeap
import math
import StartGoalVertex

class A_star:

	def __init__(self):
		grid_list = StartGoalVertex.start_and_goal()
		self.start = getStart(grid_list)
		self.start.distance = 0
		#self.start.address[0]
		self.goal = getGoal(grid_list)
		self.fringe = BinaryHeap()
		self.closed = []
		self.fringe.insert(self.start,(self.start.distance + get_heuristic(self.start)))



	def A_star():
		while not self.fringe.empty():
			current = self.fringe.pop()
			if current == self.goal:
				return "path found"
			self.closed.append(current)
			for n in neighbors(current): # !!!!need to get a way to return a list of adjacent squares
				if n not in self.closed:
					if n not in self.fringe:
						n.distance = math.inf
						#need to update parent here. see a star psedocode in assignment details
					update_vertex(current,n)
		return "no path found"


			# need to finish
	def get_heuristic(self, current):
		(x1, y1) = current.address
		(x2, y2) = self.goal
		return math.sqrt((x2-x1)^2 + (y2-y1)^2)

	def get_distance(self, current):
		(x1, y1) = current
		(x2, y2) = self.start
		return math.sqrt((x2-x1)^2 + (y2-y1)^2)
                


	def update_vertex(self, current, nextVertex):
		direction = ""
		if nextVertex == grid_list[((current.address[0]-1)*160)+(current.address[1]+1)] or nextVertex == grid_list[((current.address[0]-1)*160)+(current.address[1]-1)] or nextVertex == grid_list[((current.address[0]+1)*160)+(current.address[1]+1)] or nextVertex == grid_list[((current.address[0]+1)*160)+(current.address[1]-1)]:
			direction = "diagonally"
		if (current.distance + get_cost(current,nextVertex,direction)) < nextVertex.distance:
			nextVertex.distance = current.distance + get_cost(current,nextVertex,direction)
			#need to change parent here
			if nextVertex in self.fringe:
				self.fringe.remove(nextVertex)
			self.fringe.insert(nextVertex,(nextVertex.distance + get_heuristic(nextVertex)))


	def get_cost(self, current, nextVertex, direction):
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


	def neighbors(self, current):
		neighbors = []
		x = current.x
		y = current.y
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



	def getStart(self, grid_list):
		for x in range(120):
			for y in range(160):
				if grid_list[(x*160+y)].status == "s":
					return grid_list[(x*160+y)]


	def getGoal(self, grid_list):
		for x in range(120):
			for y in range(160):
				if grid_list[(x*160+y)].status == "g":
					return grid_list[(x*160+y)]



