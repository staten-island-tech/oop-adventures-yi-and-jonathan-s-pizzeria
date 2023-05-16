import random
import sys,time


def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(3./150)

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

cookgame ()