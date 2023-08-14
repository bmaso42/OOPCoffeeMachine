from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()


def report():
    coffee_maker.report()
    money_machine.report()


def process_coins():
    money_machine.process_coins()


def prompt():
    result = input("What would you like? (espresso/latte/cappuccino): ")
    return result


def main_function():
    terminate = False
    while not terminate:
        command = prompt()
        if command.lower() == "off":
            terminate = True
        elif command.lower() == "report":
            report()
        else:
            drink = menu.find_drink(command)
            resources = coffee_maker.is_resource_sufficient(drink)
            if resources:
                payment = money_machine.make_payment(drink.cost)
                if payment:
                    coffee_maker.make_coffee(drink)


main_function()

