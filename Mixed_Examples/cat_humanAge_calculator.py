#Thanks Pondy
#This calculator converts cat years into human years
'''This information is purely for fun and not a suitable alternative to 
the cat age calculators available on the internet
''' 

humanYears = 0
catAgeYears = int(input("what is your cat's age in years?: "))

if (catAgeYears <= 2):
  humanYears = catAgeYears * 14
else: 
  humanYears = 28 + (catAgeYears - 2)*4

#simple formula derived from the Interweb, where first 2 years of cat is equivalent
#to 14 human years each, and after that is 4 year increment each year. 

print("Your cat is ",humanYears, "human years old ")  
