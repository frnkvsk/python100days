
class Latte:
   def __init__(self, beans, water, milk, syrup):
      self.beans = beans
      self.water = water
      self.milk = milk
      self.syrup = syrup
      self.
class Cappuccino:
   def __init__(self, beans, water, milk):
      self.beans = beans
      self.water = water
      self.milk = milk
class PumpkinSpice:
   def __init__(self, beans, water, milk, spices, vanilla):
      self.beans = beans
      self.water = water
      self.milk = milk
      self.spices = spices
      self.vanilla = vanilla
   
latte = Latte(100, 100, 100, 100)
cappuccino = Cappuccino(100, 100, 100)
pumpkinSpice = PumpkinSpice(100, 100, 100, 100, 100)

def totalBeans():
   return latte.beans + cappuccino.beans + pumpkinSpice.beans
def totalWater():
   return latte.water + cappuccino.water + pumpkinSpice.water
def totalMilk():
   return latte.milk + cappuccino.milk + pumpkinSpice.milk
def totalSyrup(): 
   return latte.syrup
def totalSpices():
   return pumpkinSpice.spices
def totalVanilla():
   return pumpkinSpice.vanilla
 
userInput = ''

while userInput != 'off':
   print('What would you like? (espresso/latte/cappuccino):')
   userInput = input()
   if userInput == 'report':
      print("""
      Beans: %sg
      Water: %sml
      Milk: %sml
      Syrup: $%sml
      Spices: %sg
      Vanilla: %sml
      """ % (totalBeans(), totalWater(), totalMilk(), totalSyrup(), totalSpices(), totalVanilla()))
   elif userInput.upper() == 'LATTE':
      print('Latte')
   elif userInput.upper() == 'CAPPUCCINO':
      print('Cappuccino')
   elif userInput.upper() == 'PUMPKINSPICE':
      print('Pumpkin Spice')