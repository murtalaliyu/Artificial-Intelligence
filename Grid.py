import Tile
import Tkinter as tk

root = tk.Tk()

def draw():
    global frame
    frame =tk.Frame(root)
    #frame.pack()

    ID = 1
    status = "1"

    for row in range(120):
        for col in range(160):
            tile = Tile.make_tile(ID, [row, col], status)
            L = tk.Label(frame, text=ID, bg="green")
            L.grid(row=row, column=col, padx='1', pady='1')
            ID += 1
            
draw()
root.mainloop()














