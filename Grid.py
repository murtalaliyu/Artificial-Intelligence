import Tile
import Tkinter as tk
import random

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

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    #Create and populate grid    
    def populate(self):
        ID = 1
        status = "1"
        #make grid list in the form [[a,b,c], [x,y,z]] to save our grid in
        gridList = []

        for row in range(10):
            colList = []
            for col in range(10):
                address = [row, col]
                tile = Tile.make_tile(ID, address, status)
                colList.append([ID, address, status])
                cell = tk.Label(self.frame, text=tile.status, bg="green")
                cell.grid(row=row, column=col, padx='1', pady='1')
                ID += 1
            gridList.append(colList)

        #select 8 coordinates randomly (xrand, yrand)
        for coordinate in range(8):
            Xcoordinate = int(random.random() * 10)
            Ycoordinate = int(random.random() * 10)

            #choose with prob 50% to mark it as a hard to taverse cell
            prob = int(random.random() * 2)
            if prob == 1:
                tile.address = [Xcoordinate, Ycoordinate]
                tile.status = "2"
                cell = tk.Label(self.frame, text=tile.status, bg="yellow")
                cell.grid(row=Xcoordinate, column=Ycoordinate, padx="1", pady="1")
                print tile.status
            

        '''cell = tk.Label(self.frame, text=tile.status, bg="blue")
        cell.grid(row=1, column=1, padx='1', pady='1')'''

if __name__ == "__main__":
    root=tk.Tk()
    Grid(root).pack(side="top", fill="both", expand=True)
    root.mainloop()


