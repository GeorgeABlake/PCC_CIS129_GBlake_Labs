"""
George Blake
CIS129
Mon Mar 11, 2024 and March 13
loop practice
"""
userNumber = 0

def main():
    while True:
        userNumber = get_integer('Enter a num: ')
        #1.b. tell the user if the numbner is odd or even
        if (userNumber % 2 == 0):
            print ('The number is even!')
        else:
            print('The number is odd!')
        #1.c. ask the user if they wan to do it again
        #using a decision structure and a loop
        print('Do you want to do it agian?')
        again = input ('enter \'y\' to loop again ')
        if again != 'y':
            break

#input function
def get_integer(message):
    while True:
        try:
            user_input = int(input(message))
            return user_input
        except ValueError: 
            print('Incorrect data entered, please re-attemt')
   
main ()


