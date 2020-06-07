#Simple calculator no GUI. Make Functions for each operation. 

#Function to add
def add(x, y): #receives two inputs
    return x + y

#Function to subtract
def subtract(x, y):
    return x - y

#Function to divide
def divide(x, y):
    return x / y

#Function to multiply
def multiply(x, y):
    return x * y

#Function for square
def square(x):
    return x * x

#Function for squareroot
def squareroot(x):
    return x ** (1.0/ 2)

print("Basic Calculator")
print("1- Add")
print("2 - Subtract")
print("3 - Divide")
print("4 - Multiply")
print("5 - Square")
print("6 - Square root")
    #Accept user input
    

while True:
    choice = input("Select 1/2/3/4/5/6 from above list: ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    
        
            
        if choice == '1':
            print(num1, '+', num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, '-', num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif choice == '4':
            print(num1, '*', num2, "=", multiply(num1, num2))
        break
    # had to separate this section as it took only one value
    elif choice in ('5', '6'):
        num = float(input("Enter number: "))

        if choice == '5':
            print('Square of ', num , '=', square(num))
        else:
            print('Square Root of ', num, '=', squareroot(num))
        break
    else:
        print('invalid number')      
