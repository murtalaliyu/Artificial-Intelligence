import Tile
import Tkinter as tk

root = tk.Tk()

def draw():
    global gameframe
    gameframe =tk.Frame(root)
    gameframe.pack()

    ID = 1
    status = "1"

    for row in range(10):
        for col in range(10):
            tile = Tile.make_tile(ID, [row, col], status)
            L = tk.Label(gameframe, text=status, bg="green")
            L.grid(row=row, column=col, padx='1', pady='1')
            ID += 1
            
draw()
root.mainloop()














