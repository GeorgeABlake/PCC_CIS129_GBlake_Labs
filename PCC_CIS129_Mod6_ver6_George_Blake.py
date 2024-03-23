"""
PCC CIS129 MOD 6 Lab

Student: George Blake

Hotdog Cookout Lab:
Students will be provided the Pseudocode, then they are to create this in Python.

Hot Dog Cookout Calculator

Assume that hot dogs come in packages of 10, and hot dog buns come in packages of 8. 
Design a modular program that calculates the number of packages of hot dogs and the number of 
packages of hot dog buns needed for a cookout, with the minimum amount of leftovers. 
The program should ask the user for the number of people attending the cookout, and the 
number of hot dogs each person will be given. The program should display the following:

1. The minimum number of packages of hot dogs required.
2. The minimum number of packages of buns required
3. The number of hot dogs that will be left over
4. The number of buns that will be left over

Programming Exercise (Hotdog Cookout Calculator)
"""
import math

# Declare Variables
people = 0
dogs = 0.0
dogsTotal = 0.0
dogsEach = 0
people = 0
dogs = 0

# Named constants for the package sizes
DOGS_PER_PACKAGE = 10
BUNS_PER_PACKAGE = 8


def showResults(dogsLeft, dogPackages, bunsLeft, bunPackages):
    # Display the minimum packages of hot dogs needed.
    print("Minimum packages of hot dogs needed:", dogPackages)
    # Display the minimum packages of buns needed.
    print("Minimum packages of hot dog buns needed:", bunPackages)
    # Display the number of hot dogs left over.
    print("Hot dogs left over:", dogsLeft)
    # Display the number of hot dog buns left over.
    print("Hot dog buns left over:", bunsLeft)

# The getTotalHotDogs module gets the number of people
# attending the cookout and the number of hot dogs each
# person will be given, and stores the product in the
# totalHotDogs reference variable.

def getTotalDogs():
    # Get the number of people attending the cookout.
    people = int(input("Enter the number of people attending the cookout: "))
    # Get the number of hot dogs each person will be given.
    dogs = int(input("Enter the number of hot dogs for each person: "))
    # Calculate the total number of hot dogs needed.
    dogsTotal = people * dogs
    return dogsTotal

# main module
def main():
    # Get the total number of hot dogs needed.
    dogsTotal = getTotalDogs()

    # Local variables
    dogsLeft = 0
    bunsLeft = 0
    dogPackages = 0 
    bunPackages = 0   
    
    # Calculate the number of left over hot dogs.
    dogsLeft = dogsTotal % DOGS_PER_PACKAGE

    # Calculate the minimum number of packages of hot dogs.
    dogPackages = math.ceil(dogsTotal / DOGS_PER_PACKAGE)

    # Calculate the number of left over hot dog buns.
    bunsLeft = dogsTotal % BUNS_PER_PACKAGE

    # Calculate the minimum number of packages of hot dogs buns.
    bunPackages = math.ceil(dogsTotal / BUNS_PER_PACKAGE)

    # Display the results.
    showResults(dogsLeft, dogPackages, bunsLeft, bunPackages)

    print(f"dogsLeft {dogsLeft} dogPackages {dogPackages} bunsLeft {bunsLeft} bunPackages {bunPackages}")

if __name__ == "__main__":
    main()
