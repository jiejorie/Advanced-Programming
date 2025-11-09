from tkinter import*
from tkinter import ttk
import random

def main():
    gui = MyGUI()
    gui.mainloop()

class MyGUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("Draw Shape")
        self.geometry("700x600")

        self.TitleFrame = Frame(self)
        self.TitleFrame.pack(pady=20, anchor="n", side="top", padx=20)

        self.title_txt = Label(self.TitleFrame, text="Draw Shapes!", font=("Arial", 15, "bold")).pack(side="top", anchor="n")
        self.desc_txt = Label(self.TitleFrame, text="To start creating, choose a shape then click on the Canvas!", font=("Arial", 10), fg="gray").pack(side="top", anchor="n")

        self.Pick_Shapes = Pick_shapes(self)
        self.Pick_Shapes.pack(side="top", anchor="n")

        self.canvas = Canvas(self, bg="white", highlightbackground="gray")
        self.canvas.pack(fill="both", expand=True, side="bottom", anchor="center", padx=10, pady=10)

class Pick_shapes(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.oval_btn = Button(self, text="Oval", bg="Dark blue", fg="White", font=("Arial", 13, "bold"), command=self.draw_oval).grid(row=0, column=0, sticky="ew", pady=5, padx=5)
        self.square_btn = Button(self, text="Square", bg="Dark blue", fg="White", font=("Arial", 13, "bold"), command=self.draw_square).grid(row=0, column=1, sticky="ew", pady=5, padx=5)
        self.rect_btn = Button(self, text="Rectangle", bg="Dark blue", fg="White", font=("Arial", 13, "bold"), command=self.draw_rect).grid(row=0, column=2, sticky="ew", pady=5, padx=5)
        self.triangle_btn = Button(self, text="Triangle", bg="Dark blue", fg="White", font=("Arial", 13, "bold"), command=self.draw_triangle).grid(row=0, column=3, sticky="ew", pady=5, padx=5)
        self.clear_btn = Button(self, text="Clear", bg="Dark red", fg="White", font=("Arial", 13, "bold"), command=self.clear).grid(row=0, column=4, sticky="ew", pady=5, padx=5)
        
    def draw_oval(self):
        self.oval_btn.config(bg="white")
        def create_oval(event):
                x, y = event.x, event.y
                oval = self.parent.canvas.create_oval(x , y , x + random.randint(30, 100), y + random.randint(30, 100), fill='red', outline="dark red")
        self.parent.canvas.bind("<Button-1>", create_oval)

    def draw_square(self):
        def create_square(event):
              x, y = event.x, event.y
              size = random.randint(30,100)
              square = self.parent.canvas.create_rectangle(x, y, x + size, y + size, fill="blue", outline="dark blue")
        self.parent.canvas.bind("<Button-1>", create_square)
    
    def draw_rect(self):
        def create_rect(event):
              x, y = event.x, event.y
              square = self.parent.canvas.create_rectangle(x, y, x + random.randint(30, 100), y + random.randint(30, 100), fill='green1', outline="dark green")
        self.parent.canvas.bind("<Button-1>", create_rect)

    def draw_triangle(self):
        def create_triangle(event):
              x, y = event.x, event.y
              sizey = random.randint(30,100)
              sizex = random.randint(30,100)
              triangle = self.parent.canvas.create_polygon(x, y, x + sizex, y + sizey, x + (sizex-(sizex*2)), y + sizey, fill='yellow', outline="dark goldenrod")
        self.parent.canvas.bind("<Button-1>", create_triangle)

    def clear(self):
         self.parent.canvas.delete("all")

if __name__ == "__main__":
    main()
