import Tile
import Gridlist
import Hard
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

        self.canvas.bind("<Configure>", self.populate)
        self.canvas.bind("<Configure>", self.hard_to_traverse)


    
    
    #Create and populate grid    
    def populate(self, event):
        list1 = Gridlist.populate()




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
                
                if list2[(x*160)+y].status == "1":
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="green", tags="")
                elif list2[(x*160)+y].status == "2":
                    self.canvas.create_rectangle(x1, y1, x2, y2, outline="black", fill="yellow", tags="")
        
        
       
    #select the highways 
    def highways():
        pass 
            

if __name__ == "__main__":
    root=tk.Tk()
    Grid(root).pack(side="top", fill="both", expand="true", padx=40, pady=40)
    root.mainloop()

