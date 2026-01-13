from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from io import BytesIO
import requests
import random
import pygame

# runs mainloop() if called
def main():
    gui = PokedexApp()
    gui.mainloop()

# holds the primary GUI
class PokedexApp(Tk):
    def __init__(self):
        super().__init__()
        # Main Setup
        self.title("Pokedex API")
        self.geometry("1000x700")
        self.minsize(1000,700)
        self.maxsize(1000,700)
        self.config(bg="#e11930")

        # Window Icon
        self.icon = PhotoImage(file="Assessment 2\Assets\Poké_Ball_icon.png")
        self.iconphoto(False, self.icon)

        # Starts and Initializes BG music & SFX
        pygame.mixer.init()
        pygame.mixer.music.load("Assessment 2\Assets\Pokemon RedBlue Opening.mp3")
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(0.2)
        self.click_sound = pygame.mixer.Sound("Assessment 2\Assets\click_sfx.wav")
        self.click_sound_2 = pygame.mixer.Sound("Assessment 2\Assets\click2_sfx.wav")
     

        # Instructions popup
        messagebox.showinfo("Welcome!","Welcome to learning Pokemon with Professor Oak. Type a Pokemon's name or Id to view it!")

        # Creates Widgets
        self.title_lbl = Label(self, text="LEARN POKEMON WITH PROFESSOR OAK!", font=("Speedy", 20, "bold"), fg="#0a4740", bg="#bdf3d1", relief="sunken", bd=5)
        self.main_frame = MainFrame(self)
        self.search_frame = SearchFrame(self)
        
        # Places Widgets
        self.title_lbl.pack(anchor=N, fill="x", expand=True, ipady=10, padx=50, pady=10)
        self.main_frame.pack(anchor=CENTER, fill="x", expand=True, ipadx=10, padx=50, pady=10)
        self.search_frame.pack(anchor=S,fill="x", expand=True, ipadx=10, padx=50, pady=20)

        # Closing popup
        self.protocol("WM_DELETE_WINDOW", self.before_close)
    
    # Searches for data in PokeAPI
    def getData(self):
        self.pokemon_name = self.search_frame.entry.get().lower()
        self.url = f"https://pokeapi.co/api/v2/pokemon/{self.pokemon_name}"
        self.response = requests.get(self.url)

        if self.response.status_code == 200:
            self.data = self.response.json()
            return self.data
        else:
            messagebox.showerror("Error!", "Pokemon not found in database. Check for any spelling errors!")

    # Displays All Results After Search
    def onSearch(self):
            self.click_sound.play()
            self.data = self.getData()
            self.getSprite()
            self.getDetails()
            self.click_sound_2.play()

    # Displays Pokemon Sprites
    def getSprite(self):
        self.sprite_url = self.data["sprites"]["front_default"]
        if self.sprite_url:
            self.img_data = requests.get(self.sprite_url).content
            self.img = Image.open(BytesIO(self.img_data)).resize((250,250))
            self.photo = ImageTk.PhotoImage(self.img)

            self.main_frame.pokemon_frame.canvas.delete("all")
            self.image = self.photo
            self.main_frame.pokemon_frame.canvas.create_image(150, 100, image=self.photo)
        else:
            print("No sprite available.")

    # Displays Pokemon Information Details
    def getDetails(self):
        if self.data:
            self.main_frame.pokemon_frame.pokemon_info_frame.name_lbl.config(text=f"NAME: ")
            self.main_frame.pokemon_frame.pokemon_info_frame.name_lbl.config(text=f"NAME: {self.data["name"].upper()}")

            self.main_frame.pokemon_frame.pokemon_info_frame.id_lbl.config(text=f"ID: ")
            self.main_frame.pokemon_frame.pokemon_info_frame.id_lbl.config(text=f"ID: #{self.data["id"]}")

            self.main_frame.pokemon_frame.pokemon_info_frame.type_lbl.config(text=f"TYPE: ")
            self.main_frame.pokemon_frame.pokemon_info_frame.type_lbl.config(text=f"TYPE: {self.data["types"][0]["type"]["name"].upper()}")

            self.main_frame.pokemon_frame.pokemon_info_frame.height_lbl.config(text=f"HEIGHT: ")
            self.main_frame.pokemon_frame.pokemon_info_frame.height_lbl.config(text=f"HEIGHT: {self.data["height"]/10} M")

            self.main_frame.pokemon_frame.pokemon_info_frame.weight_lbl.config(text=f"WEIGHT: ")
            self.main_frame.pokemon_frame.pokemon_info_frame.weight_lbl.config(text=f"WEIGHT: {self.data["weight"]/10} KG")

    # Picks Random Pokemon based on ID
    def onRandom(self):
        self.click_sound.play()
        self.random_id = random.randint(1,1025)
        self.search_frame.entry.delete(0, END)
        self.search_frame.entry.insert(0,str(self.random_id))
        self.onSearch()

    # popup before exiting
    def before_close(self):
        if messagebox.askyesno("Exit?","Do you really want to exit?"):
            self.destroy()
        else:
            pass

# Center Frame
class MainFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Styles Frame
        self.config(bg="#96f1b7", relief="groove", bd=5)
        
        # Arranges column widths
        self.columnconfigure(0, weight=7)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        # Creates Widgets
        self.pokemon_frame = PokemonFrame(self)
        self.pokeball_img = ImageTk.PhotoImage(Image.open("Assessment 2\Assets\Poké_Ball_icon.png").resize((50, 50)))
        self.prof_oak_img = ImageTk.PhotoImage(Image.open("Assessment 2\Assets\professor_oak.png").resize((250, 378)))
        
        # Places Widgets
        self.pokemon_frame.grid(column=0, row=0, rowspan=2, sticky=NSEW, pady=15, padx=30, ipady=15)
        self.pokeball = Label(self, image=self.pokeball_img, bg="#96f1b7").grid(column=2, row=0, sticky=N, pady=15, padx=10)
        self.prof_oak = Label(self, image=self.prof_oak_img, bg="#96f1b7").grid(column=1, row=1, sticky=S)

# Frames All Pokemon Results
class PokemonFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # Styles Frame
        self.config(bg="#3b4cca", relief="groove", bd=5)

        # Creates Widgets
        self.canvas = Canvas(self, width=300, height=200, relief="groove", bd=3)
        self.pokemon_info_frame = PokemonInfo(self)

        # Places Widgets
        self.canvas.pack(pady=25)
        self.pokemon_info_frame.pack(fill="both", expand=True, padx=60)

        
# Frames Pokemon Text Information
class PokemonInfo(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # Styles Frame
        self.config(bg="#3b4cca")

        #  Creates Widgets
        self.name_lbl = Label(self, text="NAME: ", font=("Speedy", 11, "bold"), bg="#3b4cca", fg="#ffde00")
        self.id_lbl = Label(self, text="ID: ", font=("Speedy", 11, "bold"), bg="#3b4cca", fg="#ffde00")
        self.type_lbl = Label(self, text="TYPE: ", font=("Speedy", 11, "bold"), bg="#3b4cca", fg="#ffde00")
        self.height_lbl = Label(self, text="HEIGHT: ", font=("Speedy", 11, "bold"), bg="#3b4cca", fg="#ffde00")
        self.weight_lbl = Label(self, text="WEIGHT: ", font=("Speedy", 11, "bold"), bg="#3b4cca", fg="#ffde00")
        
        # Places Widgets
        self.name_lbl.pack(pady=2, anchor=W)
        self.id_lbl.pack(pady=2, anchor=W)
        self.type_lbl.pack(pady=2, anchor=W)
        self.height_lbl.pack(pady=2, anchor=W)
        self.weight_lbl.pack(pady=2, anchor=W)


# Frames Interactable Widgets
class SearchFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # Styles Frame
        self.config(bg="#e11930")
        # Initialize parent for inheritance
        self.parent = parent

        # Set up column thickness
        self.columnconfigure((0), weight=2)
        self.columnconfigure((1,2), weight=1)
        
        # Creates Widgets
        self.entry = Entry(self,font=("Speedy", 15), fg="#0a4740", bg="#bdf3d1", relief="sunken", bd=5)
        self.search_btn = Button(self, text="SEARCH", font=("Speedy", 10, "bold"), fg="#bdf3d1", bg="#0a4740", height=3, bd=5, command=self.parent.onSearch)
        self.random_btn = Button(self, text="RANDOM", font=("Speedy", 10, "bold"), fg="#96f1b7", bg="#0a4740", height=3, bd=5, command=self.parent.onRandom)
        
        # Places Widgets
        self.entry.grid(column=0, row=0, sticky=NSEW)
        self.search_btn.grid(column=1, row=0, sticky=NSEW, padx=10)
        self.random_btn.grid(column=2, row=0, sticky=NSEW)


# runs main() if script is directly running
if __name__ == "__main__":
    main()