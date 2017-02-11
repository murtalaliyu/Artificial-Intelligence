import Tile

#Create and populate gridlist 
def populate():

    ID = -1
    status = "1"
    gridList = []   #grid list to save our grid in
    xsize = 7
    ysize = 5
    size = min(xsize, ysize)


    for row in range(120):
        for col in range(160):

            x1 = (col * size)
            y1 = (row * size)
            x2 = x1 + size
            y2 = y1 + size

            global tile
            ID += 1
            address = [row, col]
            tile = Tile.make_tile(ID, address, status)
            gridList.append(tile)
            
    return gridList

#populate()
