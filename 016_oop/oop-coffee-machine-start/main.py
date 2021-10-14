from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_machine = CoffeeMaker()
my_machine.report()
my_menu = Menu()
my_money_machine = MoneyMachine()

machine_on = True

while machine_on:
    choice = input(f"""What would you like? Type:
    espresso ({my_menu.find_drink('espresso').cost}), 
    latte ({my_menu.find_drink('latte').cost}), 
    cappuccino ({my_menu.find_drink('cappuccino').cost}),
    or R for machine status report : """).lower()
    if choice == "r":
        my_machine.report()
    elif choice == "latte" or choice == "espresso" or choice == "cappuccino":
        chosen_drink = my_menu.find_drink(choice)
        can_be_made = my_machine.is_resource_sufficient(chosen_drink)
        if not can_be_made:
            print("Unsufficient resources")
        else:
            print("Sufficient resources! Insert your coins")
            paid_enough = my_money_machine.make_payment(chosen_drink.cost)
            if not paid_enough:
                print("Unsufficient funds!")
            else:
                print("Starting your drink... 0%")
                print("Starting your drink... 50%")
                print("Starting your drink... 100%")
                my_machine.make_coffee(chosen_drink)
                my_machine.report()
                if (my_machine.resources["water"] == 0) or (my_machine.resources["coffee"] == 0):
                        print(my_machine.resources)
                        machine_on = False
                        print("Turning OFF. No more water or coffee")
    elif choice == "off":
        machine_on = False
        print("Turning OFF. Bye bye")
    else:
        print("Not on the menu, try again")
