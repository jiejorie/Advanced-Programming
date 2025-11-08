from tkinter import*
from tkinter import messagebox

def main():
    gui = MyGUI()
    gui.mainloop()

class MyGUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("Log-in")
        self.geometry("600x300")
        self.maxsize(600, 300)

        self.columnconfigure(0, weight=1)

        self.frame1 = frame1(self)
        self.frame1.grid(row=0, column=0, pady=15)

        self.frame2 = frame2(self)
        self.frame2.grid(row=1, column=0, pady=5)

        self.frame3 = frame3(self)
        self.frame3.grid(row=2, column=0, pady=5)

        self.button = Button(self, text="Log-in", command=self.login_successful, width=16)
        self.button.grid(row=3, column=0, pady=10)
    
    def login_successful(self):
        messagebox.askyesno("Log-in successful!", "Remember password?")
        messagebox.showinfo("Log-in successful!", "Welcome back!")
        self.destroy()

class frame1(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.log_in_txt = Label(self, text="Log-in", font=("Arial", 20, "bold")).grid(row=0, column=0, pady=5)
        self.desc_txt = Label(self, text="Please enter your Log-in details").grid(row=1, column=0)

class frame2(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.user_name = Label(self, text="Username*", font=("Arial", 10)).grid(row=0, column=0, sticky="ew")
        self.entry1 = Entry(self)
        self.entry1.grid(row=1, column=0, sticky="ew")

class frame3(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.rowconfigure((0,1), weight=1)
        self.password = Label(self, text="Password*", font=("Arial", 10)).grid(row=0, column=0, sticky="ew")
        self.entry2 = Entry(self, show="*")
        self.entry2.grid(row=1, column=0, sticky="ew")
        self.check = Checkbutton(self, text='show password', command=self.show)
        self.check.grid(row=2, column=0, pady=5)
    
    def show(self):
        self.entry2.configure(show='')
        self.check.configure(command=self.hide, text='hide password')

    def hide(self):
        self.entry2.configure(show='*')
        self.check.configure(command=self.show, text='show password')

if __name__ == "__main__":
    main()
