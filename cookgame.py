import random
import sys, time
import pizza

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
     time.sleep(3./250)

Jonathan = cashier ('Jonathan Chan', 15, 15, 'To take orders from customers.')
Yi = cook ('Yi Cheng', 15, 20, 'To cook pizza for the customers.')

def tips():
    tip = random.randint(0, 9)
    print(f"\nThe customer tipped ${tip}")
    return tip   

def game():
    toppings = ["cheese", "pepperoni", "sausage"]       
    order = random.choice(toppings)
    sprint('Your shift has begun!\n')
    sprint(f"Your customer has ordered a {order} pizza!")
    
    orderlist = []
    
    while True:
        print ('\nWhat pizza would you like to cook?  \n')
        choice = input ('Enter a response: ')
        if choice.lower() == order:
            sprint ('\nCooking...')
            time.sleep(2)
            sprint ("\nYou've cooked a " + choice + " pizza!\n")
            sprint ('Customer: "Thank you! I love a good ' + choice + ' pizza!" ')
            print ("-" * 48)
            sprint(f'Your wage is ${Yi.wage}')
            order_earning = Yi.wage + tips ()
            sprint (f'\nYour total earning for this order is ${order_earning}')
            print ("-" * 48)
            
            orderlist.append(order_earning)
            
            print ('\nWould you like to continue your shift?\n\n1. Yes\n\n2. No \n ')
            choice = input ('Enter a response: ')
            print ('')
            if choice.lower() == '1':
                order = random.choice(toppings)
                sprint(f"Your customer has ordered a {order} pizza!")
            else:
                
                total_earning = sum(orderlist)  
                sprint(f'Your total earning for your shift is ${total_earning}')
                print ("-" * 48)
                print ('Options\n')
                sprint ('1. Play Again\n\n2. Main Menu\n')
                restart = input ('Enter a reponse: ')
                if restart == '1':
                    print ("-" * 48)
                    pizza.select()
                else: 
                    print ("-" * 48)
                    pizza.start ()
                if total_earning > 200:
                    print ('\nWow, you really have no life. You\'ve played a high school student\'s crappy game for this long? Shame.')
                    break
                break
        else:
            sprint ("\nYou've cooked a " + choice + " pizza!\n")
            sprint ("Customer: I didn't order a " + choice + " pizza, you idiot!")
            sprint ('\nGame Over!')
            print ("-" * 48)
            print ('Options\n')
            sprint ('1. Continue\n\n2. Main Menu\n')
            restart = input ('Enter a reponse: ')
            print ('')
            if restart == '1':
                print ("-" * 48)
                pizza.select()
            else: 
                print ("-" * 48)
                pizza.start ()