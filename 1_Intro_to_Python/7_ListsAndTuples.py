# Introduction to Lists and Tuples

# The main difference between the two is that you can add to a List but you can't add to a Tuple. List could be useful
# when you need to add elements on the go, while tuple is useful when you don't want the sequence to  change.

#declaring a list

weekdays = [
    'Sunday',
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday'
]

#accessing a list

print(weekdays[1:3])

#accessing a list backwards

print(weekdays[-3:-1])

# Creating a list from a string



# adding a sequence

total = [1,2,3] + [4,5,6]
print(total)

words = ['kia'] + ['ora']
print(words)

# note you cannot add a sequence of numbers and string

# checking for membership in a list

secure_vault = [
    ['alpha', '7899'],
    ['bravo', '4566'],
    ['charlie', '1233']

]

username = input('Please enter your username: ')
pin = input('Please enter your pin: ')

if [username, pin] in secure_vault:
    print('Access granted')
else: 
    print('Access not granted')

####################################################################################





