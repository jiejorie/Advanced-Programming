from tkinter import*
from tkinter import ttk

def main():
    gui = MyGUI()
    gui.mainloop()

class MyGUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("Greeting App")
        self.geometry("400x400")
        self.maxsize(400, 400)

        self.InputFrame = InputFrame(self)
        self.InputFrame.pack(side="top", fill="both", expand=True, anchor="n")
        
        self.DisplayFrame = DisplayFrame(self)
        self.DisplayFrame.pack(side="bottom", fill="both", expand=True, anchor="s")

    def update_greeting(self):
        self.name = self.InputFrame.username.get().title()
        self.value = self.InputFrame.value.get()
        self.DisplayFrame.greeting.configure(text=f"Greetings, {self.name}!", fg=self.value)

        

class InputFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.config(bg="#FFFF94")

        self.title_lbl = Label(self, text="What is your name?", font=("Segoe UI", 20, "bold"), fg="blue", bg="#FFFF94").pack(side="top", pady=20)

        self.username = Entry(self, width=28, font=("Segoe UI", 10), relief="flat", bd=10)
        self.username.pack(side="top", pady=5)

        self.color_options = ["Red", "Orange", "Gold", "Dark Green", "Blue",  "Purple", "Deep Pink", "Black"]
        self.value = StringVar(self)
        self.value.set("Blue")

        self.color_menu = OptionMenu(self, self.value, *self.color_options)
        self.color_menu.pack(pady=10)

        self.color_menu.config(width=26, height=2, bd=0, bg="blue", fg="white", font=("Segoe UI", 10))

        self.update = Button(self, text="Update greeting", font=("Segoe UI", 10), fg="white", bg="blue", bd=0, width=30, command=self.parent.update_greeting).pack(pady=15, ipady=5)

class DisplayFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.config(bg="#ADFFD6")

        self.greeting = Label(self, text="", font=("Segoe UI", 20, "bold"), bg="#ADFFD6")
        self.greeting.pack(pady=20, anchor="center", side="top")

if __name__ == "__main__":
    main()
