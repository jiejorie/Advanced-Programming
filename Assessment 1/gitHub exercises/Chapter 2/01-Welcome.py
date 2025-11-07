from tkinter import*
from tkinter import ttk

def main():
    gui = MyGUI()
    gui.mainloop()

class MyGUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("Welcome")
        self.geometry("300x300")
        self.minsize(300, 300)
        self.maxsize(300, 300)
        self.configure(background="black")


        self.style = ttk.Style()
        self.style.configure("label.TLabel", font=("Segoe UI", 25, "bold"), foreground="white", background="black")

        self.label = ttk.Label(self, text="Welcome", style="label.TLabel")
        self.label.pack(pady=50)

if __name__ == "__main__":
    main()
