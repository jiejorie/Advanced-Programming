import random # Imports random library

# Randomly picks a joke from the list of jokes
def choose_joke(jokes):
    joke = random.choice(jokes)
    return joke

decoLine1 = "----------------------------------------------------"
decoLine2 = "------------------------------------------------------------"

# Displays the joke by waiting to receive an input from the user
def display_joke(chosenJoke):
    setup, punchline = chosenJoke.split("?")
    print(f"\n{decoLine2}\n\n(Press 'Enter' or any key to see the joke's punchline.)\n")
    print(f"{decoLine2}\n\n{setup}...?", end=" ")
    seePunchline = input()
    if seePunchline == "":
     print(f"\n<<< {punchline.strip()} >>> HAHAHA! \n\n{decoLine2}")
    else: 
        seePunchline = ""
        print(f"\n<<< {punchline.strip()} >>> HAHAHA! \n\n{decoLine2}")
    return setup, punchline

# Plays the joke generator's main sequence of prompts and functions
def main():
    file = open("randomJokes.txt", encoding="utf-8") #opens randomJokes.txt file
    read = file.readlines() #reads each line in randomJokes.txt 
    jokes = [line.strip() for line in read] #each line is inserted to the list of jokes

    seeJoke = "joke"
    while "joke" in seeJoke:
        print(f"\n{decoLine1}\nAlexa: Welcome, user! Would you like to hear a joke?\n{decoLine1}")
        print(f"\n\n(To hear a joke from Alexa, please type 'Alexa, tell me a joke'. If you'd rather not, type 'No Thanks')")
        seeJoke = input("Answer: ").lower()
        if "joke" in seeJoke:
            chosenJoke = choose_joke(jokes)
            returnedSetup, returnedPunchline = display_joke(chosenJoke)
            anotherJoke = "yes"
            while anotherJoke != "no":
                anotherJoke = input("\nAlexa: Would you like to see another joke? \n(Type 'Yes' or 'No'): ").lower()
                if anotherJoke == "no":
                    print("\nAlexa: Come by and visit for another cackle, user!\n")
                    seeJoke = "no"
                elif anotherJoke == "yes":
                    removeChosenJoke = chosenJoke
                    jokes.remove(removeChosenJoke)
                    try:
                        chosenJoke = choose_joke(jokes)
                        display_joke(chosenJoke)
                    except IndexError:
                        print("\nAlexa: You must've enjoyed all my jokes! Unfortunately, I'm all out... Thanks for stopping by! :)")
                        seeJoke = "no"
                        anotherJoke = "no"
                else:
                    print("\nAlexa: Please type only 'Yes' or 'No'.")
        elif "no" in seeJoke:
            print("\nAlexa: Too bad! Come by to visit if you feel like having a laugh.")
            break
        else: 
            seeJoke = "joke"
            print(f"\n{decoLine2}\n\nAlexa: Please re-check for any spelling errors and read the prompt carefully!\n\n{decoLine2}")

# Determines if script is running directly or is imported, kickstarting the main function
if __name__ == "__main__":
    main()      

