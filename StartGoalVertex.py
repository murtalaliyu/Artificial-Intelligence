import BlockedCells
import random

#select start and goal vertex
def start_and_goal():
    list4 = BlockedCells.block()
    it = 0

    while it < 1:
        startx = 0
        starty = 0
        goalx = 0
        goaly = 0
        prob1 = int(random.random() * 4)    
        prob2 = int(random.random() * 4)

        #start vertex
        if prob1 == 0:      #top left region
            startx = random.randint(0, 19)
            starty = random.randint(0, 19)
        elif prob1 == 1:    #top right region
            startx = random.randint(0, 19)
            starty = random.randint(139, 159)
        elif prob1 == 2:    #bottom left region
            startx = random.randint(99, 119)
            starty = random.randint(0, 19)
        elif prob1 == 3:    #bottom right region
            startx = random.randint(99, 119)
            starty = random.randint(139, 159)

        #goal vertex
        if prob2 == 0:      #top left region
            goalx = random.randint(0, 19)
            goaly = random.randint(0, 19)
        elif prob2 == 1:    #top right region
            goalx = random.randint(0, 19)
            goaly = random.randint(139, 159)
        elif prob2 == 2:    #bottom left region
            goalx = random.randint(99, 119)
            goaly = random.randint(0, 19)
        elif prob2 == 3:    #bottom right region
            goalx = random.randint(99, 119)
            goaly = random.randint(139, 159)

        if list4[(startx*160)+starty].status != "0":
            if list4[(goalx*160)+goaly].status != "0":
                if abs(startx - goalx) >= 100 or abs(starty - goaly) >= 100:
                    start = [startx, starty]
                    goal = [goalx, goaly]
                    list4[(startx*160)+starty].status = "s"
                    list4[(goalx*160)+goaly].status = "g"
                    #print "distance:", abs((startx*160)+starty - (goalx*160)+goaly)
                    #print start
                    #print goal
                    it += 1

    return list4
