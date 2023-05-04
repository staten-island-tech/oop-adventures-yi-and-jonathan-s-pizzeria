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

def tips():
    tip = random.randint(0, 9)
    print(f"\nThe customer tipped ${tip}")
    return tip   

def cashiergame ():
    print('\nYour shift has begun!')

    customer = print('Customer: "Hello!"\n')
    

    correctanswers = ['1','3']
    choice1 = (f'1. "Hello! My name is {Jonathan.name}. What would you like to order?"')
    choice2 = ('2. "Leave the store now!"')
    choice3 = ('3. "Hey! What would you like to try today?"')
    customerresponse = ('Customer: "Hmm, I would like a pepperoni pizza"')
    orderlist = []
   
    print (choice1)
    print (choice2)
    print (choice3) 
    while True:
        response = input ("What will your response be?\n\n")
        if response in correctanswers:
            
            if response == '1':
                print (f'You: "Hello! My name is {Jonathan.name}. What would you like to order?')
            elif response == '3':
                print ('You: "Hey! What would you like to try today?"')
            print (customerresponse)
            order_earning = Jonathan.wage + tips ()
            print (f"Your wage is ${Jonathan.wage}")
            print (f'Your total earning for this order is ${order_earning}')

            orderlist.append(order_earning)
            

            keepplaying = input("Would you like to continue your shift? y/n \n\n")
            if keepplaying.lower() == 'y':
                print('\nCustomer: "Hello!"\n')
                print (choice1)
                print (choice2)
                print (choice3) 
            else:
                total_earning = sum(orderlist)
                return print(f'Your total earning for your shift is ${total_earning}\n')

        else:
            print ('You: "Leave the store now!"')
            print('Customer: "How rude! I will be taking my business elsewhere!"')
            



cashiergame ()