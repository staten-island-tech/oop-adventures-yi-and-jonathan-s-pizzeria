import uuid

print ("The Pizza Place")

def game ():
    game = input ('Do you want to play as a cook or cashier: ')
    if game == 'cook':
        print ('sajoifj')
    elif game == 'cashier':
        print ('sdiofjod')

def start ():
    start = input ('Do you want to play? Y/N: ')
    if start == 'Y':
            print ('Its time to cook')
    elif start == 'N' or 'n':
         print ('Maybe next time :(')


start ()

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

