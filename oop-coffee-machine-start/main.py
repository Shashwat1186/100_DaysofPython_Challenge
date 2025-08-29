from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_machine_running = True

menu = Menu()
cof_maker = CoffeeMaker()
mon_machine = MoneyMachine()

while is_machine_running:
    choice = input(f"What would you like? ({menu.get_items()}): ")

    coffee_type = menu.find_drink(choice)

    if choice == "off" :
        is_machine_running = False
        print("Turning Off! ")

    if choice == "report" :
        cof_maker.report()
        mon_machine.report()
        continue

    if is_machine_running:
        sufficiency = cof_maker.is_resource_sufficient(coffee_type)
        if sufficiency:
            is_money_sufficient =  mon_machine.make_payment(coffee_type.cost)
            if is_money_sufficient:
                cof_maker.make_coffee(coffee_type)

    
            
            