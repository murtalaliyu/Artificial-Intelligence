import heapq
import math

class A_star:

	def __init__(self, start, stop):
		self.distance = 0
		self.parent = start
		self.fringe = []
		self.closed = []
		heapq.heapify(self.fringe)
		heapq.heappush(self.fringe,self.start)
		heapq.heappush(self.fringe, (self.start + get_heuristic(self.start)))


		def A_star():
			while not fringe:
				current = heapq.heappop(fringe)
				if current == goal:
					return "path found"
				closed.append(current)
				for n in succ(current): # !!!!need to get a way to return a list of adjacent squares
					if n in closed:
						if n in fringe:
							get_distance(n) = math.inf
							#need to update parent here. see a star psedocode in assignment details
						update_vertex(current,nextVertex)
			return "no path found"


			# need to finish
'''	def get_heuristic(a, b):
		(x1, y1) = a
		(x2, y2) = b
		return abs(x1-x2) + abs (y1-y2) '''

	def get_distance(s):
                #need to implement 
                pass


	def update_vertex(current, nextVertex):
		if (get_distance(current) + get_cost(current,nextVertex)) < get_distance(nextVertex):
			get_distance(nextVertex) = get_distance(current) + get_cost(current,nextVertex)
			#need to change parent here
			if nextVertex in fringe:
				fringe.remove(nextVertex)
			heapq.heappush(fringe,nextVertex)
			heapq.heappush(fringe, (get_distance(nextVertex)+get_heuristic(nextVertex)))


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
				return sqrt(8)
			elif (current.status == 1 and nextVertex.status == 2) or (current.status == 2 and nextVertex.status == 1):
				return ((sqrt(2) + sqrt(8))/2)

