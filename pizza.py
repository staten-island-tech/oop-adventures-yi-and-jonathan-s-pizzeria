import sys,time
import random

def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(3./150)

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
        choice = input('\nWhat pizza would you like to cook? \n \n')
        if choice.lower() == order:
            
            sprint(f'\nYour wage is ${Yi.wage}')
            order_earning = Yi.wage + tips ()
            sprint (f'\nYour total earning for this order is ${order_earning}')
            
            orderlist.append(order_earning)
            
            choice = input('\nWould you like to continue your shift? y/n \n \n')
            if choice.lower() == 'y':
                order = random.choice(toppings)
                sprint(f"Your customer has ordered a {order} pizza!")
            else:
                
                total_earning = sum(orderlist)  
                return sprint(f'\nYour total earning for your shift is ${total_earning}')
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
    sprint ('\nDo you want to play?\n \n'"1. Yes, let's go! \n\n2. No, this game sucks.\n")
    answer = input ('Enter a response: ') 
    sprint (answer)
    if answer == '1':
        sprint ('\nGet ready to work!') 
        print ('---------------------------------------')
        main ()
    
    else:
        sprint ('\nAre you sure??\n\n1. Yes, I am sure!\n\n2. No... on second thought...\n')
        answer2 = input ('Enter a response: ')
        if answer2 == '1':
            sprint ('\nToo bad, maybe next time.')
        else:
            sprint ('\nDo you want to play?\n \n'"1. Yes, let's go! \n\n2. No, this game sucks.\n\n")
            answer = input ('Enter a response:') 
            sprint (answer)
            
            sprint ('\nGet ready to work!') 
            print ('---------------------------------------')
            main ()


start ()
