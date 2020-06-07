# Program receives user input in form of year, month(1-12) and day (1-31) and  then prints out a date in readable format

# Make a list of months 

months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

# This list is to complete the endings for day 

endings = ['st', 'nd', 'rd' ] + 17 * ['th'] + ['st', 'nd', 'rd' ] + 7 * ['th'] + ['st']

#user input

year = input('Year: ')
month = input('Month(1-12): ')
day = input('Day(1-31): ')

month_number = int(month)
day_number = int(day)

#Remember to subtract 1 from month and day to get the correct index

month_name = months[month_number -1]
ordinal = day + endings[day_number-1]


