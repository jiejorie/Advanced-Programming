import random

# Displays the difficulty menu and accepts the player's choice of difficulty
def displayMenu():
    while True:
        menuAnswer = input("\nPlease select a Difficulty !\n • Easy \n • Moderate \n • Difficult \n\n Answer: ").lower()
        menuDifficulty = ["easy", "moderate", "difficult"]
        if menuAnswer not in menuDifficulty:
            print("\n--------------------------------\nPlease enter a valid difficulty.\n--------------------------------\n")
        else:
            print(f"\n-------------------------------------------------\nYou have chosen <<<{menuAnswer.capitalize()} Mode>>> goodluck, player!\n-------------------------------------------------\n")
            break
    return menuAnswer

# Randomly chooses integers based on the difficulty level picked by the player
def randomInt(menuAnswer):
    if menuAnswer == "easy":
        return random.randint(0,10)
    elif menuAnswer == "moderate":
        return random.randint(10,100)
    else:
        return random.randint(100,1000)

#  Randomly picks between the + and - operation symbol for each problem
def decideOperation():
    mathOperationOptions = ["+", "-"]
    mathOperation = random.choice(mathOperationOptions)
    return mathOperation

# Displays the problem the player needs to solve, accepting only integer values
def displayProblem(returned_firstInt, returned_secondInt, returned_mathOperation):
    while True:
        try:
            userAnswer = int(input(f"{returned_firstInt} {returned_mathOperation} {returned_secondInt} = "))
            break
        except ValueError:
            print("\n-------------------------------------\nPlease enter a Number as your answer.\n-------------------------------------\n")
    return userAnswer

# Checks the accuracy of the player's answers while keeping count of the amount of attempts, adding points accordingly
def isCorrect(returned_userAnswer, correctAnswer, userPoints):
    attempt = 0
    while attempt < 2:
        if returned_userAnswer != correctAnswer:
            attempt = +1
            print("\n--------------------------------------------\nYour answer is Incorrect. Try one more time!\n--------------------------------------------\n")
            returned_userAnswer = displayProblem(returned_firstInt, returned_secondInt, returned_mathOperation)
            if returned_userAnswer != correctAnswer:
                print("\n-------------------------------------------------------------\nYour answer is Incorrect once again. No points will be added.\n-------------------------------------------------------------\n")
                attempt = +71    
            else:
                print("\n-------------------------------------------------------------\nYour answer is Correct! 5 points will be added to your score.\n-------------------------------------------------------------\n")
                userPoints.append(5)
                break
        else:
            print("\n--------------------------------------------------------------\nYour answer is Correct! 10 points will be added to your score.\n--------------------------------------------------------------\n")
            userPoints.append(10)
            break
    return userPoints

# Displays the results of the overall points collected by the player and giving its equivalent grade
def displayResults(userPoints):
    userPoints = sum(userPoints)
    if userPoints <=20:
        print(f"\nOh no! You had acquired a total of {userPoints} points, equivalent to an <<< F >>> grade.\n\n")
    elif userPoints >=90:
         print(f"\nCongratulations! You had acquired a total of {userPoints} points, equivalent to an <<< A >>> grade.\n")
    elif userPoints >=70:
         print(f"\nGreat Job! You had acquired a total of {userPoints} points, equivalent to a <<< B >>> grade.\n")
    elif userPoints >=50:
        print(f"\nWow! You had acquired a total of {userPoints} points, equivalent to a <<< C >>> grade.\n")
    else:
         print(f"\nThat was close! You had acquired a total of {userPoints} points, equivalent to a <<< D >>> grade.\n")

userPoints = [] #Empty List to Add points into
# returned_firstInt = "" # Initialize empty global var
# returned_secondInt = "" # Initialize emptyglobal var
# returned_mathOperation = "" # Initialize empty global var


# Runs the game's sequence in a loop if the player chooses to keep playing
def main():
    play = "yes" #keeps the game running
    while play == "yes": #main game loop
        print("\n---------------------------------------------------------------------------------\n\n<<< Welcome to the Math Quiz Game, a test to challenge your Arithmetic skills >>>\n\n---------------------------------------------------------------------------------\n")
        returned_menuAnswer = displayMenu()
        for questionNumber in range(1,11):
            returned_firstInt, returned_secondInt = randomInt(returned_menuAnswer)
            returned_mathOperation = decideOperation()
            print(f"Question #{questionNumber}:\n ")
            returned_userAnswer = displayProblem(returned_firstInt, returned_secondInt, returned_mathOperation)
            if returned_mathOperation == "+":
                correctAnswer = returned_firstInt + returned_secondInt
            else:
                correctAnswer = returned_firstInt - returned_secondInt
            isCorrect(returned_userAnswer, correctAnswer, userPoints)
        displayResults(userPoints)
        while True: # Play again prompt
            print("\n----------------------\nPlay again? (Yes / No)\n----------------------\n ")
            play = input("Answer:  ").lower()
            if play == "yes":
                break
            elif play == "no":
                print("\n<<< Thank you so much for playing! Hope you enjoyed the game<3 >>> \n")
                break
            else:
                print("\nPlease enter 'Yes' or 'No'.")

# Determines if script is running directly or is imported, kickstarting the main function
if __name__ == "__main__":
    main()    
            


