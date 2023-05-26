import random
import sys,time

print ("The Pizza Place")
print ("-------------------------------------")
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

def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(3./150)


Jonathan = cashier ('Jonathan Chan', 15, 15, 'To take orders from customers.')
Yi = cook ('Yi Cheng', 15, 20, 'To cook pizza for the customers.')

def tips():
    tip = random.randint(0, 9)
    sprint(f"\nThe customer tipped ${tip}")
    return tip   
    
def cookgame():
    toppings = ["cheese", "pepperoni", "sausage"]       
    order = random.choice(toppings)
    sprint('Your shift has begun!\n')
    sprint(f"Your customer has ordered a {order} pizza!")
    
    orderlist = []
    
    while True:
        print ('\nWhat pizza would you like to cook?  \n')
        choice = input ('Enter a response: ')
        if choice.lower() == order:
            sprint ("\nYou've cooked a " + choice + " pizza!\n")
            sprint ('Customer: "Thank you! I love a good ' + choice + ' pizza!" \n')
            sprint(f'Your wage is ${Yi.wage}')
            order_earning = Yi.wage + tips ()
            sprint (f'\nYour total earning for this order is ${order_earning}')
            
            orderlist.append(order_earning)
            
            print ('\nWould you like to continue your shift?\n\n1. Yes\n\n2. No \n ')
            choice = input ('Enter a response: ')
            print ('')
            if choice.lower() == '1':
                order = random.choice(toppings)
                sprint(f"Your customer has ordered a {order} pizza!")
            else:
                
                total_earning = sum(orderlist)  
                return sprint(f'Your total earning for your shift is ${total_earning}')
        else:
            sprint ("\nYou've cooked a " + choice + " pizza!\n")
            sprint ("Customer: I didn't order a " + choice + " pizza, you idiot!")

def cashiergame ():
    print('Your shift has begun!\n')
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
    sprint ('Choose your character! \n\n1. Jonathan Chan (cashier) \n\n2. Yi Cheng (cook)\n')
    game = input ('Enter a response: ')
    if game == '2':
        print ('--------------------------------------')
        cookgame ()
    else:
        cashiergame ()


def start ():
    sprint ('Do you want to play?\n \n'"1. Yes, let's go! \n\n2. No, this game sucks.\n")
    answer = input ('Enter a response: ') 
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
            sprint ('\nDo you want to play?\n \n'"1. Yes, let's go! \n\n2. No, this game sucks.\n")
            answer = input ('Enter a response:') 
            sprint (answer)
            
            sprint ('\nGet ready to work!') 
            print ('---------------------------------------')
            main ()


start()