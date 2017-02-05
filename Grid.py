import Tile
import Tkinter as tk
import random
import time

class Grid(tk.Frame):
    def __init__(self, root, rows=120, columns=160, size=32):
        self.rows = rows
        self.columns = columns
        self.size = size

        tk.Frame.__init__(self, root)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                             width=(columns*size), height=(rows*size), background="white")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        self.canvas.bind("<Configure>", self.populate)

    #self.populate()
    #self.hard_to_traverse()
    #self.highways()

#Create and populate grid    
    def populate(self, event):

        ID = 1
        status = "1"
        gridList = []   #grid list to save our grid in
        xsize = int((event.width - 1) / self.columns)
        ysize = int((event.height - 1) / self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")


        for row in range(self.rows):
            colList = []
            for col in range(self.columns):
                address = [row, col]
                global tile
                tile = Tile.make_tile(ID, address, status)
                colList.append([ID, address, status])
                #cell = tk.Label(self.frame, text=tile.status, bg="green")
                #cell.grid(row=row, column=col, padx='1', pady='1', columnspan=1, rowspan=1)

                x1 = (col * self.size)
                y1 = (row * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="green", tags="")

                ID += 1
            gridList.append(colList)

        #return gridList

#select 8 random cells & make them hard to traverse
def hard_to_traverse():

    iterator = 0
    hardToTraverseList = []

    print "1. randomly select hard to traverse cells" 
    while iterator < 8:

        Xcoordinate = int(random.random() * 120)
        Ycoordinate = int(random.random() * 160)
        print "Xcoordinate: %d" % Xcoordinate
        print "Ycoordinate: %d" % Ycoordinate
        
        if [Xcoordinate, Ycoordinate] not in hardToTraverseList:
            
            iterator += 1
            hardToTraverseList.append([Xcoordinate, Ycoordinate])

            xMinus = Xcoordinate - 31
            xPlus = Xcoordinate + 31
            yPlus = Ycoordinate + 31
            yMinus = Ycoordinate - 31

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
            
            for x in range(xMinus, xPlus):
                for y in range(yMinus, yPlus):
                    prob = int(random.random() *2)
                    if prob == 1:
                        tile.adress = [x, y]
                        tile.status = "2"
                        #cell = tk.Label(self.frame, text=tile.status, bg="yellow")
                        #cell.grid(row=x, column=y, padx="1", pady="1", columnspan=1, rowspan=1)
                    else:
                        tile.adress = [x, y]
                        tile.status = "1"
                        #cell = tk.Label(self.frame, text=tile.status, bg="green")
                        #cell.grid(row=x, column=y, padx="1", pady="1", columnspan=1, rowspan=1)
    return hardToTraverseList

#select the highways 
def highways():
    
    print "2. Randomly select 4 paths"
    iterator = 0
    paths = []
    distance = 0    #has to be >= 100

    #select random cell at grid boundary
    while iterator <= 4:
        Xcoordinate = int(random.random() * 120)
        Ycoordinate = int(random.random() * 160)
        
        prob1 = int(random.random() * 4)
        if prob1 == 0:
            Xcoordinate = 0
        elif prob1 == 1:
            Xcoordinate = 119
        elif prob1 == 2:
            Ycoordinate = 0
        elif prob1 == 3:
            Ycoordinate = 159

        #if [Xcoordinate, Ycoordinate] not in paths:
        #print [Xcoordinate, Ycoordinate]

        #mark highway's first 20 cells
        if Xcoordinate == 0:
            for x in range(20):
                tile.address = [x, Ycoordinate]
                if tile.status != "a":
                    if tile.status != "b":
                        if tile.status == "2":
                            tile.status = "b"
                        else:
                            tile.status = "a"
                        #cell = tk.Label(self.frame, text=tile.status, bg="blue")
                        #cell.grid(row=x, column=Ycoordinate, padx="1", pady="1", columnspan=1, rowspan=1)
                        iterator += 1
                        paths.append([x, Ycoordinate])
                        print [x, Ycoordinate]
                        print "iterator: %d" % iterator
        if Xcoordinate == 119:
            x = 119
            while x > 99:
                tile.address = [x, Ycoordinate]
                if tile.status != "a":
                    if tile.status != "b":
                        if tile.status == "2":
                            tile.status = "b"
                        else:
                            tile.status = "a"
                        #cell = tk.Label(self.frame, text=tile.status, bg="blue")
                        #cell.grid(row=x, column=Ycoordinate, padx="1", pady="1", columnspan=1, rowspan=1)  
                        x -= 1
                        iterator += 1
                        paths.append([x, Ycoordinate])
                        print [x, Ycoordinate]
                        print "iterator: %d" % iterator
        if Ycoordinate == 0:
            for y in range(20):
                tile.address = [Xcoordinate, y]
                if tile.status != "a":
                    if tile.status != "b":
                        if tile.status == "2":
                            tile.status = "b"
                        else:
                            tile.status = "a"
                        #cell = tk.Label(self.frame, text=tile.status, bg="blue")
                        #cell.grid(row=Xcoordinate, column=y, padx="1", pady="1", columnspan=1, rowspan=1)
                        iterator += 1
                        paths.append([Xcoordinate, y])
                        print "iterator: %d" % iterator
                        print [Xcoordinate, y]
        if Ycoordinate == 159:
            y = 159
            while y > 139:
                tile.address = [Xcoordinate, y]
                if tile.status != "a":
                    if tile.status != "b":
                        if tile.status == "2":
                            tile.status = "b"
                        else:
                            tile.status = "a"
                        #cell = tk.Label(self.frame, text=tile.status, bg="blue")
                        #cell.grid(row=Xcoordinate, column=y, padx="1", pady="1", columnspan=1, rowspan=1)
                        y -= 1
                        iterator += 1
                        paths.append([Xcoordinate, y])
                        print [Xcoordinate, y]
                        print "iterator: %d" % iterator

    #select set of 20 paths till we reach boundary
    return paths   
                
            

if __name__ == "__main__":
    root=tk.Tk()
    Grid(root).pack(side="top", fill="both", expand="true", padx=4, pady=4)
    root.mainloop()

#populate()
#hard_to_traverse()
#highways()