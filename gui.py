from tkinter import *
from tkinter.ttk import *
import random
import wikipedia


root = Tk()

ny = wikipedia.summary("Cristiano Ronaldo")
#image = ny.summary(sen)
class App():
    def __init__(self, master) -> None:
        self.title = master.title("wiki-art GUI")

        self.search_btn = Button(master, text="Search", command=self.search)
        self.search_btn.grid(column=6, row=0)

        #text box
        self.text_box = Text(master, height=10, width=50, padx=15, pady=15)
        self.text_box.grid(column=0, row=1, columnspan=5, rowspan=3)


        #search
        q = StringVar()
        self.e = Entry(master, textvariable=q)
        self.e.grid(column=0, row=0)
        
        


    def search(self):
        try:
            dis = wikipedia.summary(self.e.get())
            self.text_box.insert(1.0, dis)
            dis.delete("1.0", "end")
        except wikipedia.DisambiguationError:
            text = "Please be more specific"
            self.text_box.insert(1.0, text)



myapp = App(root)

root.mainloop()