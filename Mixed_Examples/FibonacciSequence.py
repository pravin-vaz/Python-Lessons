#Basically the program will add to the previous number and print it out, while looping for 'n' number of times. 

a,b = 0,1               
n = 10
for i in range(n):
    a,b = b,a+b
    print(b)