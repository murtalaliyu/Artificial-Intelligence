import FourPaths
import random

#place rivers and highways
def rivers_highways():
    lists = FourPaths.four_paths()
    list4 = lists[0]
    starting_addresses = lists[1]
    print list4[0].address

rivers_highways()
