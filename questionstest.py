class Question:
    def __init__ (self, prompt, answer):
        self.prompt  (prompt)
        self.answer (answer)

question_prompts = [
    'How would you like to respond? \n  1. "Hello! My name is Jonathan. What would you like to order?" 2. "Leave the store now!" 3. "Hey! What would you like to try today?"'


]
    
questions = [
    Question(question_prompts[0], "2 "),
    Question(question_prompts[1], "1 "),
    Question(question_prompts[2], "3 ")
]

def run_test(questions): 
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score+= 1 
    print ("You've got " + str(score) + '/' + str(len(questions)) + " correct")
       

run_test (questions)
