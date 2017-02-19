import heapq

class BinaryHeap:
    def __init__(self):
        self.tiles = []
    
    def empty(self):
        return len(self.tiles) == 0

    def pop(self):
    	return heapq.heappop(self.tiles)
    
    def insert(self, tile, priority):
        heapq.heappush(self.tiles, (priority, tile))
    
    def get(self):
        return heapq.heappop(self.tiles)[1]
    
    def remove(self, tile):
    	self.tiles.remove(tile)
    	heapq.heapify(self.tiles)

