def collatz(number=0):
    try:
        number=int(input('Enter number:'))
        while number != 1:
            if number % 2 == 0 :
                number = number//2
            else:
                number = number*3+1
            print(number)
    except ValueError :
        print('Invalid input,you must enter an integer.')
collatz()
