import random

def get_user_input():
    user_input = int(input("Enter your choice: "))
    while user_input > 5 or user_input <= 0:
        print("Invalid menu option.")
        user_input = int(input("Please try again: "))
    else:
        return user_input


def get_user_solution(problem):
    print("Enter your answer")
    print(problem, end="")
    result = int(input(" = "))
    return result


def check_solution(user_solution, solution, count):
    if user_solution == solution:
        count = count + 1
        print("Correct.")
        return count
    else:
        print("Incorrect.")
        return count
        
def addition (count):
    number_one = random.randrange(1, 21)
    number_two = random.randrange(1, 21)
    problem = str(number_one) + " + " + str(number_two)
    solution = number_one + number_two
    user_solution = get_user_solution(problem)
    count = check_solution(user_solution, solution, count)
    return count


