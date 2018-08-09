from tkinter import *
from tkinter import ttk

class buildGUI():
    def __init__(self, master):
        self.master = master

        self._createGUI()

        self.master.bind('<Left>', lambda e: self.left_move())
        self.master.bind('<Right>', lambda e: self.right_move())
        self.master.bind('<Up>', lambda e: self.up_move())
        self.master.bind('<Down>', lambda e: self.down_move())

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
                   command=lambda: self.move(0)).grid(row=1, column=0)
        ttk.Button(self.navFrame, text='RIGHT',
                   command=lambda: self.move(1)).grid(row=1, column=3)
        ttk.Button(self.navFrame, text='Focus Away',
                   command=lambda: self.move(2)).grid(row=0, column=2)
        ttk.Button(self.navFrame, text='Focus To',
                   command=lambda: self.move(3)).grid(row=2, column=2)


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

        # HUD for Movement?
        self.chooseFrame = ttk.Frame(self.master)
        self.chooseFrame.pack(side=TOP)

    def move(self, n):
        moveDict = {0:('Left', -1),
                    1: ('Right', 1),
                    2: ('Up', 1),
                    3: ('Down', -1)}
        modDict = {'milli': 1,
                   'micro': 10**-3,
                   'nano': 10**-6}

        direct = moveDict[n]
        stR = direct[0]
        print(stR)

def main():
    root = Tk()
    app = buildGUI(root)
    root.mainloop()

if __name__ == '__main__':
main()
