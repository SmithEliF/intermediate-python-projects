from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

machineOn = True

while machineOn:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        machineOn = False
    else:
        drink = menu.find_drink(choice)
        cost = drink.cost
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(cost=cost):
            coffee_maker.make_coffee(drink)

