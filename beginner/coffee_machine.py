MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 900,
    "milk": 700,
    "coffee": 100,
}

def is_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, we have insuffient ingredients for your {item}")
            return False
    return True


def Coffe_maker():
    is_on = True
    global profit
    while is_on:
        choice =  input("What would you like to have? (espresso/latte/cappuccino): ")
        if choice   == 'off':
            is_on = False
        elif choice == "report":
            print(f"Water: {resources['water']} ml")
            print(f"Milk : {resources['milk']} ml")
            print(f"Coffee: {resources['coffee']} gm")
            print(f"Profit : ${profit}")
        else:
            drink = MENU[choice]
            if is_sufficient(drink['ingredients']):
                print(f"{choice} costs {drink['cost']} ")
                money = int(input("Enter money you have: "))
                if money < drink['cost']:
                    print(f"Not Enough money for {choice}!!")
                else: 
                    for item in resources:
                        stuff = drink['ingredients']
                        resources[item] -= stuff[item]
                    profit += drink['cost']
                    cash = money - drink['cost']
                    if cash == 0:
                        print(f"Here you have your {choice}. Enjoy your day!!")
                    else:
                        print(f"Here is your change of {cash}!")
                        print(f"Here you have your {choice}. Enjoy your day!!")
                more = input("Do you wish to have something else? (y or n):")
                if more == 'y':
                    Coffe_maker()
                else:
                    is_on = False
            else:
                is_on = False        

Coffe_maker()