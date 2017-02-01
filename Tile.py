class Tile(object):
    ID = 0
    address = ""
    status = ""

    def __init__(self, ID, address, status):
        self.ID = ID
        self.address = address
        self.status = status

def make_tile(ID, address, status):
    tile = Tile(ID, address, status)
    return tile
