import Hard
import random

#randomly place 4 paths with length > 100, border to border
def four_paths():
    list3 = Hard.hard()
    print "2. Randomly select 4 paths and assign them as rivers and highways"
    iterator = 0
    global pathList
    pathList = [[],     #top border
                [],     #left border
                [],     #bottom border
                []]     #right border

    while iterator < 1:
        #choose a new highway/river beginning
        x = int(random.random()*120)
        y = int(random.random()*160)

        #place 1st 20
        if x==0: #top
            currentAddress = [x,y]

            #check if valid path
            count = 0
            for i in range(20):
                status = list3[(i*160)+y].status
                if status!="a" or status!="b":
                    count += 1
                    print "count:", count
                    
            #add to grid if valid
            if count==20:
                '''for i in range(20):
                        currentAddress = [i,y]
                        if currentAddress not in pathList[0]:
                            pathList[1].append(currentAddress)
                            if list3[(i*160)+y].status=="1": 
                                list3[(i*160)+y].status = "a"
                            elif list3[(i*160)+y].status=="2":
                                list3[(i*160)+y].status = "b"
                        
                iterator +=1'''
                
                #place rest of path > 100, until hits another border
                complete = "false"
                
                        
        elif y==0: #left side #------------->
            currentAddress = [x,y]
            
            #check if valid path
            count = 0
            for j in range(20):
                status = list3[(x*160)+j].status
                if status!="a" or status!="b":
                    count += 1
                    print "count:", count
                    
            #add to grid if valid
            if count==20:
                '''for j in range(20):
                    currentAddress = [x,j]
                    if currentAddress not in pathList[1]:
                        pathList[2].append(currentAddress)
                        if list3[(x*160)+j].status=="1":
                            list3[(x*160)+j].status = "a"
                        elif list3[(x*160)+j].status=="2":
                            list3[(x*160)+j].status = "b"
                iterator +=1'''
                
                #place rest of path > 100, until hits another border

                    
        elif x==119: #bottom
            currentAddress = [x,y]
            
            #check if valid path
            count = 0
            for i in range(100,120):
                status = list3[(i*160)+y].status
                if status!="a" or status!="b":
                    count += 1
                    print "count:", count
                    
            #add to grid if valid
            if count==20:
                '''for i in range(100,120):
                    currentAddress = [i,y]
                    if currentAddress not in pathList[2]:
                        pathList[3].append(currentAddress)
                        if list3[(i*160)+y].status=="1":
                            list3[(i*160)+y].status = "a"
                        elif list3[(i*160)+y].status=="2":
                            list3[(i*160)+y].status = "b"
                iterator +=1'''
                
                #place rest of path > 100, until hits another border
                            
                        
        elif y==159: #right side  <-------------#
            currentAddress = [x,y]

            #check if valid path
            count = 0
            for j in range(140,160):
                status = list3[(x*160)+j]
                if status!="a" or status!="b":
                    count += 1
                    print "count:", count
                    
             #add to grid if valid
            if count==20:
                '''for j in range(140,160):
                    currentAddress = [x,j]
                    if currentAddress not in pathList[3]:
                        pathList[3].append(currentAddress)
                        if list3[(x*160)+j].status=="1":
                            list3[(x*160)+j].status = "a"
                        elif list3[(x*160)+j].status=="2":
                            list3[(x*160)+j].status = "b"
                iterator +=1
                '''
                
                #place rest of path > 100, until hits another border

                            
                        
    return list3

def place_downward(currentAddress):
    x = currentAddress[0]
    y = currentAddress[1]
    count = 0

    #check if valid path
    if x+19 <= 119:
        for i in range(x,x+20):
            address = [i,y]
            if address not in pathList:
                pathList[0].append()
    
    return False

#four_paths()
