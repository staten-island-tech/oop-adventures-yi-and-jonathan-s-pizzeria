import random
import sys, time

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
    print(f"\nThe customer tipped ${tip}")
    return tip   

def pizzatoppings ():

    toppings = ["cheese", "pepperoni", "sausage"]   
    order = random.choice(toppings)
    print(f'Customer: "I would like a {order} pizza!"')

def tips():
    tip = random.randint(0, 9)
    print(f"\nThe customer tipped ${tip}")
    return tip  

def questions ():
    print ("-------------------------------------")
    options = [
        {
            "dialogue": 'Customer: "Hello!"\n',
            "choices": [
                '1. "Hello! What would you like to order?"\n',
                '2. "What do you want, butt-face?"\n',
                '3. "We don\'t like your kind around here! Skedaddle!"\n'
            ],
            "correct_choice": 1
        },
        {
            "dialogue": 'Customer: "So many options..."\n',
            "choices": [
                '1. "Leave the store please, your face is unpleasing."\n',
                '2. "Stop bothering me."\n',
                '3. "Hey there, what pizza would you like to order?"\n'
            ],
            "correct_choice": 3
        },
        {
            "dialogue": 'Customer: "Hey! Lemme just think about what I want."\n',
            "choices": [
                '1. "I don\'t get paid enough to deal with people like you"\n',
                '2. "Take your time, valued customer!"\n',
                '3. "I don\'t have time... Chop chop buddy!."\n'
            ],
            "correct_choice": 2
        }
    ]
    customerresponses =[
        '\nCustomer: "How rude! I will be taking my business elsewhere!"',
        '\nCustomer: "Where is your manager?"',
        '\nCustomer: "All I wanted was a pizza..."'
    ]
    selected_option = random.choice(options)
    print(selected_option["dialogue"])
    for choice in selected_option["choices"]:
        print(choice)
    
    order_list = []

    user_choice = input("Enter a response: ")

    if user_choice == str(selected_option["correct_choice"]):
        print ("-------------------------------------")
        print("\nCongratulations! The customer is satfisfied!\n")
        print(f'Your wage is ${Yi.wage}')

        order_earning = Yi.wage + tips ()
        print (f'\nYour total earning for this order is ${order_earning}')

        order_list.append (order_earning)
        print ("-------------------------------------")
        print ('Would you like to continue your shift?\n')
        print ('1. Yes\n\n2. No\n')
        continue_game = input("Enter a response: ")
        
        if continue_game.lower() == "1":
            questions()
        else:
            total_earning = sum(order_list)  
            return sprint(f'Your total earning for your shift is ${total_earning}')
    else:
        customer = random.choice (customerresponses)
        print (customer)
questions ()