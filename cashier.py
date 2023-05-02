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

def cashiergame ():
    print('\nYour shift has begun!\n')

    print('Customer: "Hello!"\n')
    

    correctanswers = ['1','3']
    choice1 = ('1. "Hello! What would you like to order?"')
    choice2 = ('2. "Leave the store now!"')
    choice3 = ('3. "Hey! What would you like to try today?"')
    customerresponse = ('Customer: "Hmm, I would like a pepperoni pizza"')
   
    print (choice1)
    print (choice2)
    print (choice3) 
    while True:
        response = input ("What will your response be?\n\n")
        if response in correctanswers:
            if response == '1':
                print (f'You: "Hello! What would you like to order?')
            elif response == '3':
                print (f'You: "Hey! What would you like to try today?"')
            print (customerresponse)

            print (f"You've made ${Jonathan.wage}")

            keepplaying = input("Would you like to continue your shift?")
            if keepplaying.lower == 'y':
                print (choice1)
                print (choice2)
                print (choice3) 
                response = input ("What will your response be?\n\n")
            else:
                print ('placeholder')

        else:
            print ('You: "Leave the store now!"')
            print('Customer: "How rude! I will be taking my business elsewhere!"')



cashiergame ()