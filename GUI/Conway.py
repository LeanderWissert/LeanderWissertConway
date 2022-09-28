from tkinter import *

class main():
    def __init__(self):
        self.dieGUI = Tk()
        self.labelXSize = 20
        self.labelYSize = 20
        self.rows = 40
        self.cols = 40
        idx = 0
        row = 0
        col = 0

        fieldSize = str(self.labelXSize*self.rows+100)+"x"+str(self.labelYSize*self.cols+100)
        self.dieGUI.geometry(fieldSize)
        self.l = []

        while row < self.rows:
            while col < self.cols:
                self.l.append(Label(master=self.dieGUI)) #bg=""
                self.l[idx].place(x=self.labelXSize*col, y=self.labelYSize*row, width=self.labelXSize,height=self.labelYSize)
                self.l[idx].bind("<Button>", self.onClick)
                col += 1
                idx += 1
            col = 0
            row +=1

    def onClick(self,event):
        idx = self.l.index(event.widget) #// bad but it works
        row = idx // self.cols
        col = idx % self.cols
        color = "SystemButtonFace"
        value = 0#Gamefield.DEAD

        print(event.widget["bg"])
        
        if event.widget["bg"] == "SystemButtonFace":
            color = "black"
            value = 1#Gamefield.ALIVE
        
        event.widget["bg"] = color
      #  self.currentField.set(value, row, col)

    def start(self):
        self.dieGUI.mainloop()
        
conway = main()
conway.start()