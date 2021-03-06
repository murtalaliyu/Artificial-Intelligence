import Tile
import Gridlist
import random


#Update Gridlist to show hard to traverse tiles
#select 8 random cells & make them hard to traverse
def hard():

    iterator = 0
    hardToTraverseList = []
    list2 = Gridlist.populate()

    print "1. randomly select hard to traverse cells around 31x31 tiles" 
    while iterator < 8:

        Xcoordinate = int(random.random() * 120)
        Ycoordinate = int(random.random() * 160)
        print "Xcoordinate: %d" % Xcoordinate
        print "Ycoordinate: %d" % Ycoordinate
        
        if [Xcoordinate, Ycoordinate] not in hardToTraverseList:
            
            iterator += 1
            hardToTraverseList.append([Xcoordinate, Ycoordinate])

            xMinus = Xcoordinate - 15
            xPlus = Xcoordinate + 15
            yPlus = Ycoordinate + 15
            yMinus = Ycoordinate - 15

            #sides
            if (xMinus <= 0):
                xMinus = 0
            if xPlus >= 119:
                xPlus = 119
            if (yPlus >= 159):
                yPlus = 159
            if yMinus <= 0:
                yMinus = 0

            print "xMinus: %d" % xMinus
            print "xPlus: %d" % xPlus
            print "yMinus: %d" % yMinus
            print "yPlus: %d" % yPlus
            if iterator == 8:
                print '''----------------
----------------'''
            else:
                print "----------------"
            
            for x in range(xMinus, xPlus+1):
                for y in range(yMinus, yPlus+1):
                    prob = int(random.random() *2)
                    if prob == 1:
                        list2[(x*160)+y].status = "2"
                    else:
                        list2[(x*160)+y].status = "1" 
 
    return list2



