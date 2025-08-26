#Constants
QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 50,
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
money = 0
#function to give report
def report(resources, money):
    print(f"Water : {resources['water']}ml")
    print(f"Milk : {resources['milk']}ml")
    print(f"Coffee : {resources['coffee']}g")
    print(f"Money : ${money}")

#create a func to check if resources are sufficient
def check_resources(coffee_desc, resources, is_order_running):
    for item in resources:
        if coffee_desc['ingredients'][item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            is_order_running = False
            break
    return is_order_running

#create a function to make changes in the resouces 
def upadte_resources(coffee_desc, resources, money):
    for item in resources:
        resources[item] = resources[item] - coffee_desc['ingredients'][item]
    money = money + coffee_desc['cost']
    return resources, money

#create a function which returns idx of coffee type
def coffee_type_menu(MENU, coffee_type):
    for coffee in MENU:
        if coffee == coffee_type:
            return MENU[coffee], coffee

#create a function to process coins, calculate monetary value of coins inserted 
def process_coins(num_quarters, num_dimes, num_nickels, num_pennies):
    total = 0
    total = QUARTERS*num_quarters + DIMES*num_dimes + NICKLES*num_nickels + PENNIES*num_pennies
    return total

# create function to calculate change function which calculates change
def calculate_change(total, coffee_desc):
    return round(total - coffee_desc['cost'], 2)

# create a function to check if user has entered enough money for the transaction to happen
def money_validity(coffee_desc, total):
    return total >= coffee_desc['cost'] 


is_machine_running = True

while is_machine_running:
    is_order_running = True
    while is_order_running:
        #ask for user input
        coffee_type = input("What would you like? (espresso/latte/cappuccino): ")

        #turn off if coffee type is off
        if coffee_type == "off" :
            is_machine_running = False
            print("Turning Off! ")
            break

        if coffee_type == "report" :
            report(resources, money)
            continue
        
        coffee_desc, coffee_name = coffee_type_menu(MENU, coffee_type)
        is_order_running = check_resources(coffee_desc, resources, is_order_running)
        if is_order_running:
            print("Please insert coins.")
            num_quarters = int(input("How many quarters?: "))
            num_dimes = int(input("How many dimes?: "))
            num_nickles = int(input("How many nickles?: "))
            num_pennies = int(input("How many pennies?: "))

            
            total_coins = process_coins(num_quarters, num_dimes, num_nickles, num_pennies)
            change = calculate_change(total_coins, coffee_desc)

            if money_validity(coffee_desc, total_coins):
                print(f"Here's ${change} in change.")
                resources, money = upadte_resources(coffee_desc, resources, money)
                print(f"Here is your {coffee_name}, Enjoy!")
            elif not money_validity(coffee_desc, total_coins):
                print("Sorry that's not enough money. Money refunded.")

        


            

