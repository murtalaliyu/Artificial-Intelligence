import Hard
import random

#select the first 20 cells to be highways, 4 times 
def four_paths():
    iterator1 = 0
    global list3
    list3 = Hard.hard()
    print "2. Randomly select 4 paths and assign them as rivers and highways"
    global iterator
    global paths
    paths = []

    paths.append([0, 0])
    paths.append([119, 0])
    paths.append([0, 159])
    paths.append([119, 159])

    #select random cell at grid boundary
    while iterator1 < 4:
        Xcoord = int(random.random() * 120)
        Ycoord = int(random.random() * 160)

        if Xcoord == 0 or Xcoord == 119 or Ycoord == 0 or Ycoord == 159:
            global starting_address
            starting_address = [Xcoord, Ycoord]
            if starting_address not in paths:
                global continuing_address
                continuing_address = first_twenty_tiles(starting_address)

                rest_of_path(continuing_address)
            
                iterator1 += 1
        #print "iterator:", [Xcoord, Ycoord]
    return list3



#move randomly hori or vert away from boundary for 20 cells
def first_twenty_tiles(starting_address):
    final_address = 0
    xC = starting_address[0]
    yC = starting_address[1]
    
    if xC == 0 and yC > 0 and yC < 159:
        print "starting address:", [xC, yC]
        for x in range(20):
            current_address = [x, yC]
            if current_address not in paths:
                paths.append(current_address)
                #print x+1, ", current_address:", current_address
                status = list3[(x*160)+yC].status
                if status == "1":
                    list3[(x*160)+yC].status = "a"
                elif status == "2":
                    list3[(x*160)+yC].status = "b"
                if x == 19:
                    final_address = current_address
                    print "final_address:", final_address
                    
            #print paths
            #print "current_address:", current_address
    elif xC == 119 and yC > 0 and yC < 159:
        print "starting_address:", [xC, yC]
        i = 119
        while i > 99:
            current_address = [i, yC]
            if current_address not in paths:
                paths.append(current_address)
                #print i+1, ", current_address:", current_address
                status = list3[(i*160)+yC].status
                if status == "1":
                    list3[(i*160)+yC].status = "a"
                elif status == "2":
                    list3[(i*160)+yC].status = "b"
                i -= 1
                if i == 100:
                    final_address = current_address
                    print "final_address:", final_address
            #print paths
            #print "current_address:", current_address
    elif xC > 0 and xC < 119 and yC == 0:
        print "starting address:", [xC, yC]
        for y in range(20):
            current_address = [xC, y]
            if current_address not in paths:
                status = list3[(xC*160)+y].status
                if status == "1":
                    list3[(xC*160)+y].status = "a"
                elif status == "2":
                    list3[(xC*160)+y].status = "b"
                if y == 19:
                    final_address = current_address
                    print "final address:", final_address
    elif xC > 0 and xC < 119 and yC == 159:
        print "starting address:", [xC, yC]
        j = 159
        while j > 139:
            current_address = [xC, j]
            if current_address not in paths:
                paths.append(current_address)
                #print j+1, "current_address:", current_address
                status = list3[(xC*160)+j].status
                if status == "1":
                    list3[(xC*160)+j].status = "a"
                elif status == "2":
                    list3[(xC*160)+j].status = "b"
                j -= 1
                if j == 140:
                    final_address = current_address
                    print "final address:", final_address
    
    return final_address




#add rest of highway/river    
def rest_of_path(continuing_address):
    print "continuing_address:", continuing_address
    print "-----------------------------"


four_paths()
