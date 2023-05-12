import random

print ("The Pizza Place")
money = []
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
    print(f"\nThe customer tipped ${tip}")
    return tip   
    
def cookgame():
    toppings = ["cheese", "pepperoni", "sausage"]   
    order = random.choice(toppings)
    print(f"Your customer has ordered a {order} pizza!")
    
    orderlist = []
    
    while True:
        choice = input('\nWhat pizza would you like to cook? \n \n')
        if choice.lower() == order:
            order_earnings = Yi.wage + tips ()
            print(f'Your wage is ${Yi.wage}')
            print (f'Your total earning is for this order is ${order_earnings}')
            orderlist.append(order_earnings)
            choice = input('\nWould you like to continue? y/n ')
            if choice.lower() == 'y':
                    order = random.choice(toppings)
                    print(f"Your customer has ordered a {order} pizza!")
            else:
                totalorderearnings = sum(orderlist)
                return print (f'Your total earning for your shift is ${totalorderearnings}')
        else: 
            print ('Wrong! Try again or check your spelling.')

def cashiergame ():
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

# def cookcontinue ():    
#     while input ('\nDo you want to continue? y/n ') == "y" :
#         cookgame () 
#     else:
#         print ('test')
def main ():
    game = input ('Who would you like to play as? Jonathan Chan (cashier) or Yi Cheng (cook) ')
    if game.lower() == 'cook':
        print ("\nYou've chosen the cook!\n ")
        cookgame ()
        # cookcontinue ()
    else:
        print ("You've chosen the cashier!")
        cashiergame ()


def start ():
    start = input ('Do you want to play? y/n ')
    if start == 'y':
        print ('Get ready to work!') 
        main ()
    else:
        print ('Too bad, maybe next time...')


cookgame()

