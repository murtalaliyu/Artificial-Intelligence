import Hard
import random

#select the first 20 cells to be highways, 4 times 
def four_paths():
    list3 = Hard.hard()
    print "2. Randomly select 4 paths"
    iterator = 0
    paths = []

    #select random cell at grid boundary
    while iterator < 4:
        Xcoord = int(random.random() * 120)
        Ycoord = int(random.random() * 160)

        if Xcoord == 0 or Xcoord == 119 or Ycoord == 0 or Ycoord == 159:

            address = [Xcoord, Ycoord]
            
            if [Xcoord, Ycoord] not in paths:
                if list3[(Xcoord*160)+Ycoord].status == "1" or list3[(Xcoord*160)+Ycoord].status == "2":
                    paths.append(address)
                    status = list3[(Xcoord*160)+Ycoord].status
                    if status == "1":
                        list3[(Xcoord*160)+Ycoord].status = "a"
                    elif status == "2":
                        list3[(Xcoord*160)+Ycoord].status = "b"
                    iterator += 1
                    
            print "status: %s" % list3[(Xcoord*160)+Ycoord].status        
            print address
            print "------------"


    #move randomly hori or vert away from boundary for 20 cells
    iterator = 0
    while iterator < 4:
        xC = paths[iterator][0]
        yC = paths[iterator][1]

        if xC == 0 and yC >= 0:
            for x in range(20):
                status = list3[(x*160)+yC].status
                if status == "1":
                    list3[(x*160)+yC].status = "a"
                elif status == "2":
                    list3[(x*160)+yC].status = "b"
        elif xC == 119 and yC >= 0:
            i = 119
            while i > 99:
                status = list3[(i*160)+yC].status
                if status == "1":
                    list3[(x*160)+yC].status = "a"
                elif status == "2":
                    list3[(x*160)+yC].status = "b"
                i -= 1
        '''elif xC >= 0 and yC == 0:
            for x in range(20):'''
                

        iterator += 1


        

    return list3
        
#four_paths()




















