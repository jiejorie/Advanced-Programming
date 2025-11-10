from tkinter import*
from tkinter import ttk

# runs mainloop() if called
def main():
    gui = MyGUI()
    gui.mainloop()

# holds primary GUI
class MyGUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("600x570")

        # widgets
        # title text
        self.calc_title = Label(self, text="Calculator", font=("Arial", 20, "bold")).pack(pady=20, anchor="n")
        # first and second number entries
        self.Entries = Entries(self)
        self.Entries.pack(pady=10, anchor="center")
        # pick an operation
        self.pick_txt = Label(self, text="Pick an operation:", font=("Arial", 10)).pack(pady=10, anchor="center")
        self.Operations = Operations(self)
        self.Operations.pack(pady=10, anchor="center")
        # answer segment
        self.answer_title = Label(self, text="Answer:", font=("Arial", 15, "bold")).pack(pady=15, anchor="center")
        self.answer = Label(self, text="...", font=("Arial", 10, "bold"), bg="white", fg="black")
        self.answer.pack(pady=5, ipadx=80, ipady=10, anchor="center")

    # adds the two numbers
    def addition(self):
        self.answer.configure(text="")
        self.num1 = float(self.Entries.first_num.get())
        self.num2 = float(self.Entries.second_num.get())
        self.sum = self.num1 + self.num2
        self.answer.configure(text=f"{self.sum:.2f}", relief="solid")

    # subtracts the two numbers
    def subtraction(self):
        self.answer.configure(text="")
        self.num1 = float(self.Entries.first_num.get())
        self.num2 = float(self.Entries.second_num.get())
        self.difference = self.num1 - self.num2
        self.answer.configure(text=f"{self.difference:.2f}", relief="solid")

    # multiplies the two numbers
    def multiplication(self):
        self.answer.configure(text="")
        self.num1 = float(self.Entries.first_num.get())
        self.num2 = float(self.Entries.second_num.get())
        self.product = self.num1 * self.num2
        self.answer.configure(text=f"{self.product:.2f}", relief="solid")

    # divides the two numbers
    def division(self):
        self.answer.configure(text="")
        self.num1 = float(self.Entries.first_num.get())
        self.num2 = float(self.Entries.second_num.get())
        self.quotient = self.num1 / self.num2
        self.answer.configure(text=f"{self.quotient:.2f}", relief="solid")

    # find the remainder of the two numebers
    def modulo(self):
        self.answer.configure(text="")
        self.num1 = float(self.Entries.first_num.get())
        self.num2 = float(self.Entries.second_num.get())
        self.remainder = self.num1 % self.num2
        self.answer.configure(text=f"{self.remainder:.2f}", relief="solid")

# holds operation buttons
class Operations(ttk.Frame):
    # allows inheritance
    def __init__(self, parent):
        super().__init__(parent)
        # initialize important variables
        self.parent = parent
        self.operation = StringVar(value="")
        self.operation.set("")

        # styling
        self.s = ttk.Style()
        self.s.configure("TButton", font=('Arial', 10), foreground="black", borderwidth=0)

        # widgets
        # addition button
        self.addition = ttk.Button(self, text="Addition", style="TButton", command=self.parent.addition)
        self.addition.grid(row=0, column=0, padx=5, pady=5, ipadx=10, ipady=5)
        # subtraction button
        self.subtraction = ttk.Button(self, text="Subtraction",  style="TButton", command=self.parent.subtraction)
        self.subtraction.grid(row=0, column=1, padx=5, pady=5, ipadx=10, ipady=5)
        # multiplication button
        self.multiplication = ttk.Button(self, text="Multiplication", style="TButton", command=self.parent.multiplication)
        self.multiplication.grid(row=0, column=2, padx=5, pady=5, ipadx=10, ipady=5)
        # division button
        self.division = ttk.Button(self, text="Division", style="TButton", command=self.parent.division)
        self.division.grid(row=1, column=0, columnspan=2, padx=5, pady=5, ipadx=10, ipady=5)
        # modulo button
        self.modulo = ttk.Button(self, text="Modulo Division", style="TButton", command=self.parent.modulo)
        self.modulo.grid(row=1, column=1, columnspan=2, padx=5, pady=5, ipadx=10, ipady=5)

# holds first and second number entries
class Entries(ttk.Frame):
    # allows inheritance
    def __init__(self,parent):
        super().__init__(parent)

        # widgets
        # first number
        self.first_text = Label(self, text="Enter first number: ", font=("Arial", 10)).pack(fill="x", expand=True, padx=100, pady=5)
        self.first_num = ttk.Entry(self, width= 30)
        self.first_num.pack(fill="x", expand=True, padx=100, pady=10)
        # second number
        self.second_text = Label(self, text="Enter second number: ", font=("Arial", 10)).pack(fill="x", expand=True, padx=100, pady=5)
        self.second_num = ttk.Entry(self, width= 30)
        self.second_num.pack(fill="x", expand=True, padx=100, pady=10)

# calls main() is script is directly being run
if __name__ == "__main__":
    main()
