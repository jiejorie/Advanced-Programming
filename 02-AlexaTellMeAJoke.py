import random # Imports random library

# List of jokes to be used
jokes = ["Why did the zombies get divorced? Their marriage was dead!", 
         "Why did the lion go to therapy? He found out his wife was a cheetah!", 
         "Did you hear about the couple of bed bugs? They got married in the spring!", 
         "Which one of your kids will never grow up and move out? Your husband!", 
         "Why is being married worse than going to work? At least at work, you might get a new boss!", 
         "How are boys similar to wine? They take years and years and years to mature!",
         "Why is a good doctor able to stay calm? He has a lot of patients!", 
         "What the best way to criticize your boss? Very quietly, so she can’t hear you!", 
         "Why did the marketer dump her boyfriend? Lack of engagement!", 
         "What’s a pirate’s favorite meeting style? A webinarrrrr!", 
         "What does Nemo have in common with my dad? Neither can be found!", 
         "What did the cow say to the leather chair? “Hi Mom!”", 
         "When does a joke become a dad joke? When it leaves and never comes back!",
         "Why don’t cannibals eat clowns? Because they taste funny!", 
         "Why don’t graveyards ever get overcrowded? Because people are dying to get in!", 
         "Why don’t orphans get their driver’s license? Because they don’t know where home is!", 
         "What’s the best part about dead batteries? Free of charge!", 
         "Why did the old man fall into the well? Because he couldn’t see that well!", 
         "Why don’t we play hide and seek in cemeteries? Because good luck finding someone who hasn’t already won!",
         "Why do blind people hate skydiving? It scares the heck out of their dog!", 
         "What’s red and bad for your teeth? A brick!"]

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






