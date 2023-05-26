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

def question1 ():
        
    question = {
    "question": 'Customer: "Hello!"',
    "choices": ['1. "Hello! What would you like to order?"','2. "Leave the store now!"', '3. "Hey! What would you like to try today?"'],
     "answer": "2" }
    print(question["question"])
    for choice in question["choices"]:
        print(choice)

    user_answer = input("\nWhat will your response be? ")

    while user_answer == question["answer"]:
        print (f'{Jonathan.name}: "Leave the store now!"')
        ('Customer: "How rude! I will be taking my business elsewhere!"')
    else:
        if user_answer == "1":
            print (f'{Jonathan.name}: "Hello! What would you like to order?"')
            pizzatoppings ()
        elif user_answer == "3":
            print (f'{Jonathan.name}: "Hey! What would you like to try today?"')
            pizzatoppings ()
def question2 ():
    question = {
    "question": 'Customer: "Hello!"',
    "choices": ['1. "Hey there! What pizza would you like to order?"','2. "Welcome to The Pizza Place! How may I help you?"', '3. "Skedaddle outta here! We do not like you!"'],
    "answer": "3"
    }
    print(question["question"])
    for choice in question ["choices"]:
        print(choice)

    user_answer = input ("\n What will your response be?")
    if user_answer == question["answer"]:
        print (f'{Jonathan.name}: "Skedaddle outta here! We do not like you!"')
        print('Customer: "How rude! I will be taking my business elsewhere!"')
    else:
        if user_answer == "1":
            print (f'{Jonathan.name}: "Hey there! What pizza would you like to order?"')
            pizzatoppings ()
        elif user_answer == "2":
            print (f'{Jonathan.name}: "Welcome to The Pizza Place! How may I help you?"')
            pizzatoppings ()
def question3 ():
    question = {
    "question": 'Customer: "Hello!"',
    "choices": ['1. "Hello valued customer! How would you like to LEAVE!"','2. "Hello, my name is Jonathan. What would you like to order?"', '3. "Welcome to The Pizza Place! Take a order prease?"'],
    "answer": "1"
    }
    print(question["question"])
    for choice in question ["choices"]:
        print(choice)

    user_answer = input ("\n What will your response be?")
    if user_answer == question["answer"]:
        print (f'{Jonathan.name}: "Hello valued customer! How would you like to LEAVE!"')
        print('Customer: "How rude! I will be taking my business elsewhere!"')
    else:
        if user_answer == "2":
            print (f'{Jonathan.name}: "Hello, my name is Jonathan. What would you like to order?"')
            pizzatoppings ()
        elif user_answer == "3":
            print (f'{Jonathan.name}: "Welcome to The Pizza Place! Take a order prease?"')
            pizzatoppings ()


def randomquestions ():
    questionlist =[question1 (), question2 (), question3 ()]
    generate = random.choice(questionlist)
    print (generate)
    orderlist = []

    

def cookgame():
    toppings = ["cheese", "pepperoni", "sausage"]       
    order = random.choice(toppings)
    print (order)
    
    orderlist = []
    

#cookgame()
randomquestions ()

