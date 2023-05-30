import random
import sys,time
import cashiergame
import cookgame

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

def titlescreen():
    print ("                City Pizza™\n")
    sprint ('A Pizza Place Sim by Yi Cheng and Jonathan Chan')
    print ("-" * 48)

def tips():
    tip = random.randint(0, 9)
    sprint(f"\nThe customer tipped ${tip}")
    return tip   
    
def cookfile():
    cookgame.game()

def cashierfile():
    sprint ('Your shift has begun! \n')
    cashiergame.game ()
    

def select ():
    sprint ('Choose your character! \n\n1. Jonathan Chan (cashier) \n\n2. Yi Cheng (cook)\n\n3. Back\n')
    game = input ('Enter a response: ')
    if game == '2':
        print ("-" * 48)
        cookfile ()
    if game == '1':
        print ("-" * 48)
        cashierfile()
    if game == '3':
        print ("-" * 48)
        start ()
def start ():
    titlescreen()
    sprint ('1. Play\n\n2. Credits\n\n3. Quit\n')
    answer = input ('Enter a response: ') 
    if answer == '1':
        print ("-" * 48)
        sprint ('Do you want to play?\n \n'"1. Yes, let's go! \n\n2. No, this game sucks.\n")
        answer = input ('Enter a response: ')
        
        if answer == '1':
            print ("-" * 48)
            select ()
        else:
            print ("-" * 48)
            start ()
    if answer == '2':
        print ("-" * 48)
        sprint ('                City Pizza™                    \n')
        sprint ('A Pizza Place Sim by Yi Cheng and Jonathan Chan\n')
        sprint ('                  Credits                      \n')
        sprint ('Producer:                              Yi Cheng\n')
        sprint ('Director:                              Yi Cheng\n')
        sprint ('Lead Gameplay Designer:                Yi Cheng\n')
        sprint ('Design and Scripting:                  Yi Cheng\n')
        sprint ('Emotional Support:                     Jonathan Chan')
        sprint ("-" * 48)
        sprint ('1. Main Menu\n\n2. Quit Game\n')
        choice = input ('Enter a response: ')
        if choice == '1':
            print ("-" * 48)
            start ()
        else: 
            print ("-" * 48)
            sprint ('Thank you for playing City Pizza™!\n')
            sprint ('Shutting down...\n')
            time.sleep(3)
            sprint ('Bye bye!')
    else: 
        print ("-" * 48)
        sprint ('Thank you for playing City Pizza™!\n')
        sprint ('Shutting down...\n')
        time.sleep(3)
        sprint ('Bye bye!')
        
        