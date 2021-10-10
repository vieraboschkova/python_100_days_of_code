from data import MENU, resources, money_types
from art import logo



print(logo)

# Helpers
def check_if_choice_possible(choice, resources):
    if choice == "e":
        if resources["water"] >= 50 and resources["coffee"] >= 18:
            return True
    elif choice == "l":
        if resources["water"] >= 200 and resources["coffee"] >= 24 and resources["milk"] >= 150:
            return True
    elif choice == "l":
        if resources["water"] >= 250 and resources["coffee"] >= 24 and resources["milk"] >= 100:
            return True
    else:
        return False        
    
def get_drink(choice):
    if choice == "e":
        return MENU["espresso"]
    elif choice == "l":
        return MENU["latte"]
    elif choice == "l":
        return MENU["cappuccino"]
    else:
        return

def calculate_paid_money(number_of_quarters, number_of_dimes, number_of_nickles, number_of_pennies):
    total = 0
    total += number_of_quarters * money_types["quarter"]
    total += number_of_dimes * money_types["dime"]
    total += number_of_nickles * money_types["nickles"]
    total += number_of_pennies * money_types["penny"]
    return round(total, 2)

def get_change(cost, paid):
    return paid - cost

def make_drink(resources, chosen_drink, paid_money, had_change):
    new_resources = {
        "water": resources["water"] - chosen_drink["ingredients"]["water"],
        "coffee": resources["coffee"] - chosen_drink["ingredients"]["coffee"],
        "money": resources["money"] + chosen_drink["cost"],
    }

    if "milk" in chosen_drink["ingredients"]:
        new_resources["milk"] = resources["milk"] - chosen_drink["ingredients"]["milk"]
    else:
        new_resources["milk"] = resources["milk"]

    return new_resources


# Coffe machine code
def coffee_machine(resources):
    machine_on = True
    while machine_on:
        choice = input(f"""What would you like? Type:
            E for espresso ({MENU['espresso']['cost']}), 
            L for latte ({MENU['latte']['cost']}), 
            C for cappuccino ({MENU['cappuccino']['cost']}),
            or R for machine status report : """).lower()
        # print(choice)
        chosen_drink = get_drink(choice)
        # print(chosen_drink)
        if choice == "r":
            print(resources)
        elif choice == "l" or choice == "e" or choice == "c":
            can_be_made = check_if_choice_possible(choice, resources)
            if not can_be_made:
                print("Unsufficient resources")
            else:
                print("Sufficient resources! Insert your coins")
                number_of_quarters = int(input("How many quarters do you insert? "))
                number_of_dimes = int(input("How many dimes do you insert? "))
                number_of_nickles = int(input("How many nickles do you insert? "))
                number_of_pennies = int(input("How many pennies do you insert? "))
                paid_money = calculate_paid_money(number_of_quarters, number_of_dimes, number_of_nickles, number_of_pennies)
                print(f"You paid: {paid_money}$")
                if paid_money < chosen_drink["cost"]:
                    print("Unsufficient funds!")
                else:
                    change = get_change(chosen_drink["cost"], paid_money)
                    print(f"Your change is: {change}")
                    print("Starting your drink... 0%")
                    print("Starting your drink... 50%")
                    print("Starting your drink... 100%")
                    resources = make_drink(resources, chosen_drink, paid_money, had_change = True)
                    print(f"""
                    Resources left:
                    Water: {resources["water"]}
                    Coffee: {resources["coffee"]}
                    Milk: {resources["milk"]}
                    """)
                    if (resources["water"] == 0) or (resources["coffee"] == 0):
                        machine_on = False
                        print("Turning OFF. No more water or coffee")

        elif choice == "off":
            machine_on = False
            print("Turning OFF. Bye bye")
        else:
            print("Not on the menu, try again")

# Init machine
coffee_machine(resources)
