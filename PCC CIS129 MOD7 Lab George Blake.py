# CIS129 Lab 7-3 The Dice Game
# George Blake

# Import necessary libraries
import random

# Function to get players' names
def get_players():
    playerOne = input("Input player 1's name: ")
    playerTwo = input("Input player 2's name: ")
    return playerOne, playerTwo

# Function to roll dice
def rollDice():
    p1number = random.randint(1, 6)
    p2number = random.randint(1, 6)
    return p1number, p2number

# Function to display winner
def displayWinner(p1number, p2number, playerOne, playerTwo):
    if p1number > p2number:
        winner = playerOne
    elif p2number > p1number:
        winner = playerTwo
    else:
        winner = "TIE"
    return winner

# Main function
def main():
    print()
    # Initialize variables
    endProgram = "no"
    playerOne = "NO NAME"
    playerTwo = "NO NAME"
    
    # Get players' names
    playerOne, playerTwo = get_players()

    # While loop to run the program again
    while endProgram.lower() == 'no':
        # Populate variables
        p1number, p2number = rollDice()

        # Display dice rolls
        print(playerOne, "rolled:", p1number)
        print(playerTwo, "rolled:", p2number)

        # Display winner
        print("The winner is:", displayWinner(p1number, p2number, playerOne, playerTwo))

        # Ask to end program
        endProgram = input('Do you want to end program? (yes/no): ')
        if endProgram.lower() == "no":
            pass
        else:
            break

# Call main function
main()
