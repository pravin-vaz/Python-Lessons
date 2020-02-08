import random  # Random module

while True:
        
    number = int(input('Press a number from 0 to 9 to randomize it: '))
    if number >= 10:
        print('Should have followed my instructions. GoodBye')
        break   
    
    #CHALLENGE - TRY AND MAKE THE PROGRAM NOT BREAK IF THE PERSON ENTERS A NUMBER OVER 10
    
    randomAnswer = random.randrange(0, 8)  # pick a random number
    
    if randomAnswer == 0:
        print('0 ')
    
    elif randomAnswer == 1:
        print('1 ')
    
    elif randomAnswer == 2:
        print('2 ')
    
    elif randomAnswer == 3:
        print('3 ')
    
    elif randomAnswer == 4:
        print('4 ')
    
    elif randomAnswer == 5:
        print(' 5 ')
    
    elif randomAnswer == 6:
        print('6')
    
    elif randomAnswer == 7:
        print('7 ')

    elif randomAnswer == 8:
        print('8')
    
    elif randomAnswer == 9:
        print('9')
