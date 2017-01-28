from tkinter import *

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Heuristic Search")
        self.pack(fill=BOTH, expand=1)

<<<<<<< HEAD
        playButton = Button(self, text="Play", command=self.start_engine)
        playButton.place(x=200, y=200)

        quitButton = Button(self, text="Quit", command=self.client_exit)
        quitButton.place(x=250, y=500)

    def start_engine(self):
        for gridX in range(160):
            for gridY in range(120):
                print(gridX, gridY)
            print(gridX)
=======
        quitButton = Button(self, text="Quit", command=self.client_exit)
        quitButton.place(x=500, y=500)
>>>>>>> 48fe35c0fb3ffab8fa099744eaaf7f25bd8423d2

    def client_exit(self):
        exit()

root = Tk()
root.geometry("600x600")

app = Window(root)
root.mainloop()
