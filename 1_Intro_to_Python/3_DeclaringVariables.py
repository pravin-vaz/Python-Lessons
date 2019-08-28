#############################################################################################
# This lesson is on declaring variables according to their type                             #
# ###########################################################################################  

a = int(5)    #Declare variable a as an integer
print(a)

b = float(25.5) #Declare variable b as a floating point number
print(b)

c = float(a * b)    #multiplying an integer and float will give you a float
print(c)

d = int(a * b)      #but if you declared it as an integer , it will spit out an integer value
print(d)

e = str('ssup')     # str is short for string
f = str("kia ora")  # text can have single or double quotes
print(a,e,f)        # you can print multiple items inside the print command

### Multiline text is done by using 3 single or double quotes like below

g = str('''This is going to be multi line text                         
since it has lots of text I will split it over
multiple lines like this
''')
print(g)

# You CANNOT ADD STRINGS and INTEGERS 
# You use  the format() method and get brace brackets where you want the number to show up

x = "The price of Milk today is $ {}" 
y = 5
print(x.format(y))

# You can use multiple number of arguments in there. It places the numbers in order from left to right

milk = 5
lemons = 10
chocolate = 15
total = milk + lemons + chocolate
myOrder = " The total shopping bill after adding Milk ${}, Lemons ${} and Chocolate ${} is ${}"
print(myOrder.format(milk,lemons,chocolate,total))