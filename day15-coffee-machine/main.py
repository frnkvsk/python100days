
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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

userInput = ''

def process_coin(amt, moneyIn):
   """Returns the amount of each coin"""
   if moneyIn == 'quarter' or moneyIn == 'quarters':
      return amt * .25
   elif moneyIn == 'dime' or moneyIn == 'dimes':
      return amt * .10
   elif moneyIn == 'nickel' or moneyIn == 'nickels':
      return amt * .05
   elif moneyIn == 'penny' or moneyIn == 'pennies':
      return amt * .01

def is_resources_sufficient(order_in):
   """Returns true if enough resources are available and false if not"""
   for x in order_in:
      if resources[x] < order_in[x]:            
         print(f'Sorry there is not enough {x}')
         return False
   return True

while userInput != 'off':
   userInput = input('What would you like? (espresso/latte/cappuccino): ').lower()
   if userInput == 'report':
      print("""
      Water: %sml
      Milk: %sml
      Coffee: %sg
      Money: $format(%s, '.2f')
      """ % (resources['water'], resources['milk'], resources['coffee'], format(profit, '.2f')))
   elif userInput == 'espresso' or userInput == 'latte' or userInput == 'cappuccino':
      ingredients = MENU[userInput]['ingredients']
      cost = float(MENU[userInput]['cost'])

      if is_resources_sufficient(ingredients):
         money_in = input(f'Your cost is ${format(cost,".2f")} please insert coins ').lower().split(',')
         for x in money_in:  
            moneyEach = x.split() 
            cost -= process_coin(float(moneyEach[0]), moneyEach[1])
         if cost <= 0:
            for e in ingredients:
               resources[e] = resources[e] - ingredients[e]
            profit = profit + float(MENU[userInput]['cost'])
            if cost < 0:
               print(f'Here is ${format(cost * -1, ".2f")} dollars in change.')
            print(f'Here is you {userInput}. Enjoy!')
         else:
            print("Sorry that's not enough money. Money refunded.")
   else:
      print(f"Sorry we don't have {userInput}, maybe you spelt it wrong?")