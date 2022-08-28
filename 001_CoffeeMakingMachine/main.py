
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#create instance of classes
money_machine= MoneyMachine()
coffee_maker =CoffeeMaker()
menu =Menu()
is_on =True
#  1.print report
coffee_maker.report()
money_machine.report()

#  2.check resources sufficient?

while is_on:
    options=menu.get_items()
    choice =input(f"What would you like? ({options}):")
    if choice =="off":
        is_on=False
    elif choice=="report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(choice)
# 3.Process coins and
# 4.check transaction sucessful?
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            # 5.Make coffee
            coffee_maker.make_coffee(drink)
