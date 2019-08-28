####################################################################################################################################################
# This lesson is to store some information in a location on the computer called a Variable. A Variable can change over the course of the program.  #
# We will then print the variable on to the screen.                                                                                                #
# ##################################################################################################################################################

x = 5        #Let x equals 5
print (x)

y = 10       #Let y equals 10
print (y)

print(x + y) # you can do basic math as long as all the variables are the same type, for example in  this case, integers
print(x * y)
print(y / x) 


print('--------------------')

#############################################################################################
# Now lets try saving some text in a variable                                               #
# ###########################################################################################    

x = 'My First '                     # So as you can see, when I replace x this time with text, it overwrites the value of x which was 5
   
y = 'Python program'                # and same here, y was 10 but now replaced by a string value

print(x + y)


print('---------------------')

#############################################################################################
# Now lets try adding string and integers                                                   #
# ###########################################################################################  

x = 'My phone number is '
y =  ' 001-4-555-6778'          #This example is still adding string with string as the number is inside quote marks

print(x + y)

print('---------------------')

#########################################################
# Assigning multiple variables at the same time         #
#########################################################

x, y, z = 'Audi ', 'Bentley ', 'Corvette '
print('My three favorite cars are ' + x + y + z)

# Key points about Variables
# 1- must start with a letter or underscore character, and cannot start with a number or characters
# 2- names are case sensitive