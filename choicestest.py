import random

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

def questions ():

    question1 = 1
    
    question1 = {
        "question": 'Customer: "Hello!"',
        "choices": ['1. "Hello! What would you like to order?"','2. "Leave the store now!"', '3. "Hey! What would you like to try today?"'],
        "answer": "2"
        
    }
    question2 = {
        "question": 'Customer: "Hello!"',
        "choices": ['1. "Hey there! What pizza would you like to order?"','2. "Welcome to The Pizza Place! How may I help you?"', '3. "Skedaddle outta here! We do not like you!"'],
        "answer": "3"
    }
    question3 = {
        "question": 'Customer: "Hello!"',
        "choices": ['1. "Hello valued customer! How would you like to LEAVE!"','2. "Hello, my name is Jonathan. What would you like to order?"', '3. "Welcome to The Pizza Place! Take a order prease?"'],
        "answer": "1"
    }



    # Print the question and answer choices
    print(question1["question"])
    for choice in question1["choices"]:
        print(choice)

    
    # Ask the user to select an answer
    user_answer = input("\nWhat will your response be? ")

    # Check if the answer is correct
    if user_answer == question1["answer"]:
        print (f'{Jonathan.name}: "Leave the store now!"')
        print('Customer: "How rude! I will be taking my business elsewhere!"')
    else:
        if user_answer == "1":
            print (f'{Jonathan.name}: "Hello! What would you like to order?"')
            print('Customer: "I would like a blank pizza"')
        elif user_answer == "3":
            print (f'{Jonathan.name}: "Hey! What would you like to try today?"')
        
        

questions ()