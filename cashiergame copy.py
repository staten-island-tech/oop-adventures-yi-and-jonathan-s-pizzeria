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
    options = [
        {
            "dialogue": 'Customer: "Hello!"',
            "choices": [
                '1. "Hello! What would you like to order?"',
                '2. "What do you want?"',
                '3. "We don\'t like your kind around here! Skedaddle!"'
            ],
            "correct_choice": 1
        },
        {
            "dialogue": 'Customer: "So many options..."',
            "choices": [
                '1. "Leave the store please, your face is unpleasing"',
                '2. "Stop bothering me."',
                '3. "Hey there, what pizza would you like to order?"'
            ],
            "correct_choice": 3
        },
        {
            "dialogue": 'Customer: "Hey! Lemme just think about what I want."',
            "choices": [
                '1. "I don\'t get paid enough to deal with people like you"',
                '2. "Take your time, valued customer!"',
                '3. "I don\'t have time... Chop chop buddy!."'
            ],
            "correct_choice": 2
        }
    ]

    selected_option = random.choice(options)
    print(selected_option["dialogue"])
    for choice in selected_option["choices"]:
        print(choice)

    user_choice = input("Enter a response: ")

    if user_choice == str(selected_option["correct_choice"]):
        print("Congratulations!")
        print(f'Your wage is ${Yi.wage}')
        order_list = []
        order_earning = Yi.wage + tips ()
        print (f'\nYour total earning for this order is ${order_earning}')

        order_list.append (order_earning)

        print ('Would you like to continue your shift?')
        print ('1. Yes\n2. No')
        continue_game = input("Enter a response: ")
        if continue_game.lower() == "1":
            questions()
        else:
            total_earning = sum(order_list)  
            return sprint(f'Your total earning for your shift is ${total_earning}')
    else:
        print("Oops! That was a rude response. You lost. Game Over.")
questions ()