import sys,time
import random

def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(3./100)

print ("The Pizza Place")
print ("---------------------------------------")
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

def tips():
    tip = random.randint(0, 9)
    sprint(f"\nThe customer tipped ${tip}")
    return tip   
    
def cookgame():
    toppings = ["cheese", "pepperoni", "sausage"]   
    order = random.choice(toppings)
    sprint('\nYour shift has begun!\n')
    sprint(f"Your customer has ordered a {order} pizza!")
    
    orderlist = []
    
    while True:
        choice = input(sprint('\nWhat pizza would you like to cook? \n \n'))
        if choice.lower() == order:
            order_earning = Yi.wage + tips ()
            sprint(f'Your wage is ${Yi.wage}')
            sprint (f'Your total earning for this order is ${order_earning}')
            
            orderlist.append(order_earning)
            
            choice = input('\nWould you like to continue your shift? y/n \n \n')
            if choice.lower() == 'y':
                order = random.choice(toppings)
                sprint(f"Your customer has ordered a {order} pizza!")
            else:
                
                total_earning = sum(orderlist)  
                return sprint(f'Your total earning for your shift is ${total_earning}')
        else:
            sprint('Wrong! Try again.')

def cashiergame ():
    print('\nYour shift has begun!\n')
    toppings = ["cheese", "pepperoni","sausage"]
    prices = ["8", "10" , "12"]
    order = random.choice(prices)
    print(f"Your customer has ordered a {prices} pizza!")
    while True:
        choice = input ('What pizza did the customer order?')
        if choice == order:
            print (f"Correct! You've earned {Jonathan.wage} dollars!")
            return Jonathan.wage
        else: 
            print ('Wrong! Try again.')

def main ():
    game = input('\nWho would you like to play as? Jonathan Chan (cashier) or Yi Cheng (cook)\n \n')
    if game.lower() == 'cook':
        print ('---------------------------------------')
        cookgame ()
    else:
        cashiergame ()


def start ():
    start = input ('\nDo you want to play? y/n \n \n')
    if start == 'y':
        sprint ('\nGet ready to work!') 
        print ('---------------------------------------')
        main ()
    else:
        sprint ('Too bad, maybe next time')

start ()
