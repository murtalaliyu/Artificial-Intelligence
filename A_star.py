import heapq
import math
import StartGoalVertex

class A_star:

	def __init__(self):
		grid_list = StartGoalVertex.start_and_goal()
		self.distance = 0
		self.start = getStart(grid_list)
		self.goal = getGoal(grid_list)
		self.fringe = []
		self.closed = []
		heapq.heapify(self.fringe)
		heapq.heappush(self.fringe,self.start)
		heapq.heappush(self.fringe, (self.start + get_heuristic(self.start)))


		def A_star():
			while not self.fringe:
				current = heapq.heappop(fringe)
				if current == self.goal:
					return "path found"
				self.closed.append(current)
				for n in neighbors(current): # !!!!need to get a way to return a list of adjacent squares
					if n in self.closed:
						if n in self.fringe:
							get_distance(n) = math.inf
							#need to update parent here. see a star psedocode in assignment details
						update_vertex(current,nextVertex)
			return "no path found"


			# need to finish
	def get_heuristic(current, goal):
		(x1, y1) = current
		(x2, y2) = goal
		return math.sqrt((x2-x1)^2 + (y2-y1)^2)

	def get_distance(self, s):
                #need to implement 
                pass


	def update_vertex(self, current, nextVertex):
		if (get_distance(current) + get_cost(current,nextVertex)) < get_distance(nextVertex):
			get_distance(nextVertex) = get_distance(current) + get_cost(current,nextVertex)
			#need to change parent here
			if nextVertex in fringe:
				self.fringe.remove(nextVertex)
			heapq.heappush(self.fringe,nextVertex)
			heapq.heappush(self.fringe, (get_distance(nextVertex)+get_heuristic(nextVertex)))


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


	def neighbors(current):
		neighbors = []
		x = current.x
		y = current.y
		if grid_list[(x.160)+(y+1)]:
			neighbors.append(grid_list[(x.160)+(y+1)]) # tile to right
		if grid_list[(x.160)+(y-1)]:
			neighbors.append(grid_list[(x.160)+(y-1)]) # tile to left
		if grid_list[((x+1).160)+(y)]:
			neighbors.append(grid_list[((x+1).160)+(y)]) # tile below
		if grid_list[((x-1).160)+(y)]:
			neighbors.append(grid_list[((x-1).160)+(y)]) # tile above
		if grid_list[((x-1).160)+(y+1)]:
			neighbors.append(grid_list[((x-1).160)+(y+1)]) # tile top right
		if grid_list[((x-1).160)+(y-1)]:
			neighbors.append(grid_list[((x-1).160)+(y-1)]) # tile top left
		if grid_list[((x+1).160)+(y+1)]:
			neighbors.append(grid_list[((x+1).160)+(y+1)]) # tile bottom right
		if grid_list[((x+1).160)+(y-1)]:
			neighbors.append(grid_list[((x+1).160)+(y-1)]) # tile bottom left
		return neighbors



	def getStart(grid_list):
		for x in range(120):
			for y in range(160):
				if grid_list[(x.160+y)].status == "s":
					return grid_list[(x.160+y)]


	def getGoal(grid_list):
		for x in range(120):
			for y in range(160):
				if grid_list[(x.160+y)].status == "g":
					return grid_list[(x.160+y)]



