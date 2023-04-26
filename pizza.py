import random

print ("The Pizza Place")

class worker:
    def __init__(self, name, age, wage):
        self.name = name
        self.age = age
        self.wage = wage

class cashier (worker):
    def __init__(self, name, age, wage, job):
        super().__init__(name, age, wage)
        self.job = job
class cook (worker):
    def __init__(self, name, age, wage, job):
        super().__init__(name, age, wage)
        self.job = job

Jonathan = cashier ('Jonathan Chan', 15, 15, 'To take orders from customers.')
Yi = cook ('Yi Cheng', 15, 20, 'To cook pizza for the customers.')

def cookgame ():
    toppings = ["cheese", "pepperoni","sausage"]
    order = random.choice(toppings)
    print(f"Your customer has ordered a {order} pizza!")
    while True:
        choice = input ('What pizza would you like to cook?')
        if choice == order:
            print (f"Correct! You've earned {Yi.wage} dollars!")
            return Yi.wage
        else: 
            print ('Wrong! Try again.')

def cashiergame ():
    prices = ["8", "10" , "12"]
    order = random.choice(prices)
    print(f"The customer gives you ")
    while True:
        choice = input ('What pizza did the customer order?')
        if choice == order:
            print (f"Correct! You've earned {Jonathan.wage} dollars!")
            return Jonathan.wage
        else: 
            print ('Wrong! Try again.')

    

def main ():
    game = input ('Who would you like to play as? Jonathan Chan (cashier) or Yi Cheng (cook)')
    if game.capitalize == 'cook' or 'Yi Cheng':
        print ("You've chosen the cook!")
        cookgame ()
    else:
        print ("You've chosen the cashier!")


def start ():
    start = input ('Do you want to play? y/n')
    if start == 'y':
        print ('Get ready to work!') 
        main ()
    else:
        print ('Too bad, maybe next time')

start ()

