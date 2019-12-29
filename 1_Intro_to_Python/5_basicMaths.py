#Basic Math operations in Python

x = 25
y =  7

print( x + y)

print( x- y )

print ( x * y)

print (x / y )      #returns a large decimal value, to round off do... 
print (round(x/y, 2))  # Rounds off to 2 decimal places

print( x // y )     #returns the integer value of division  


#Lets try some Modulo functions

catAgeMonths = int(input("what is your cat's age in months?: "))

years = catAgeMonths // 12    #Returns int value of years
months = catAgeMonths % 12    #Returns remainder using modulo feature

print("Your cat's age is ", years, "years and ", months, "months")
