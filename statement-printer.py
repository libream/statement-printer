myit = 'y'
mystring = ''

while myit == 'y':
    mystring = input('Please enter a statement to print.\n')
    print(mystring)
    myit = input('Would you like to do it again? y or n: ')
    if myit == 'y':
        mystring
    else:
        print('you have chosen not to do it again')
        break

