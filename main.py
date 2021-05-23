from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
is_machine_on = True
menu = Menu()


while is_machine_on:
    options = menu.get_items()
    choice = input(f"What do you want to drink? ({options})").lower()
    if choice == "off":
        is_machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        

