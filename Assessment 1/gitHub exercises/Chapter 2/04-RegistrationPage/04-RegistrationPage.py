from tkinter import*
from PIL import ImageTk, Image
from tkinter import ttk

def main():
    gui = MyGUI()
    gui.mainloop()

class MyGUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("Registration")
        self.geometry("340x600")
        self.minsize(340, 650)
        self.maxsize(340, 650)
        self.configure(bg="white")

        self.img = Image.open("C:/Users/Marcelo/Documents/Margie CC L5/Advanced Programming/Assessment 1/gitHub exercises/Chapter 2/04-RegistrationPage/bsu_banner.jpg").resize((340,107))
        self.img = ImageTk.PhotoImage(self.img)

        self.banner = Label(self, image=self.img).pack(anchor="n")

        self.Form = Form(self)
        self.Form.pack(anchor="center",fill="both", expand=True, pady=15, padx=30)


class Form(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(bg="#f5f5f6")
        
        self.columnconfigure(0, weight=1)
        self.Heading = Heading(self)
        self.Heading.grid(row=0, column=0, pady=5)

        self.Entries = Entries(self)
        self.Entries.grid(row=1, column=0, pady=5)
        
        self.Course = Course(self)
        self.Course.grid(row=2, column=0, pady=5)
        
        self.Languages = Languages(self)
        self.Languages.grid(row=3, column=0, pady=5)
        
        self.Rate = Rate(self)
        self.Rate.grid(row=4, column=0, pady=5)
        
        self.submit_button = Button(self, text="Submit", font=("Segoe UI", 9), bg="#23273e", fg="#f5f5f6", relief="flat")
        self.submit_button.grid(row=5, column=0, padx=10, sticky="w", ipadx=35, ipady=5)

        self.clear_button = Button(self, text="Clear", font=("Segoe UI", 9), bg="#23273e", fg="#f5f5f6", relief="flat")
        self.clear_button.grid(row=5, column=0, padx=10, sticky="e", ipadx=35, ipady=5)

class Heading(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(bg="#f5f5f6")

        self.title = Label(self, text="Student Management System", font=("Segoe UI", 13, "bold"), fg="#23273e", bg="#f5f5f6").pack(side="top")
        self.desc = Label(self, text="New Student Registration", font=("Segoe UI", 11, "bold"), fg="#23273e", bg="#f5f5f6").pack(side="bottom")

class Entries(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(bg="#f5f5f6")

        self.Student_Name_txt = Label(self, text="Student Name:", font=("Segoe UI", 9), fg="#23273e", bg="#f5f5f6").grid(row=0, column=0, sticky="e")
        self.entry1 = Entry(self, bg="#adaeb7", bd=5, relief="flat")
        self.entry1.grid(row=0, column=1, sticky="ew", padx=10, pady=5)
        
        self.Mobile_Number_txt = Label(self, text="Mobile Number:", font=("Segoe UI", 9), fg="#23273e", bg="#f5f5f6").grid(row=1, column=0, sticky="e")
        self.entry2 = Entry(self, bg="#adaeb7", bd=5, relief="flat")
        self.entry2.grid(row=1, column=1, sticky="ew", padx=10, pady=5)
        
        self.Email_txt = Label(self, text="Email ID:", font=("Segoe UI", 9), fg="#23273e", bg="#f5f5f6").grid(row=2, column=0, sticky="e")
        self.entry3 = Entry(self, bg="#adaeb7", bd=5, relief="flat")
        self.entry3.grid(row=2, column=1, sticky="ew", padx=10, pady=5)
         
        self.Address_txt = Label(self, text="Home Address:", font=("Segoe UI", 9), fg="#23273e", bg="#f5f5f6").grid(row=3, column=0, sticky="e")
        self.entry4 = Entry(self, bg="#adaeb7", bd=5, relief="flat")
        self.entry4.grid(row=3, column=1, sticky="ew", padx=10, pady=5)
        
        self.Gender_txt = Label(self, text="Gender:", font=("Segoe UI", 9), fg="#23273e", bg="#f5f5f6").grid(row=4, column=0, sticky="e")

        self.arrow = ImageTk.PhotoImage(Image.open("C:/Users\Marcelo/Documents/Margie CC L5/Advanced Programming/Assessment 1/gitHub exercises/Chapter 2/04-RegistrationPage/arrow.png"))

        self.gender_options = ["Male", "Female", "Other"]
        self.value = StringVar(self)
        self.value.set("")

        self.menu = OptionMenu(self, self.value, *self.gender_options)
        self.menu.grid(row=4, column=1, sticky="ew", padx=10, pady=5, ipady=3, ipadx=10)

        self.menu.config(bg="#adaeb7", bd=0, activebackground="#c5c7d0", indicatoron=0)
        self.symbol = Label(self, image=self.arrow, bg="#adaeb7").place(relx=0.835, rely=0.815)

class Course(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.s = ttk.Style()
        self.s.configure("Frame.TFrame", background= "#f5f5f6")
        self.config(style="Frame.TFrame")

        self.course = StringVar(value="")
        self.course.set("")

        self.s.configure("radiobutton.TRadiobutton", font=("Segoe UI", 9), background="#f5f5f6")

        self.courses_txt = Label(self, text="Course Enrolled:", font=("Segoe UI", 9), fg="#23273e", bg="#f5f5f6").grid(row=0, column=0, padx=5)
        self.cc_button = ttk.Radiobutton(self, text="BSc CC",variable=self.course, value="BSc CC", style="radiobutton.TRadiobutton").grid(row=0, column=1, sticky="w")
        self.cy_button = ttk.Radiobutton(self, text="BSc CY",variable=self.course, value="BSc CY", style="radiobutton.TRadiobutton").grid(row=0, column=2, padx=5, sticky="w")
        self.psy_button = ttk.Radiobutton(self, text="BSc PSY",variable=self.course, value="BSc PSY", style="radiobutton.TRadiobutton").grid(row=1, column=1, sticky="w")
        self.bm_button = ttk.Radiobutton(self, text="BA & BM",variable=self.course, value="BA & BM", style="radiobutton.TRadiobutton").grid(row=1, column=2, padx=5, sticky="w")

class Languages(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.s = ttk.Style()
        self.s.configure("Frame.TFrame", background= "#f5f5f6")
        self.config(style="Frame.TFrame")
        
        self.eng_language = StringVar(value="")
        self.tag_language = StringVar(value="")
        self.hin_urd_language = StringVar(value="")

        self.lang_known_txt = Label(self, text="Languages known:", font=("Segoe UI", 9), fg="#23273e", bg="#f5f5f6").grid(row=0, column=0, padx=5)

        self.s.configure("check.TCheckbutton", background="#f5f5f6")

        self.english_check = ttk.Checkbutton(self, text="English", variable= self.eng_language, style="check.TCheckbutton").grid(row=0, column=1, sticky="w")
        self.tagalog_check = ttk.Checkbutton(self, text="Tagalog", variable= self.tag_language, style="check.TCheckbutton").grid(row=0, column=2, sticky="w")
        self.hindu_urdu_check = ttk.Checkbutton(self, text="Hindu/Urdu", variable= self.hin_urd_language, style="check.TCheckbutton").grid(row=1, column=1, columnspan=2, sticky="w")

class Rate(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.s = ttk.Style()
        self.s.configure("Frame.TFrame", background= "#f5f5f6")
        self.config(style="Frame.TFrame")     

        self.s.configure("TScale", slidercolor="#23273e", background="#f5f5f6")
        self.rate_txt = Label(self, text="Rate your English communication skills:", font=("Segoe UI", 9), fg="#23273e", bg="#f5f5f6").grid(row=0, column=0, pady=5)
        self.scale = ttk.Scale(self, from_=0, to=100, orient=HORIZONTAL, style="TScale")
        self.scale.grid(row=1, column=0, pady=5)  

if __name__ == "__main__":
    main()
