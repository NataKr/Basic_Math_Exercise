import random
import operator
ops = {"+": operator.add, "-": operator.sub, "*": operator.mul, ":": operator.div}

def generate_problem():
    operators = ["-", "+", "*", ":"]
    correct_answer = 0
    number1 = random.randint(-10, 10)
    number2 = random.randint(-10, 10)
    selected_operator = random.choice(operators)

    while True:
        try:
            operator.div(number1, number2)
            break
        except ZeroDivisionError:
            # print "division by zero not allowed"
            # print number2
            number1 = random.randint(-10, 10)
            number2 = random.randint(-10, 10)

    print "Solve the following problem {0} {1} {2}".format(number1, selected_operator, number2)
    correct_answer = ops[selected_operator](number1, number2)
    if selected_operator == ":":
        # print selected_operator
        correct_answer = float(number1) / number2
        # print correct_answer
        if number1 % number2 == 0:
            correct_answer = int(number1 / number2)
            # print "i am in if"
        else:
            correct_answer = round(correct_answer, 2)
            # print "i am in else"
            # print correct_answer
    problem = str(number1) + " " + selected_operator + " " + str(number2) + "=" + str(correct_answer)
    return problem, correct_answer

def check(user_answer, correct_answer, problem, list_correct_answers, list_incorrect_answers):
    if user_answer == correct_answer:
        print "Congratulations you have answered correctly"
        list_correct_answers.append(problem)
        correct_answers_number = len(list_correct_answers)
        incorrect_answers_number = len(list_incorrect_answers)
        print "The number of correct answers is {}".format(correct_answers_number)
        print "The number of incorrect answers is {}".format(incorrect_answers_number)
    else:
        print "Your answer is wrong"
        list_incorrect_answers.append(problem)
        correct_answers_number = len(list_correct_answers)
        incorrect_answers_number = len(list_incorrect_answers)
        print "The number of correct answers is {}".format(correct_answers_number)
        print "The number of incorrect answers is {}".format(incorrect_answers_number)
    return list_correct_answers, list_incorrect_answers

def get_indicator_to_continue():
    return raw_input("Do you want to solve the next math problem? ").lower()


def print_exercise_report(list_correct_answers, list_incorrect_answers):
    answers_string = ""
    print "Problems solved correctly {}".format(len(list_correct_answers))
    for answer in list_correct_answers:
        answers_string += answer + ", "
    print answers_string

    print "Problems solved incorrectly {}".format(len(list_incorrect_answers))
    answers_string = ""
    for answer in list_incorrect_answers:
        answers_string += answer + ", "
    print answers_string
    print "Your correctness rate is: {}%".format(
        len(list_correct_answers) * 100 / (len(list_incorrect_answers) + len(list_correct_answers)))


def start_exercise():
    flag = True
    list_correct_answers = []
    list_incorrect_answers = []

    while flag:
        list_of_answers = ["yes", "no", "Yes", "No", "y", "n", "Y", "N", ""]
        list_of_yes_answers = ["yes", "y"]
        list_of_no_answers = ["no", "n", ""]

        flag2 = True
        indicator_to_continue = get_indicator_to_continue()
        # indicator_to_continue=raw_input("Do you want to solve the next math problem? ").lower()
        while flag2:
            if indicator_to_continue not in list_of_answers:
                indicator_to_continue = get_indicator_to_continue()  # adding
            else:
                flag2 = False

        if indicator_to_continue.lower() in list_of_yes_answers:
            problem, correct_answer = generate_problem()
            user_answer = raw_input("Enter your answer here: ")
            while True:
                try:
                    int(user_answer)
                    user_answer = int(user_answer)
                    break
                except:
                    try:
                        float(user_answer)
                        user_answer = float(user_answer)
                        break
                    except ValueError:
                        print "Oops!  That was no valid number.  Try again..."
                        user_answer = raw_input("Enter your answer here: ")

            list_correct_answers, list_incorrect_answers=check(user_answer, correct_answer, problem, list_correct_answers, list_incorrect_answers)

        elif indicator_to_continue.lower() in list_of_no_answers:
            if len(list_incorrect_answers) + len(list_correct_answers) == 0:
                print "You have provided no answers"
                flag = False
            else:
                print "Below is exercise report:"
                print_exercise_report(list_correct_answers, list_incorrect_answers)
                flag = False

start_exercise()