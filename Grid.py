import Tile
import Tkinter as tk
import random
import time

class Grid(tk.Frame):
    def __init__(self, root):

        tk.Frame.__init__(self, root)
        self.canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.hsb = tk.Scrollbar(root, orient="horizontal", command=self.canvas.xview)
        self.canvas.configure(yscrollcommand=self.vsb.set)
        self.canvas.configure(xscrollcommand=self.hsb.set)

        self.vsb.pack(side="right", fill="y")
        self.hsb.pack(side="bottom", fill="x")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((4,4), window=self.frame, anchor="nw", 
                                  tags="self.frame")

        self.frame.bind("<Configure>", self.onFrameConfigure)

        self.populate()
        self.hard_to_traverse()

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    #Create and populate grid    
    def populate(self):
        ID = 1
        status = "1"
        gridList = []   #grid list to save our grid in

        for row in range(120):
            colList = []
            for col in range(160):
                address = [row, col]
                global tile
                tile = Tile.make_tile(ID, address, status)
                colList.append([ID, address, status])
                cell = tk.Label(self.frame, text=tile.status, bg="green")
                cell.grid(row=row, column=col, padx='1', pady='1', columnspan=1, rowspan=1)
                ID += 1
            gridList.append(colList)
        #return gridList        

    #select 8 random cells & make them hard to traverse
    def hard_to_traverse(self):

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

                northWest = Xcoordinate - 31
                northEast = Ycoordinate + 31
                southWest = Xcoordinate + 31

                #sides
                if (northEast < 0):
                    northEast = 0
                if northWest < 0:
                    northWest = 0
                if (northWest > 159):
                    northwest = 159
                if southWest > 120:
                    southWest = 120

                print "northWest: %d" % northWest
                print "northEast: %d" % northEast
                print "southWest: %d" % southWest
                print "----------------"
                
                for x in range(northWest, southWest):
                    for y in range(northWest, northEast):
                        prob = int(random.random() *2)
                        if prob == 1:
                            tile.adress = [x, y]
                            tile.status = "2"
                            cell = tk.Label(self.frame, text=tile.status, bg="yellow")
                            cell.grid(row=x, column=y, padx="1", pady="1", columnspan=1, rowspan=1)
            


        
        '''for coordinate in range(8):
            Xcoordinate = int(random.random() * 120)
            Ycoordinate = int(random.random() * 160)
            print "Xcoordinate: %d" % Xcoordinate
            print "Ycoordinate: %d" % Ycoordinate

            #tile.address == [Xcoordinate, Ycoordinate]
            #NEEDS SOME MORE LOOKING INTO
            #if tile.status == "1":
            #CONSIDER THE 31x31 REGION CENTERED AT THIS COORDINATE PAIR FIRST 
            if (Xcoordinate+31) <= 159:
                col_right = Xcoordinate + 31
                print col_right
            else: 
                col_right = 159
                print col_right
            if (Xcoordinate-31) >= 0:
                col_left = Xcoordinate - 31
                print col_left
            else:
                col_left = 0
                print col_left
            if (Ycoordinate+31) <= 119:
                row_down = Ycoordinate + 31
                print row_down
            else:
                row_down = 119
                print row_down
            if (Ycoordinate-31) >= 0:
                row_up = Ycoordinate - 31
                print row_up
            else:
                row_up = 0
                print row_up
                
            #choose with prob 50% to mark it as a hard to taverse cell
            for x in range(row_left, row_right+1):
                for y in range(col_up, col_down+1):
                    print [x, y]
                    prob = int(random.random() * 2)
                    if prob == 1:
                        tile.address = [x, y]
                        tile.status = "2"
                        cell = tk.Label(self.frame, text=tile.status, bg="yellow")
                        cell.grid(row=x, column=y, padx="1", pady="1", columnspan=1, rowspan=1)'''

if __name__ == "__main__":
    root=tk.Tk()
    Grid(root).pack(side="top", fill="both", expand=True)
    root.mainloop()


