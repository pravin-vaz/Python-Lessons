from time import sleep                                                  #Just to add a small sleep between the chat

name = str(input("Howdy, stranger. What's your name? "))                #storing the user input in name variable

print("Welcome", name, "I am Nick Pope" )                               #Print some text with variable name

sleep(2)                                                                #sleep for 2 secs

age = int(input("What's your age " + name + "?" ))                      #This time receive a number input    

print("Crap", age, "! That's a ripe old age")                           

sleep(2)

print("Allright I'll go get you some tea. ")