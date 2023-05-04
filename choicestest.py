def questions ():

    question1 = 1
    
    question1 = {
        "question": 'Customer: "Hello!"',
        "choices": ['1. "Hello! What would you like to order?"','2. "Leave the store now!"', '3. "Hey! What would you like to try today?"'],
        "answer": "2"
    }

    # Print the question and answer choices
    print(question1["question"])
    for choice in question1["choices"]:
        print(choice)

    # Ask the user to select an answer
    user_answer = input("What will your response be? ")

    # Check if the answer is correct
    if user_answer == question1["answer"]:
        print('Customer: "Rude! I will be taking my business elsewhere!"')
    else:
        print('Customer: "I would like a pepperoni pizza!"')

questions ()