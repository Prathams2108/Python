import os
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: 1. print all resources in the coffee machine
# TODO: 2. check if sufficient resources are available to make the drink
# TODO: 3. process the coins
# TODO: 4. check if the transaction is successful
# TODO: 5. DEDUCT ReSOURCES AFTER EVERY DRINK


def drink(r1, r2, r3,c):

    if r1 > resources["water"] or r2 > resources["coffee"]:
        print("Resources are unavailable for the the drink you have requested.")
    else:
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?:"))
        nickles = int(input("How Many nickles?: "))
        pennies = int(input("How many pennies?: "))
        total = coincalci(quarters, dimes, nickles, pennies)
        if total < c:
            print("Sorry you do not have enough money to buy this drink.")
        elif total >= c:
            change = total - c
            print(f"Here is your change: {change}")
            print("Enjoy Your drink ☕")
            resources["water"] -= r1
            resources["coffee"] -= r2
            resources["milk"] -= r3

def coincalci(q, d, n, p):
    return (0.25 * q) + (0.10 * d) + (0.05 * n) + (0.01 * p)


machineon = True
while machineon:

    drinkoption = input("What would you like to have? (espresso/latte/cappuccino)").lower()
    os.system('cls')
    if drinkoption == "espresso":
        resource1 = MENU["espresso"]["ingredients"]["water"]
        resource2 = MENU["espresso"]["ingredients"]["coffee"]
        resource3 = 0
        cost=MENU["espresso"]["cost"]
        drink(resource1, resource2, resource3,cost)
    elif drinkoption == "latte":
        resource1 = MENU["latte"]["ingredients"]["water"]
        resource2 = MENU["latte"]["ingredients"]["coffee"]
        resource3 = MENU["latte"]["ingredients"]["milk"]
        cost = MENU["latte"]["cost"]
        drink(resource1, resource2, resource3,cost)
    elif drinkoption == "cappuccino":
        resource1 = MENU["cappuccino"]["ingredients"]["water"]
        resource2 = MENU["cappuccino"]["ingredients"]["coffee"]
        resource3 = MENU["cappuccino"]["ingredients"]["milk"]
        cost = MENU["cappuccino"]["cost"]
        drink(resource1, resource2, resource3,cost)
    elif drinkoption == "report":
        w = resources["water"]
        m = resources["milk"]
        c = resources["coffee"]
        print(f"Water: {w}\nMilk: {m}\nCoffee: {c}")
    else:
        print("Sory! This drink is not available")
    user = input("Would you like to have another drink?Enter(y/n): ").lower()
    if user == "y":
        machineon = True
    elif user == "n":
        machineon = False
    else:
        print("Enter the correct option.")