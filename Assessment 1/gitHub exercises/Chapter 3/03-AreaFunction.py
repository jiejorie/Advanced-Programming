from tkinter import*
from tkinter import ttk
from tkinter import messagebox
import math

def main():
    gui = MyGUI()
    gui.mainloop()

class MyGUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("Area Function")
        self.geometry("500x500")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both")

        self.create_tabs()

    def create_tabs(self):
        self.circle_tab = setup_circle(self.notebook)
        self.circle_tab.pack()

        self.square_tab = setup_square(self.notebook)
        self.square_tab.pack()

        self.rect_tab = setup_rectangle(self.notebook)
        self.rect_tab.pack()

        self.notebook.add(self.circle_tab, text="Circle")
        self.notebook.add(self.square_tab, text="Square")
        self.notebook.add(self.rect_tab, text="Rectangle")
        

class setup_circle(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.calc_circle_txt = Label(self, text="Circle Calculator Area", font=("Arial", 20, "bold")).pack(pady=30)

        self.circle_tab_frame = circle_tab_frame(self)
        self.circle_tab_frame.pack(anchor="center", pady=20, padx=5)

    def calc_area(self):
        try:
            self.radius = float(self.circle_tab_frame.radius_entry.get())
            if self.radius <= 0:
                messagebox.showerror("Invalid Input", "Please only enter a positive number.")
            else:
                self.area = math.pi*(self.radius**2)
                self.circle_tab_frame.answer.config(text=f"{self.area:.2f} m²", font=("Arial", 10, "bold"), relief="solid")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please only enter a number.")
               
class circle_tab_frame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.radius_txt = Label(self, text="Radius*", font=("Arial", 13)).grid(row=0, column=0)
        self.radius_entry = Entry(self, font=("Arial", 10))
        self.radius_entry.grid(row=1, column=0, sticky="ew", ipady=5)

        self.calc_area_btn = Button(self, text="Calculate Area", font=("Arial", 13), bd=0, fg="white", bg="black", command=self.parent.calc_area).grid(row=2, column=0, pady=20, sticky="ew", ipady=5)

        self.answer_txt = Label(self, text="Area:", font=("Arial", 13)).grid(row=3, column=0)
        self.answer = Label(self, text="...", font=("Arial", 10), bg="white")
        self.answer.grid(pady=10, ipady=5, row=4, column=0, sticky="ew")

        self.formula = Label(self, text="Formula: Area = π × radius²", font=("Arial", 10), fg="gray").grid(padx=5, pady=15, row=5, column=0, sticky="ew")
        
class setup_square(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.calc_square_txt = Label(self, text="Square Calculator Area", font=("Arial", 20, "bold")).pack(pady=30)
    
        self.square_tab_frame = square_tab_frame(self)
        self.square_tab_frame.pack(anchor="center", pady=20, padx=5)

    def calc_area(self):
        try:
            self.side = float(self.square_tab_frame.side_entry.get())
            if self.side <= 0:
                messagebox.showerror("Invalid Input", "Please only enter a positive number.")
            else:
                self.area = self.side**2
                self.square_tab_frame.answer.config(text=f"{self.area:.2f} m²", font=("Arial", 10, "bold"), relief="solid")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please only enter a positive number.")

class square_tab_frame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.side_txt = Label(self, text="Side Length*", font=("Arial", 13)).grid(row=0, column=0)
        self.side_entry = Entry(self, font=("Arial", 10))
        self.side_entry.grid(row=1, column=0, sticky="ew", ipady=5)

        self.calc_area_btn = Button(self, text="Calculate Area", font=("Arial", 13), bd=0, fg="white", bg="black", command=self.parent.calc_area).grid(row=2, column=0, pady=20, sticky="ew", ipady=5)

        self.answer_txt = Label(self, text="Area:", font=("Arial", 13)).grid(row=3, column=0)
        self.answer = Label(self, text="...", font=("Arial", 10), bg="white")
        self.answer.grid(pady=10, ipady=5, row=4, column=0, sticky="ew")

        self.formula = Label(self, text="Formula: Area = side × side", font=("Arial", 10), fg="gray").grid(padx=5, pady=15, row=5, column=0, sticky="ew")
        
class setup_rectangle(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.calc_rect_txt = Label(self, text="Rectangle Calculator Area", font=("Arial", 20, "bold")).pack(pady=30)

        self.rect_tab_frame = rect_tab_frame(self)
        self.rect_tab_frame.pack(anchor="center", pady=10, padx=5)

    def calc_area(self):
        try:
            self.length = float(self.rect_tab_frame.length_entry.get())
            if self.length <= 0:
                messagebox.showerror("Invalid Input", "Please only enter a positive number.")
            else:
                try:
                    self.width = float(self.rect_tab_frame.width_entry.get())
                    if self.width <= 0:
                       messagebox.showerror("Invalid Input", "Please only enter a positive number.")
                    else: 
                        self.area = self.length*self.width
                        self.rect_tab_frame.answer.config(text=f"{self.area:.2f} m²", font=("Arial", 10, "bold"), relief="solid")
                except ValueError:
                    messagebox.showerror("Invalid Input", "Please only enter a number.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please only enter a number.")

class rect_tab_frame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.length_txt = Label(self, text="Length*", font=("Arial", 13)).grid(row=0, column=0)
        self.length_entry = Entry(self, font=("Arial", 10))
        self.length_entry.grid(row=1, column=0, sticky="ew", ipady=5)
        
        self.space = Label(self, text="", font=("Arial", 5)).grid(row=2, column=0)

        self.width_txt = Label(self, text="Width*", font=("Arial", 13)).grid(row=3, column=0)
        self.width_entry = Entry(self, font=("Arial", 10))
        self.width_entry.grid(row=4, column=0, sticky="ew", ipady=5)

        self.calc_area_btn = Button(self, text="Calculate Area", font=("Arial", 13), bd=0, fg="white", bg="black", command=self.parent.calc_area).grid(row=5, column=0, pady=20, sticky="ew", ipady=5)

        self.answer_txt = Label(self, text="Area:", font=("Arial", 13)).grid(row=6, column=0)
        self.answer = Label(self, text="...", font=("Arial", 10), bg="white")
        self.answer.grid(pady=10, ipady=5, row=7, column=0, sticky="ew")

        self.formula = Label(self, text="Formula: Area = length × width", font=("Arial", 10), fg="gray").grid(padx=5, pady=15, row=8, column=0, sticky="ew")
        
if __name__ == "__main__":
    main()
