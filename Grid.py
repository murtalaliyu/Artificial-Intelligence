import Tile
import A_star
import Gridlist
import Hard
import FourPaths
import BlockedCells
import StartGoalVertex
import Tkinter as tk
import random
import time

class Grid(tk.Frame):
    
    def __init__(self, root, rows=120, columns=160, size=32, gridList=[]):
        self.rows = rows
        self.columns = columns
        self.size = size

        tk.Frame.__init__(self, root)
        self.canvas = tk.Canvas(self, borderwidth=0, highlightthickness=0,
                             width=(columns*size), height=(rows*size), background="white")
        self.canvas.pack(side="top", fill="both", expand=True, padx=2, pady=2)

        #self.canvas.bind("<Configure>", self.populate)
        #self.canvas.bind("<Configure>", self.hard_to_traverse)
        #self.canvas.bind("<Configure>", self.four_paths)
        self.canvas.bind("<Configure>", self.blocked_cells)

    #Create and populate grid    
    def populate(self, event):
        list1 = Gridlist.populate()
        xsize = int((event.width - 1) / self.columns)
        ysize = int((event.height - 1) / self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")

        for x in range(120):
            for y in range(160):
                x1 = (y * self.size)
                y1 = (x * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size
                
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="green", tags="")
        
    #select 8 random cells & make them hard to traverse
    def hard_to_traverse(self, event):
        list2 = Hard.hard()
        xsize = int((event.width - 1) / self.columns)
        ysize = int((event.height - 1) / self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")

        for x in range(120):
            for y in range(160):
                x1 = (y * self.size)
                y1 = (x * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size

                status = list2[(x*160)+y].status
                
                if status == "1":
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="green", tags="")
                elif status == "2":
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="yellow", tags="")
        
    #select cells to be highways, 4 times
    def four_paths(self, event):
        list3 = FourPaths.four_paths()
        xsize = int((event.width - 1) / self.columns)
        ysize = int((event.height - 1) / self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")

        for x in range(120):
            for y in range(160):
                x1 = (y * self.size)
                y1 = (x * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size

                status = list3[(x*160)+y].status
                #print status
                
                if status == "1":
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="green", tags="")
                elif status == "2":
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="yellow", tags="")
                elif status == "a":
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="blue", tags="")
                elif status == "b":
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="red", tags="")

    #randomly block 20% of the grid, not including tiles belonging to a highway
    def blocked_cells(self, event):
        list4 = BlockedCells.block()
        xsize = int((event.width - 1) / self.columns)
        ysize = int((event.height - 1) / self.rows)
        self.size = min(xsize, ysize)
        self.canvas.delete("square")

        #get start and goal vertexes
        list4 = StartGoalVertex.start_and_goal()

        for x in range(120):
            for y in range(160):
                x1 = (y * self.size)
                y1 = (x * self.size)
                x2 = x1 + self.size
                y2 = y1 + self.size

                status = list4[(x*160)+y].status
                if status == "0":
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="black", tags="")
                if status == "1":
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="green", tags="")
                elif status == "2":
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="yellow", tags="")
                elif status == "a":
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="blue", tags="")
                elif status == "b":
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="red", tags="")
                elif status == "s":
                    print "start:", [x, y]
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="orange", fill="orange", tags="")
                elif status == "g":
                    print "goal:", [x, y]
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="pink", fill="pink", tags="")


                
                


        

if __name__ == "__main__":
    root=tk.Tk()
    Grid(root).pack(side="top", fill="both", expand="true", padx=5, pady=5)
    root.mainloop()















