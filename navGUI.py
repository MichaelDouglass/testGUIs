from tkinter import *
from tkinter import ttk

class buildGUI():
    def __init__(self, master):
        self.master = master

        self._createGUI()

        self.master.bind('<Left>', lambda e: self.moveStep(0))
        self.master.bind('<Right>', lambda e: self.moveStep(1))
        self.master.bind('<Up>', lambda e: self.moveStep(2))
        self.master.bind('<Down>', lambda e: self.moveStep(3))

    def _createGUI(self):

        # configure GUI Style
        self.master.title('PI Actuator Navigation Screen')
        self.master.geometry('640x480+600+250')
        self.master.resizable(False, False)

        # title Frame
        self.titleFrame =  ttk.Frame(self.master)
        self.titleFrame.pack(side=TOP)
        title = ttk.Label(self.titleFrame, text='Welcome to the Navigation User '
                  'Interface', font=('Arial', 18))
        title.pack(side=TOP, pady=10)

        # navigation frame
        self.navFrame =  ttk.Frame(self.master)
        self.navFrame.pack(side=TOP)

        self.stepSize = IntVar()
        self.stepSize.set(1)
        self.stepEntry = ttk.Entry(self.navFrame, textvariable=self.stepSize)
        self.stepEntry.grid(row=0, column=4)

        OPTIONS = ['milli', 'micro', 'nano']
        self.stepMod = StringVar()
        self.stepModd = ttk.OptionMenu(self.navFrame, self.stepMod,
                                       OPTIONS[0], *OPTIONS)

        self.stepModd.grid(row=1, column=4)

        ttk.Button(self.navFrame, text='LEFT',
                   command=lambda: self.moveStep(0)).grid(row=1, column=0)
        ttk.Button(self.navFrame, text='RIGHT',
                   command=lambda: self.moveStep(1)).grid(row=1, column=3)
        ttk.Button(self.navFrame, text='UP',
                   command=lambda: self.moveStep(2)).grid(row=0, column=2)
        ttk.Button(self.navFrame, text='DOWN',
                   command=lambda: self.moveStep(3)).grid(row=2, column=2)


        # Position frame
        self.storeFrame = ttk.Frame(self.master)
        self.storeFrame.pack(side=TOP)

        # The Focus Position is read from the actuator
        ttk.Label(self.storeFrame, text='Focus Position (mm): ').grid(row=0, column=0)
        self.showMainVar = DoubleVar()
        self.showMainVar.set('Placeholder Position')
        self.showMainEnt = ttk.Entry(self.storeFrame,
                             textvariable=self.showMainVar)
        self.showMainEnt.grid(row=1, column=0)

        # The Lateral Position is read from the actuator
        ttk.Label(self.storeFrame, text='Lateral Position (mm): ').grid(row=0, column=3)
        self.showSlaveVar = DoubleVar()
        self.showSlaveVar.set('Placeholder Position')
        self.showSlaveEnt = ttk.Entry(self.storeFrame,
                             textvariable=self.showSlaveVar)
        self.showSlaveEnt.grid(row=1, column=3)

        # HUD for MoveTo
        self.chooseFrame = ttk.Frame(self.master)
        self.chooseFrame.pack(side=TOP)

        ttk.Label(self.chooseFrame, text='Enter a position (mm): ',
                   font=('Arial', 12)).grid(row=0, column=0, columnspan=2)
        ttk.Label(self.chooseFrame, text='Up/Down: ').grid(row=1, column=0)
        ttk.Label(self.chooseFrame, text='Lateral: ').grid(row=1, column=1)

        self.choosePosY = DoubleVar()
        self.choosePosY.set(2.5)
        self.choosePosYEnt = ttk.Entry(self.chooseFrame, textvariable=self.choosePosY)
        self.choosePosYEnt.grid(row=2, column=0)

        self.choosePosX = DoubleVar()
        self.choosePosX.set(2.5)
        self.choosePosXEnt = ttk.Entry(self.chooseFrame, textvariable=self.choosePosX)
        self.choosePosXEnt.grid(row=2, column=1)

        ttk.Button(self.chooseFrame, text='GO!',
                   command=lambda: self.moveTo()).grid(row=3, column=0, columnspan=2)

        # Saved Positions
        self.savedFrame = ttk.Frame(self.master)
        self.savedFrame.pack(side=TOP)

        # Saved Position1
        ttk.Label(self.savedFrame, text='Position 1: ').grid(row=0, column=0)

        self.choosePosY1 = DoubleVar()
        self.choosePosY1Ent = ttk.Entry(self.savedFrame, textvariable=self.choosePosY1)
        self.choosePosY1Ent.grid(row=0, column=1)

        self.choosePosX1 = DoubleVar()
        self.choosePosX1Ent = ttk.Entry(self.savedFrame, textvariable=self.choosePosX1)
        self.choosePosX1Ent.grid(row=0, column=2)

        ttk.Button(self.savedFrame, text='Save',
                   command=lambda: self.savePos(0)).grid(row=0, column=3)

        ttk.Button(self.savedFrame, text='GO!',
                   command=lambda: self.moveToSet(0)).grid(row=0, column=4)

        # Saved Position2
        ttk.Label(self.savedFrame, text='Position 2: ').grid(row=1, column=0)

        self.choosePosY2 = DoubleVar()
        self.choosePosY2Ent = ttk.Entry(self.savedFrame, textvariable=self.choosePosY2)
        self.choosePosY2Ent.grid(row=1, column=1)

        self.choosePosX2 = DoubleVar()
        self.choosePosX2Ent = ttk.Entry(self.savedFrame, textvariable=self.choosePosX2)
        self.choosePosX2Ent.grid(row=1, column=2)

        ttk.Button(self.savedFrame, text='Save',
                   command=lambda: self.savePos(1)).grid(row=1, column=3)

        ttk.Button(self.savedFrame, text='GO!',
                   command=lambda: self.moveToSet(1)).grid(row=1, column=4)

        # Saved Position3
        ttk.Label(self.savedFrame, text='Position 3: ').grid(row=2, column=0)

        self.choosePosY3 = DoubleVar()
        self.choosePosY3Ent = ttk.Entry(self.savedFrame, textvariable=self.choosePosY3)
        self.choosePosY3Ent.grid(row=2, column=1)

        self.choosePosX3 = DoubleVar()
        self.choosePosX3Ent = ttk.Entry(self.savedFrame, textvariable=self.choosePosX3)
        self.choosePosX3Ent.grid(row=2, column=2)

        ttk.Button(self.savedFrame, text='Save',
                   command=lambda: self.savePos(2)).grid(row=2, column=3)

        ttk.Button(self.savedFrame, text='GO!',
                   command=lambda: self.moveToSet(2)).grid(row=2, column=4)


    def moveStep(self, n):
        moveDict = {0:('Left', -1),
                    1: ('Right', 1),
                    2: ('Up', 1),
                    3: ('Down', -1)}
        modDict = {'milli': 1,
                   'micro': 10**-3,
                   'nano': 10**-6}

        direct = moveDict[n]
        stR = direct[0]

        step = self.stepSize.get()
        mod = modDict[self.stepMod.get()]

        try:
            print('Move '+stR)
            print('by '+str(step*mod)+' mm')
        except e:
            print('You\'ve gone too far'
                  ' this time.')

    def moveTo(self):
        xPos = self.choosePosX.get()
        yPos = self.choosePosY.get()
        try:
            print('Moving to '+str(xPos)+' in x-axis')
            print('Moving to '+str(yPos)+' in y-axis')
        except:
            print('Whoops, you\'ve gone too far again...')

    def savePos(self, n):
        entriesY = [self.choosePosY1, self.choosePosY2, self.choosePosY3]
        entriesX = [self.choosePosX1, self.choosePosX2, self.choosePosX3]
        entriesY[n].set('0.456')
        entriesX[n].set('0.366')

    def moveToSet(self, n):
        entriesY = [self.choosePosY1, self.choosePosY2, self.choosePosY3]
        entriesX = [self.choosePosX1, self.choosePosX2, self.choosePosX3]
        yPos = entriesY[n].get()
        xPos = entriesX[n].get()
        try:
            print('Moving to '+str(xPos)+' in x-axis')
            print('Moving to '+str(yPos)+' in y-axis')
        except:
            print('Whoops, you\'ve gone too far again...')

def main():
    root = Tk()
    app = buildGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
