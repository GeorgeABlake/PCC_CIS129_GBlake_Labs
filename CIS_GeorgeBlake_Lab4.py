"""
Module 4 LB-4
George Blake
2/27/2024
Store Bonus and Employee Bonus Calculator
"""

# delcare local variables
monthlySales = 0  # monthly sales amount
storeAmount = 0 # store bonus
salesIncrease = 0.00 # percent of sales increase
empAmount = 0 # employee 
prompt = "Please enter the montly sales "

# This code gets the monthly sales

monthlySales = float(input(prompt))

# This code determines the store bonus

if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000 
else:
    storeAmount = 0


# This code gets the percent of increase in sales

salesIncrease = float(input('Enter the percent of increase in sales as a whole number '))
print (salesIncrease)
salesIncrease = salesIncrease / 100
print (salesIncrease)

# This code determins the employee bonus

if salesIncrease >= .05:
    empAmount = 75
elif salesIncrease >= .04:
    empAmount = 50
elif salesIncrease >= .03:
    empAmount = 40
else:
    empAmount = 0

# This code prints the bonus information
print ("The store bonus amount is $ ", storeAmount)
print ("The employee bonus amount is $ ", empAmount)
if (storeAmount == 6000) and (empAmount == 75):
    print ('Congrats! You have reached the highest bonus amounts possible! ')
  


  

  

