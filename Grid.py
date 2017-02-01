import Tile
import Tkinter as tk
'''
root = tk.Tk()

def draw():
    global frame
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=1)

    #Create scrollbars
    scrollbarX = tk.Scrollbar(frame, bg='grey')
    scrollbarX.activate()

    ID = 1
    status = "1"

    for row in range(50):
        for col in range(50):
            tile = Tile.make_tile(ID, [row, col], status)
            cell = tk.Label(frame, text=tile.status, bg="green")
            cell.grid(row=row, column=col, padx='1', pady='1')
            ID += 1
            
draw()
root.mainloop()
'''






class Example(tk.Frame):
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

    def populate(self):
        ID = 1
        status = "1"

        for row in range(50):
            for col in range(50):
                tile = Tile.make_tile(ID, [row, col], status)
                cell = tk.Label(self.frame, text=tile.ID, bg="green")
                cell.grid(row=row, column=col, padx='1', pady='1')
                ID += 1

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

if __name__ == "__main__":
    root=tk.Tk()
    Example(root).pack(side="top", fill="both", expand=True)
    root.mainloop()







