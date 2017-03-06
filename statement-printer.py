myit = 'y'
mystring = ''
myIT ='y'
myInt=0

while myit == 'y':
    mystring = input('Please enter a statement to print.')
    print(mystring)
    myit = input('Would you like to do it again? y or n: \n')
    if myit == 'y':
        mystring
    else:
        print('you have chosen not to do it again\n')
        print('thank you for printing your statement(s).')
        break
while myIT == 'y':
    myInt = input('Please enter a number to print.')
    print(myInt)
    myIT = input('Would you like to do it again? y or n: \n')
    if myIT == 'y':
        myInt
    else:
        print('you have chosen not to do it again')
        print('thank you for printing your number(s).')
        break
