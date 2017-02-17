import FourPaths
import random

#randomly block 20% of the grid
def block():
    list4 = FourPaths.four_paths()
    num_blocked = len(list4)/5
    iterator = 0

    while iterator < num_blocked:
        randx = int(random.random() * 120)
        randy = int(random.random() * 160)
        print "iterator:", iterator

        status = list4[(randx*160)+randy].status
        #print "status:", status
        if status == "1" or status == "2":
            list4[(randx*160)+randy].status = "0"
            
            iterator += 1
            #print "status:", status

    return list4

#block()
