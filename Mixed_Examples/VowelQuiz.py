<<<<<<< HEAD
'''was doing some lessons on Future learn and one of the tasks was to modify a quiz.
so this was my solution'''


from random import randint
import time
#function that has the question set and answer set
# It also prints one word and returns the answer 
def questionBank(q):
    statements=["Alfa", "Bravo", "Charlie", "Delta", "Echo",
                "Foxtrot", "Golf", "Hotel", "India", "Juliett",
                "Kilo", "Lima", "Mike","November", "Oscar",
                "Papa", "Quebec", "Romeo", "Sierra", "Tango",
                "Uniform", "Victor", "Whiskey", "X-ray", "Yankee", "Zulu"]
    answers=["2", "2", "3","2","2",
             "2","1","2","3","3",
             "2","2","2","3","2",
             "2","3","3","3","2",
             "3","2","2","1","3","2"]
 
    print()
    print(statements[q])
    answer=answers[q]
    return answer
#This function goes through 5 words in the list above
#For each correct answers it prints out the time
#Otherwise it prints incorrect
def game():
 
    for i in range(5):
   
        q = randint(0, 25)
        answer = questionBank(q)
        startTime = time.time()
        guess = input("Guess how many vowels? : ")
        
 
 
 
        if guess == answer:
            endTime = time.time()
            timeTaken = round(endTime - startTime, 2)
            print("Correct")
            print("You took ", str(timeTaken), "seconds")
        else:
            print("Incorrect")

    
 
=======
'''was doing some lessons on Future learn and one of the tasks was to modify a quiz.
so this was my solution'''


from random import randint
import time
#function that has the question set and answer set
# It also prints one word and returns the answer 
def questionBank(q):
    statements=["Alfa", "Bravo", "Charlie", "Delta", "Echo",
                "Foxtrot", "Golf", "Hotel", "India", "Juliett",
                "Kilo", "Lima", "Mike","November", "Oscar",
                "Papa", "Quebec", "Romeo", "Sierra", "Tango",
                "Uniform", "Victor", "Whiskey", "X-ray", "Yankee", "Zulu"]
    answers=["2", "2", "3","2","2",
             "2","1","2","3","3",
             "2","2","2","3","2",
             "2","3","3","3","2",
             "3","2","2","1","3","2"]
 
    print()
    print(statements[q])
    answer=answers[q]
    return answer
#This function goes through 5 words in the list above
#For each correct answers it prints out the time
#Otherwise it prints incorrect
def game():
 
    for i in range(5):
   
        q = randint(0, 25)
        answer = questionBank(q)
        startTime = time.time()
        guess = input("Guess how many vowels? : ")
        
 
 
 
        if guess == answer:
            endTime = time.time()
            timeTaken = round(endTime - startTime, 2)
            print("Correct")
            print("You took ", str(timeTaken), "seconds")
        else:
            print("Incorrect")

    
 
>>>>>>> 130b6e5de879110218c2f46be1146b9946722d81
game()