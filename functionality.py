import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class MInterface:

    def __init__(self):

        self.window = tk.Tk()
        self.window.title("Traveling Accountant")
        self.window.minsize(width=300, height=300)

        self.fdtx1 = 1027.5
        self.fdtx2 = 4807.5
        self.fdtx3 = 15213.5
        self.fdtx4 = 34647.5
        self.fdtx5 = 49335.5
        self.fdtx6 = 162718

        self.sttx1 = 178.13
        self.sttx2 = 562.875
        self.sttx3 = 10673.5

        self.lbhrincm = tk.Label(self.window, text="Hourly Pay")
        self.hrincm = ttk.Entry(self.window, width=10)
        self.lbhrwk = tk.Label(self.window, text="Weekly Hours")
        self.hrwk = ttk.Entry(self.window, width=10)

        self.sgrt = 0
        self.sgrttx = 0
        self.strsgrt = tk.StringVar()
        self.strsgrt.set("$0.00\n")
        self.avgut = 350

        self.mthinm = 0
        self.mthtx = 0
        self.strmthincom = tk.StringVar()
        self.strmthincom.set("$0.00\n")

        self.wkincm = 0
        self.wktx = 0
        self.strwkicm = tk.StringVar()
        self.strwkicm.set("$0.00\n")

        self.sy = 0
        self.sytx = 0
        self.strsy = tk.StringVar()
        self.strsy.set("$0.00\n")

        # Show "Salary"
        self.syds = tk.Label(self.window, text="Salary", font=('Arial', 15))
        self.syds.pack()
        self.sydsvu = tk.Label(self.window, textvariable=self.strsy, font=('Arial', 18))
        self.sydsvu.pack()

        # Show "Monthy Income"
        self.lbdswkincm = tk.Label(self.window, text="Monthly Income", font=('Arial', 15))
        self.lbdswkincm.pack()
        self.dsmthincom = tk.Label(self.window, textvariable=self.strmthincom, font=('Arial', 18))
        self.dsmthincom.pack()

        # Show "Weekly Income"
        self.lbdswkincm = tk.Label(self.window, text="Weekly Income", font=('Arial', 15))
        self.lbdswkincm.pack()
        self.dswkincom = tk.Label(self.window, textvariable=self.strwkicm, font=('Arial', 18))
        self.dswkincom.pack()

        # Show "Rent Suggestion"
        self.sugrent = tk.Label(self.window, text="Max Rent", font=('Arial', 15))
        self.sugrentxp = tk.Label(self.window, text="(1/3 of Monthly Income, without Util.)", font=('Arial', 10))
        self.sugrent.pack()
        self.sugrentxp.pack()
        self.sgrent = tk.Label(self.window, textvariable=self.strsgrt, font=('Arial', 18))
        self.sgrent.pack()

        # Display "Hourly Pay" Label and Entry box
        self.lbhrincm.pack()
        self.hrincm.pack()
        # Display "Weekly Hours" Label line and Entry box
        self.lbhrwk.pack()
        self.hrwk.pack()

        # Calculation buttons, w/ and w/out tax
        self.wkicmbtn = tk.Button(self.window, text="Gross Income", font=('Arial', 13),
                                  command=self.salary)
        self.wkicmbtn.pack()

        self.wkicmtxbtn = tk.Button(self.window, text="Net Income", font=('Arial', 13),
                                    command=self.withtax)
        self.wkicmtxbtn.pack()

        self.window.protocol("WM_DELETE_WINDOW", self.cl)
        self.window.mainloop()

    def setincomeds(self):
        self.strwkicm.set(f'$ {self.wkincm:0.2f}\n')
        self.strsy.set(f'$ {self.sy:0.2f}\n')
        self.strmthincom.set(f'$ {self.mthinm:0.2f}\n')
        self.strsgrt.set(f'$ {self.sgrt:0.2f}\n')

    def setincomedstx(self):
        self.wktx = self.sytx / 52
        self.mthtx = self.wktx * 4
        self.sgrttx = self.mthtx / 3
        self.strwkicm.set(f'$ {self.wktx:0.2f}\n')
        self.strsy.set(f'$ {self.sytx:0.2f}\n')
        self.strmthincom.set(f'$ {self.mthtx:0.2f}\n')
        self.strsgrt.set(f'$ {self.sgrttx:0.2f}\n')

    def salary(self):
        self.sy = float(self.hrincm.get()) * int(self.hrwk.get()) * 52
        self.wkincm = self.sy / 52
        self.mthinm = self.wkincm * 4
        self.sgrt = self.mthinm / 3
        self.setincomeds()
        print(self.strwkicm.get())
        print(self.wkincm)
        print(self.sy)

    def withtax(self):
        if self.sy <= 3750:
            self.sytx = self.sy * (1 - 0.0475 - 0.1)
            self.setincomedstx()
        elif self.sy <= 9450:
            self.sytx = self.sy - self.sttx1 - ((self.sy - 3750) * (0.1 + 0.0675))
            self.setincomedstx()
        elif self.sy <= 10275:
            self.sytx = self.sy - self.sttx2 - ((self.sy - 9450) * (0.1 + 0.0875))
            self.setincomedstx()
        elif self.sy <= 41775:
            self.sytx = self.sy - self.sttx2 - self.fdtx1 - (self.sy - 9450) * 0.0875 - (self.sy - 10275) * 0.12
            self.setincomedstx()
        elif self.sy <= 89075:
            self.sytx = self.sy - self.sttx2 - self.fdtx2 - (self.sy - 9450) * 0.0875 - (self.sy - 41775) * 0.22
            self.setincomedstx()
        elif self.sy <= 125000:
            self.sytx = self.sy - self.sttx2 - self.fdtx3 - (self.sy - 9450) * 0.0875 - (self.sy - 89075) * 0.24
            self.setincomedstx()
        elif self.sy <= 170050:
            self.sytx = self.sy - self.sttx3 - self.fdtx3 - (self.sy - 125000) * 0.0975 - (self.sy - 89075) * 0.24
            self.setincomedstx()
        elif self.sy <= 215950:
            self.sytx = self.sy - self.sttx3 - self.fdtx4 - (self.sy - 125000) * 0.0975 - (self.sy - 170050) * 0.32
            self.setincomedstx()
        elif self.sy <= 539900:
            self.sytx = self.sy - self.sttx3 - self.fdtx5 - (self.sy - 125000) * 0.0975 - (self.sy - 215950) * 0.35
            self.setincomedstx()
        elif self.sy > 539900:
            self.sytx = self.sy - self.sttx3 - self.fdtx6 - (self.sy - 125000) * 0.0975 - (self.sy - 539900) * 0.37
            self.setincomedstx()
        else:
            print("error")

    def cl(self):
        if messagebox.askyesno(title="Exit", message="Are you sure you want to Exit?"):
            print("Ending")
            self.window.destroy()


MInterface()
