"""
CIS129 Programming Class at Pima College
Module 5 Lab
Student: George Blake

Program Name
Grocery Store Bottle Return Calculator
"""

#Declare Variables

bottles = 0

bottlesTotal = 0

RETURNRATE = 0.10

keepGoing = "y"



#TODO in the future add error checking for instance zero breaks the program now.

while keepGoing == "y":
        for day in range(1,8):

                bottles = int(input("Enter number of bottles for day #" + str(day) + ": "))
                bottlesTotal += bottles

        print()          
        print (f"The total number of bottles collected is {bottlesTotal}")
        print (f"The total paid out is $  {(bottlesTotal*RETURNRATE):.2f} /n")
        print()
        
        keepGoing = input("Enter 'y' if you would like to enter another week's worth of data otherwise enter anything else to end")

        
