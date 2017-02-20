import heapq
import itertools

class BinaryHeap:

    def __init__(self):
        self.tiles = []
    
    def empty(self):
        return len(self.tiles) == 0

    def pop(self):
        tile = heapq.heappop(self.tiles)
    	return tile[1]
    
    def insert(self, tile, priority):
        heapq.heappush(self.tiles, (priority, tile))
    
    def get(self):
        return heapq.heappop(self.tiles)[1]
    
    def remove(self, tile):

        for t in self.tiles:

            if t[1] == tile:
                self.tiles.remove(t)
                heapq.heapify(self.tiles)

    	
        '''

    pq = []                         # list of entries arranged in a heap
    entry_finder = {}               # mapping of tasks to entries
    REMOVED = '<removed-task>'      # placeholder for a removed task
    counter = itertools.count()     # unique sequence count

    def empty(self):
        return len(self.pq) == 0

    def insert(task, priority=0):
        'Add a new task or update the priority of an existing task'
        if task in entry_finder:
            remove_task(task)
        count = next(counter)
        entry = [priority, count, task]
        entry_finder[task] = entry
        heappush(pq, entry)

    def remove(task):
        'Mark an existing task as REMOVED.  Raise KeyError if not found.'
        entry = entry_finder.pop(task)
        entry[-1] = REMOVED

    def pop():
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while pq:
            priority, count, task = heappop(pq)
            if task is not REMOVED:
                del entry_finder[task]
                return task
        raise KeyError('pop from an empty priority queue')

'''