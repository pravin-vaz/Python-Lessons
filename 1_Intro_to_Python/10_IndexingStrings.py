#This page has some examples on how to index and slice strings

x = "Hairy McLairy from Donaldson's Dairy"   #Some text in variable x

print(x[0])                         #H
print(x[1])                         #a
print(x[5:10])                      # McLa -- Note that position 5 is a space

y = x.split()                       #creates a string array of words

print(y[0] + " " + y[3])            #picks up the words at zero position and position 3

print("ThiS Is WeIrD To rEaD". lower()) #makes everything lowercase

print("ThiS Is WeIrD To rEaD". upper()) #Capitalises everything

print("HandsUp".startswith("Hands"))    #Returns True if answer is correct
print("HandsUp".endswith("Hands"))      #returns false because its incorrect

print("Hairy".replace("H", "F"))        #Replaces the letter with a new one

print(",".join(['h','e','r','c','u','l','e','s']))  #Add certain letters to a string

print(len("Constantinople"))            #returns number of items in the string

