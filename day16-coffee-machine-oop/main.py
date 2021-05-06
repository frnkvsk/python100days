from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

userInput = ''

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while userInput != 'off':
   userInput = input('What would you like? (espresso/latte/cappuccino/): ')
   if userInput == 'report':
      coffee_maker.report()
      money_machine.report()
   else:
      drink = menu.find_drink(userInput)
      if drink and coffee_maker.is_resource_sufficient(drink):
         money_machine.make_payment(drink.cost)
         coffee_maker.make_coffee(drink)
      
