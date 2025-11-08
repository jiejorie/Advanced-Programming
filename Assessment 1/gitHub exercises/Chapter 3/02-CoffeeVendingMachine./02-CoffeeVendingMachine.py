from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

def main():
    gui = MyGUI()
    gui.mainloop()

class MyGUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("Coffee Vending Machine")
        self.geometry("700x630")
        self.minsize(700, 630)
        self.maxsize(700, 630)
        self.config(bg="#edd8c5")

        self.balance = 10

        self.img = ImageTk.PhotoImage(Image.open("C:/Users\Marcelo/Documents/Margie CC L5/Advanced Programming/Assessment 1/gitHub exercises/Chapter 3/02-CoffeeVendingMachine/banner.png").resize((700, 150)))
        self.bg = Label(self, image=self.img).pack(anchor="n", side="top")

        self.title_text = Label(self, text="What would you like today?", font=("Georgia", 15, "bold"), fg="saddle brown", bg="#fdefe7").pack(side="top", anchor="n", ipady=10, fill="x", expand=1)

        self.MenuFrame = MenuFrame(self)
        self.MenuFrame.pack(anchor="center")

        self.current_blnc = Label(self, text=f"Your current balance is: {self.balance} AED", font=("Georgia", 10, "bold"), fg="#fdefe7", bg="saddle brown")
        self.current_blnc.pack(side="bottom", anchor="s", fill="x", expand=1, ipady=10)

        self.protocol("WM_DELETE_WINDOW", self.before_close)

    def before_close(self):
        if messagebox.askyesno("Exit Student Manager","Do you really want to exit?"):
            self.destroy()
        else:
            pass



class MenuFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.config(bg="#edd8c5")

        self.drink_price = 0

        self.CoffeeFrame = CoffeeFrame(self)
        self.CoffeeFrame.grid(row=0, rowspan=2, column=0, padx=15, sticky="nws")

        self.CustomizeFrame = CustomizeFrame(self)
        self.CustomizeFrame.grid(row=0, column=1, padx=15, sticky="ne")

        self.OrderFrame = OrderFrame(self)
        self.OrderFrame.grid(row=1, column=1, sticky="ews", padx=15)
    
    def order_espresso(self):
        self.OrderFrame.order.config(text="Espresso : 2 AED")
        self.drink_price = 2
        return self.drink_price
    
    def order_americano(self):
        self.OrderFrame.order.config(text="Americano : 2.50 AED")
        self.drink_price = 2.50
        return self.drink_price
    
    def order_latte(self):
        self.OrderFrame.order.config(text="Latte : 2 AED")
        self.drink_price = 2
        return self.drink_price
    
    def order_mocha(self):
        self.OrderFrame.order.config(text="Mocha : 3 AED")
        self.drink_price = 3
        return self.drink_price
    
    def order_macchiato(self):
        self.OrderFrame.order.config(text="Macchiato : 3 AED")
        self.drink_price = 3
        return self.drink_price
    
    def order_capuccino(self):
        self.OrderFrame.order.config(text="Capuccino : 2.50 AED")
        self.drink_price = 2.50
        return self.drink_price
    
    def checkout(self):
        if self.drink_price <= 0:
            messagebox.showerror("Transaction Order", message="Please place an order before checking out.")
        elif self.parent.balance >= self.drink_price:
            messagebox.showinfo("Successful Transaction", message="Transaction was successful, buy again soon!")
            self.parent.balance -= self.drink_price
            messagebox.showinfo("Drink Completed!", message="Your drink is complete, please collect it below!")
            self.OrderFrame.order.config(text="...")
            self.CustomizeFrame.milk_type.set("Cow's Milk")
            self.CustomizeFrame.sugar_scale.set(0)
            return self.parent.current_blnc.config(text=f"Your current balance is: {self.parent.balance} AED")
        else:
            messagebox.showwarning("Failed Transaction", message="Transaction was unsuccessful, balance insufficient.")
    
    def clear(self):
        self.OrderFrame.order.config(text="...")
        self.drink_price = 0
        self.CustomizeFrame.milk_type.set("Cow's Milk")
        self.CustomizeFrame.sugar_scale.set(0)



class CoffeeFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.config(bg="#edd8c5")

        self.rowconfigure((0,1,2,3), weight=1)
        self.rowconfigure(4, weight=10)
        self.rowconfigure((5,6,7), weight=1)

        self.coffee_options_txt = Label(self, text="Coffee Options:", font=("Georgia", 12, "bold"), fg="black", bg="#fdefe7").grid(row=0, column=0, columnspan=3, pady=15, ipady=3, sticky="ew")

        self.espresso = ImageTk.PhotoImage(Image.open("C:/Users\Marcelo/Documents/Margie CC L5/Advanced Programming/Assessment 1/gitHub exercises/Chapter 3/02-CoffeeVendingMachine/espresso.png").resize((70, 70)))
        self.espresso_btn = Button(self, image=self.espresso, bd=0, bg="#edd8c5", activebackground="#edd8c5", command=self.parent.order_espresso).grid(row=1, column=0, padx=10, pady=5)
        self.espresso_txt = Label(self, text="Espresso", font=("Georgia", 9), fg="black", bg="#edd8c5").grid(row=2, column=0)
        self.espresso_price = Label(self, text="2 AED", font=("Georgia", 8), fg="saddle brown", bg="#edd8c5").grid(row=3, column=0)
        
        self.americano = ImageTk.PhotoImage(Image.open("C:/Users\Marcelo/Documents/Margie CC L5/Advanced Programming/Assessment 1/gitHub exercises/Chapter 3/02-CoffeeVendingMachine/americano.png").resize((70, 70)))
        self.americano_btn = Button(self, image=self.americano, bd=0, bg="#edd8c5", activebackground="#edd8c5", command=self.parent.order_americano).grid(row=1, column=1, padx=10, pady=5) 
        self.americano_txt = Label(self, text="Americano", font=("Georgia", 9), fg="black", bg="#edd8c5").grid(row=2, column=1)
        self.americano_price = Label(self, text="2.50 AED", font=("Georgia", 8), fg="saddle brown", bg="#edd8c5").grid(row=3, column=1)

        self.latte = ImageTk.PhotoImage(Image.open("C:/Users\Marcelo/Documents/Margie CC L5/Advanced Programming/Assessment 1/gitHub exercises/Chapter 3/02-CoffeeVendingMachine/latte.png").resize((70, 70)))
        self.latte_btn = Button(self, image=self.latte, bd=0, bg="#edd8c5", activebackground="#edd8c5", command=self.parent.order_latte).grid(row=1, column=2, padx=10, pady=5) 
        self.latte_txt = Label(self, text="Latte", font=("Georgia", 9), fg="black", bg="#edd8c5").grid(row=2, column=2)
        self.latte_price = Label(self, text="2 AED", font=("Georgia", 8), fg="saddle brown", bg="#edd8c5").grid(row=3, column=2)

        self.spacing = Label(self, text="", font=50, bg="#edd8c5").grid(row=4, column=0, columnspan=3)

        self.mocha = ImageTk.PhotoImage(Image.open("C:/Users\Marcelo/Documents/Margie CC L5/Advanced Programming/Assessment 1/gitHub exercises/Chapter 3/02-CoffeeVendingMachine/mocha.png").resize((70, 70)))
        self.mocha_btn = Button(self, image=self.mocha, bd=0, bg="#edd8c5", activebackground="#edd8c5", command=self.parent.order_mocha).grid(row=5, column=0, padx=10, pady=5) 
        self.mocha_txt = Label(self, text="Mocha", font=("Georgia", 9), fg="black", bg="#edd8c5").grid(row=6, column=0)
        self.mocha_price = Label(self, text="3 AED", font=("Georgia", 8), fg="saddle brown", bg="#edd8c5").grid(row=7, column=0)

        self.macchiato = ImageTk.PhotoImage(Image.open("C:/Users\Marcelo/Documents/Margie CC L5/Advanced Programming/Assessment 1/gitHub exercises/Chapter 3/02-CoffeeVendingMachine/macchiato.png").resize((70, 70)))
        self.macchiato_btn = Button(self, image=self.macchiato, bd=0, bg="#edd8c5", activebackground="#edd8c5", command=self.parent.order_macchiato).grid(row=5, column=1, padx=10, pady=5) 
        self.macchiato_txt = Label(self, text="Macchiato", font=("Georgia", 9), fg="black", bg="#edd8c5").grid(row=6, column=1)
        self.macchiato_price = Label(self, text="3 AED", font=("Georgia", 8), fg="saddle brown", bg="#edd8c5").grid(row=7, column=1)

        self.capuccino = ImageTk.PhotoImage(Image.open("C:/Users\Marcelo/Documents/Margie CC L5/Advanced Programming/Assessment 1/gitHub exercises/Chapter 3/02-CoffeeVendingMachine/capuccino.png").resize((70, 70)))
        self.capuccino_btn = Button(self, image=self.capuccino, bd=0, bg="#edd8c5", activebackground="#edd8c5", command=self.parent.order_capuccino).grid(row=5, column=2, padx=10, pady=5) 
        self.capuccino_txt = Label(self, text="Capuccino", font=("Georgia", 9), fg="black", bg="#edd8c5").grid(row=6, column=2)
        self.capuccino_price = Label(self, text="2.50 AED", font=("Georgia", 8), fg="saddle brown", bg="#edd8c5").grid(row=7, column=2)

class CustomizeFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.config(bg="#edd8c5")

        self.custom_txt = Label(self, text="Customize your drink:", font=("Georgia", 12, "bold"), fg="black", bg="#fdefe7").grid(row=0, column=0, columnspan=3, pady=15, ipady=3, sticky="ew")

        self.milk_type = StringVar(value="")
        self.milk_type.set("Cow's Milk")

        self.add_milk_txt = Label(self, text="What type of Milk?", font=("Georgia", 10, "bold"), fg="saddle brown", bg="#edd8c5").grid(row=1,column=0, columnspan=3)
        self.milk_check = Radiobutton(self, text="Cow's Milk", font=("Georgia", 9), fg="black", bg="#edd8c5", variable=self.milk_type, value="Cow's Milk").grid(row=2, column=0, pady=10, sticky="w")
        self.milk_check = Radiobutton(self, text="Soy Milk", font=("Georgia", 9), fg="black", bg="#edd8c5", variable=self.milk_type, value="Soy Milk").grid(row=2, column=1, pady=10, padx=15, sticky="we")
        self.milk_check = Radiobutton(self, text="Almond Milk", font=("Georgia", 9), fg="black", bg="#edd8c5", variable=self.milk_type, value="Almond Milk").grid(row=2, column=2, pady=10, sticky="e")

        self.sugar_amnt_txt = Label(self, text="What sugar %?", font=("Georgia", 10, "bold"), fg="saddle brown", bg="#edd8c5").grid(row=3,column=0, columnspan=3, pady=5)
        self.sugar_scale =  Scale(self, from_=0, to=100, orient=HORIZONTAL, troughcolor="#edd8c5", bg="#fdefe7", bd=0, relief="flat", highlightthickness=0)
        self.sugar_scale.grid(row=4, column=0, columnspan=3, padx=5, pady=5, sticky="ew")

class OrderFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.config(bg="#edd8c5")

        self.columnconfigure((0,1), weight=1)

        self.order_txt = Label(self, text="Your total is: ", font=("Georgia", 15, "bold"), fg="black", bg="#edd8c5").grid(row=0, column=0, columnspan=2, pady=10)
        self.order = Label(self, text="...", font=("Georgia", 9, "bold"), fg="black", bg="#fdefe7")
        self.order.grid(row=1, column=0, columnspan=2, padx=5, pady=5, ipady=5, sticky="ew")

        self.clear = Button(self, text="Clear", font=("Georgia", 9), fg="#fdefe7", bg="saddle brown", bd=0, command=self.parent.clear).grid(row=3, column=0, pady=5, padx=5, ipadx=5, ipady=5, sticky="we")
        self.checkout = Button(self, text="Checkout", font=("Georgia", 9), fg="#fdefe7", bg="saddle brown", bd=0, command=self.parent.checkout).grid(row=3, column=1, pady=5, padx=5, ipadx=5, ipady=5, sticky="we")
if __name__ == "__main__":
    main()
