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

        self.wkincm = 0
        self.wktx = 0
        self.strwkicm = tk.StringVar()
        self.strwkicm.set("$0.00")

        self.sy = 0
        self.sytx = 0
        self.strsy = tk.StringVar()
        self.strsy.set("$0.00")

        # How "Salary"
        self.syds = tk.Label(self.window, text="Salary", font=('Arial', 15))
        self.syds.pack()
        self.sydsvu = tk.Label(self.window, textvariable=self.strsy, font=('Arial', 18))
        self.sydsvu.pack()

        # Show "Weekly Income"
        self.lbdswkincm = tk.Label(self.window, text="Weekly Income", font=('Arial', 15))
        self.lbdswkincm.pack()
        self.dswkincom = tk.Label(self.window, textvariable=self.strwkicm, font=('Arial', 18))
        self.dswkincom.pack()

        # Display "Hourly Pay" Label and Entry box
        self.lbhrincm.pack()
        self.hrincm.pack()
        # Display "Weekly Hours" Label line and Entry box
        self.lbhrwk.pack()
        self.hrwk.pack()

        # Calculation buttons, w/ and w/out tax
        self.wkicmbtn = tk.Button(self.window, text="Calculate Without Tax", font=('Arial', 15),
                                  command=self.salary)
        self.wkicmbtn.pack()

        self.wkicmtxbtn = tk.Button(self.window, text="Calculate With Tax", font=('Arial', 15),
                                    command=self.withtax)
        self.wkicmtxbtn.pack()

        self.window.protocol("WM_DELETE_WINDOW", self.cl)
        self.window.mainloop()

    def setincomeds(self):
        self.wkincm = round(self.wkincm, 2)
        self.strwkicm.set(f'$ {self.wkincm:0.2f}')
        self.sy = round(self.sy, 2)
        self.strsy.set(f'$ {self.sy:0.2f}')

    def setincomedstx(self):
        self.wktx = self.sytx / 52
        self.strwkicm.set(f'$ {self.wktx:0.2f}')
        self.strsy.set(f'$ {self.sytx:0.2f}')

    def salary(self):
        self.sy = float(self.hrincm.get()) * int(self.hrwk.get()) * 52
        self.wkincm = self.sy / 52
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
