from tkinter import*

def main():
    gui = MyGUI()
    gui.mainloop()

class MyGUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("GUI Pack Example")
        self.geometry("300x180")

        self.frame1 = frame1(self)
        self.frame1.pack(side="left", fill="both", expand=True)

        self.frame2 = frame2(self)
        self.frame2.pack(side="right", fill="both", expand=True)

class frame1(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(relief="sunken", bd=5)
        self.label1 = Label(self, text="A", fg="white", bg="#22263d")
        self.label1.pack(side="top", fill="both", expand=True)
        self.label2 = Label(self, text="B")
        self.label2.pack(side="bottom", fill="both", expand=True)

class frame2(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(relief="sunken", bd=5)
        self.label3 = Label(self, text="C")
        self.label3.pack(side="top", fill="both", expand=True)
        self.label4 = Label(self, text="D", fg="white", bg="#22263d")
        self.label4.pack(side="bottom", fill="both", expand=True)

if __name__ == "__main__":
    main()
