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

def game ():
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
        },
        {
            "dialogue": 'Customer: "How\'s it going man! I would like to place an order."\n',
            "choices": [
                '1. "Of course! What would you like to try today?"\n',
                '2. "You look like you have ate too much pizza, man. I think you should lay it off."\n',
                '3. "How would you like to leave?."\n'
            ],
            "correct_choice": 1
        },
        {
            "dialogue": 'Customer: "Herro! Is this City Pizza?"\n',
            "choices": [
                '1. "You are not South Park."\n',
                '2. "Herro! City Pizza! Take a order prease?"\n',
                '3. "Do your parents love you?"\n'
            ],
            "correct_choice": 2
        },
        {
            "dialogue": 'Customer: "Hey pretty boy!"\n',
            "choices": [
                '1. "Pervert!"\n',
                '2. "Don\'t talk to me with that disrespect."\n',
                '3. "Hey... weird response but... what like you like to order..?"\n'
            ],
            "correct_choice": 3
        }
    ]
    customerresponses =[
        '\nCustomer: "How rude! I will be taking my business elsewhere!"',
        '\nCustomer: "Where is your manager?"',
        '\nCustomer: "All I wanted was a pizza..."',
        '\nCustomer: "Meet me outside. I\'m going to knock your ass out."',
        '\nCustomer: "Is that any way you talk to a valued customer?"'

    ]
    
    order_list = []
    while True:
        selected_option = random.choice(options)
        print(selected_option["dialogue"])
        for choice in selected_option["choices"]:
            print(choice)
        
        

        user_choice = input("Enter a response: ")

        if user_choice == str(selected_option["correct_choice"]):
            print ("-" * 48)
            sprint("Congratulations! The customer is satfisfied!\n")
            print(f'Your wage is ${Jonathan.wage}')

            order_earning = Jonathan.wage + tips ()
            sprint (f'\nYour total earning for this order is ${order_earning}')

            order_list.append (order_earning)
            print ("-" * 48)
            sprint ('Would you like to continue your shift?\n')
            sprint ('1. Yes\n\n2. No\n')
            continue_game = input("Enter a response: ")
            print ("-" * 48)
            
            if continue_game == '2':
                total_earning = sum(order_list)  
                sprint(f'Your total earning for your shift is ${total_earning}')
                print ("-" * 48)
                print ('Options\n')
                sprint ('1. Play Again\n\n2. Main Menu\n')
                restart = input ('Enter a reponse: ')
                print ('')
                if restart == '1':
                    print ("-" * 48)
                    pizza.select()
                else: 
                    ("-" * 48)
                    pizza.start ()
                if total_earning > 200:
                    print ('\nWow, you really have no life. You\'ve played a high school student\'s crappy game for this long? Shame.')
                    break
                break
        else:
            customer = random.choice (customerresponses)
            sprint (customer)
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
