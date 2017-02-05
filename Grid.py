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
                print "----------------"
                
                for x in range(xMinus, xPlus):
                    for y in range(yMinus, yPlus):
                        prob = int(random.random() *2)
                        if prob == 1:
                            tile.adress = [x, y]
                            tile.status = "2"
                            cell = tk.Label(self.frame, text=tile.status, bg="yellow")
                            cell.grid(row=x, column=y, padx="1", pady="1", columnspan=1, rowspan=1)
            
if __name__ == "__main__":
    root=tk.Tk()
    Grid(root).pack(side="top", fill="both", expand=True)
    root.mainloop()


