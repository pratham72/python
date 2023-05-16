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
    "money": 0,
}

def indi_of_coffee(na_coffee):
    order = MENU[na_coffee]["ingredients"]
    for item in order:
        resources[item] -= order[item]
    print(f"Here is your {na_coffee} ☕️. Enjoy!")
    print(resources)

def indi_is_not_suffi(na_coffee):
    order = MENU[na_coffee]["ingredients"]
    for item in order:
        if resources[item] <= order[item]:
            print(f"sorry there is no enough {item}.")
            return False
    return True



def calculate_coin(coffee_cost):
    """ penny is one cent.
        nickel is five cent.
        dime is ten cent.
        quarter is 25 cent."""
    print("please insert coins.")
    quarter = int(input("how many quarters? "))
    dime = int(input("how many dimes? "))
    nickles = int(input("how many nickles?"))
    penny = int(input("how many penny?"))
    inserted_coin = (quarter * 0.25) + (dime * 0.1) + (nickles * 0.05) + (penny * 0.01)
    round_inserted_coin = round(inserted_coin, 2)
    if coffee_cost > round_inserted_coin:
        print("Sorry that's not enough money. Money refunded.")
    else:
        rest_money = round((round_inserted_coin - coffee_cost), 2)
        print(f"Here is ${rest_money} in change.")
        
machine_is_off = True
while machine_is_off == True:
    choice_of_coffee = input("what would you like to have ? (espresso/latte/cappuccino): \n")
    if choice_of_coffee == 'off':
        machine_is_off = False
    elif choice_of_coffee == 'report':
        print(f"water : {resources['water']}",end= '\n' )
        print(f"milk : {resources['milk']}",end='\n')
        print(f"coffee : {resources['coffee']}",end='\n')
        print(f"money : {resources['money']}",end='\n')
    elif choice_of_coffee == 'espresso':
        if indi_is_not_suffi('espresso') == True:
            inserted_coin = calculate_coin(1.5)
            indi_of_coffee("espresso")
            resources["money"] = MENU["espresso"]["cost"] 
    elif choice_of_coffee == 'latte':
        if indi_is_not_suffi('latte') == True:
            inserted_coin = calculate_coin(2.5)
            indi_of_coffee("latte")
            resources["money"] = MENU["latte"]["cost"] 
    elif choice_of_coffee == 'cappuccino':
        indi_is_not_suffi('cappuccino')
        inserted_coin = calculate_coin(3.0)
        indi_of_coffee("cappuccino")
        resources["money"] = MENU["cappuccino"]["cost"] 