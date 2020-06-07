#Original code below from 101computing.net which I have modified with scores, for loop, etc.

import time

print("Welcome to the Reaction Time Game")

#Pause of 1 second
time.sleep(1)

start=time.time()

text = input("Press the return key?")
end = time.time()

duration = round(end - start,2)
print("Reaction Time: " + str(duration) + " seconds.")


#Adapt the challenge to suit
# 1) Keep the game inside a loop so it doesn't end after one go
# 2) Have 5 rounds and score them. For example: 5 points for inside 0.25 seconds,
#    4 points for 0.25 to 0.5 seconds and 3 points for 0.5 to 1 second. No points for over 1 second
# 3) Print those scores out to the screen. 

'''
Solution 1

import time

print("Welcome to the Reaction Time Game")
time.sleep(1)
print("High score is 25, Can you beat it?")
time.sleep(1)
print("Press the return key when you see the message")
time.sleep(1)
print("Good luck")

score = 0

for i in range(5):
    #Pause of 1 second
    time.sleep(1)
    
    
    start=time.time()
    text = input("Press the return key")
    end = time.time()

    duration = round(end - start,2)
    print("Reaction Time: " + str(duration) + " seconds.")
    
    if duration >= 0.5 and duration < 1:
        score += 3
        print("You got 3 points this round, you need to be faster")
    elif duration < 0.5 and duration >= 0.25:
        score += 4
        print("You got 4 points this round, not bad")
    elif duration < 0.25 and duration >= 0.01:
        score += 5
        print("Top job, 5 points")
    else:
        print("sorry you didn't score any points this round")
    time.sleep(1)
              
    
   
    
print("Your total score is: ", score)
print("Thanks for playing the Reaction Time Game")




'''