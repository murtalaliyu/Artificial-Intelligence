import Tile
import Tkinter as tk

root = tk.Tk()

def draw():
    global frame
    frame = tk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=1)

    ID = 1
    status = "1"

    for row in range(50):
        for col in range(50):
            tile = Tile.make_tile(ID, [row, col], status)
            cell = tk.Label(frame, text=[row, col], bg="green")
            cell.grid(row=row, column=col, padx='1', pady='1')
            ID += 1
            
draw()
root.mainloop()














