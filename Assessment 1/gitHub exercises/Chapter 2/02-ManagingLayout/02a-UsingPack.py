from tkinter import*

# runs the mainloop function
def main():
    gui = MyGui()
    gui.mainloop()

# main App GUI class
class MyGui(Tk):
    def __init__(self):
        super().__init__()
        self.title("GUI Pack Example")
        self.geometry("190x80")
        self.config(bg="#e0e0e0")  

        # widgets
        # 'A' text
        self.txtA = Label(self, text="A", bg="red", bd=6, relief="ridge").pack(fill="x", side="top", anchor="center", expand=1)
        # 'B' text within frame
        self.Frame1 = Frame1(self)
        self.Frame1.pack(side="bottom", anchor="n", fill="x")
        # 'C' and 'D' text within frame
        self.Frame2 = Frame2(self)
        self.Frame2.pack(side="bottom", anchor="s", fill="x")

# this frame holds 'B'
class Frame1(Frame):
    # allows inheritance
    def __init__(self, parent):
        super().__init__(parent)
        self.config(bg="#e0e0e0") 
        self.txtB = Label(self, text="B", bg="yellow", bd=5, relief = "raised", width=13)
        self.txtB.pack(side="bottom", anchor="center")

# this frame holds 'C' and 'D'
class Frame2(Frame):
    # allows inheritance
    def __init__(self, parent):
        super().__init__(parent)
        self.config(bg="#e0e0e0") 
        self.txtD = Label(self, text="D", bg="white", width=13)
        self.txtD.pack(anchor="center", side="right")

        self.txtC = Label(self, text="C", bg="blue", width=13)
        self.txtC.pack(anchor="center")

# calls main() if script is directly running
if __name__ == "__main__":
    main()


