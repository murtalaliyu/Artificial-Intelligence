class Tile(object):
    ID = 0
    address = []
    status = "1"
    distance = 0

    def __init__(self, ID, address, status, distance):
        self.ID = ID
        self.address = address
        self.status = status
        self.distance = float('inf')

def make_tile(ID, address, status, distance):
    tile = Tile(ID, address, status, distance)
    return tile
