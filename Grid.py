import Tile

grid = []
status = "1"
iterator = 1

#Generate row of length 120
for row in range(120):
    #Append a blank list to each row cell    
    grid.append([])
    for column in range(160):
        #Assign status to each row
        tile = Tile.make_tile(iterator, [row, column], status)
        grid[row].append(tile.status)
        iterator =+ 1
        
#Function will print board like an actual board
def print_grid(grid):
    for row in grid:
        print row

print_grid(grid)
