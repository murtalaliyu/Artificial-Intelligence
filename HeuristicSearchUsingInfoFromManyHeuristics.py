from tkinter import *

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Heuristic Search")
        self.pack(fill=BOTH, expand=1)

        quitButton = Button(self, text="Quit", command=self.client_exit)
        quitButton.place(x=500, y=500)

    def client_exit(self):
        exit()

root = Tk()
root.geometry("600x600")

app = Window(root)
root.mainloop()
