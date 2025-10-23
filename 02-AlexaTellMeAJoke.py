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

# Displays the joke by waiting to receive an input from the user
def display_joke(chosen_joke):
    setup, punchline = chosen_joke.split("?")
    print("\n------------------------------------------------------------\n\n(Press 'Enter' or any key to see the joke's punchline.)\n")
    print(f"------------------------------------------------------------\n\n{setup}...?", end=" ")
    see_punchline = input()
    if see_punchline == "":
     print(f"\n<<< {punchline.strip()} >>> HAHAHA! \n\n------------------------------------------------------------")
    else: 
        see_punchline = ""
        print(f"\n<<< {punchline.strip()} >>> HAHAHA! \n\n------------------------------------------------------------")
    return setup, punchline

# Plays the joke generator's main sequence of prompts and functions
def main():
    see_joke = "joke"
    while "joke" in see_joke:
        print("\n----------------------------------------------------\nAlexa: Welcome, user! Would you like to hear a joke?\n----------------------------------------------------\n\n(To hear a joke from Alexa, please type 'Alexa, tell me a joke'. If you'd rather not, type 'No Thanks')")
        see_joke = input("Answer: ").lower()
        if "joke" in see_joke:
            chosen_joke = choose_joke(jokes)
            returned_setup, returned_punchline = display_joke(chosen_joke)
            another_joke = "yes"
            while another_joke != "no":
                another_joke = input("\nAlexa: Would you like to see another joke? (Type 'Yes' or 'No'): ").lower()
                if another_joke == "no":
                    print("\nAlexa: Come by and visit for another cackle, user!\n")
                    see_joke = "no"
                elif another_joke == "yes":
                    remove_chosen_joke = chosen_joke
                    jokes.remove(remove_chosen_joke)
                    try:
                        chosen_joke = choose_joke(jokes)
                        display_joke(chosen_joke)
                    except IndexError:
                        print("\nAlexa: You must've enjoyed all my jokes! Unfortunately, I'm all out... Thanks for stopping by! :)")
                        see_joke = "no"
                        another_joke = "no"
                else:
                    print("\nAlexa: Please type only 'Yes' or 'No'.")
        elif "no" in see_joke:
            print("\nAlexa: Too bad! Come by to visit if you feel like having a laugh.")
            break
        else: 
            see_joke = "joke"
            print("\n<<<<Alexa: Please recheck for any spelling mistakes and read the prompt carefully!>>>>\n\n")

# Determines if script is running directly or is imported, kickstarting the main function
if __name__ == "__main__":
    main()      


