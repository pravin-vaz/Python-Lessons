# from https://codereview.stackexchange.com/questions/176377/mcdonalds-food-order-system
# Will be very useful when you are showing how to setup a simple ordering system


import collections
from string import capwords


def foodplan(price, stock):
    if not str(stock).isdecimal():
        raise ValueError("Can only assign a whole number to stock attribute")
    return type('FoodPlan', (object,), dict(price=float(price), stock=int(stock)))


def get_choice():
    while True:
        option = input("What would you like? ")
        if option.isdecimal() and 0 <= int(option) - 1 < len(choices):
            return list(choices.keys())[int(option) - 1]
        elif capwords(option) in choices.keys():
            return capwords(option)
        else:
            print("Invalid item")


def get_quantity(choice):
    while True:
        quantity = input("How many would you like? ")
        if quantity.isdecimal():
            if int(quantity) <= choices[choice].stock:
                return int(quantity)
            else:
                print("There is not enough stock!")
        else:
            print("Illegal quantity")


choices = collections.OrderedDict({
    "Big Mac": foodplan(2.50, 50),
    "Large Fries": foodplan(0.50, 200),
    "Vegetarian Burger": foodplan(1.00, 20),
})


if __name__ == '__main__':

    orders = dict(zip(choices.keys(), [0] * len(choices)))

    print("Welcome to McDonald's")
    ordering = 'y'
    while ordering == 'y':
        [print("{0}. {1}, £{2}".format(
            i + 1, list(choices.keys())[i], list(choices.values())[i].price
        )) for i in range(len(choices))]
        choice = get_choice()
        quantity = get_quantity(choice)
        orders[choice] += quantity
        choices[choice].stock -= quantity
        ordering = input("Do you want to order more items? [y/n] ").lower()
    print("\nThank you for ordering!\nYour total cost is: £{0}".format(
        sum([orders[choice] * choices[choice].price 
        for choice in choices.keys()])
    ))
