import random


def number_limit(min, max):
    """
    Selects random integer and return a number between this range
    """
    return random.randint(min, max)


def function_ops():
    return random.choice(['+', '-', '*'])


def function_equations(n1, n2, o):
    finalResult=0
    solve = f"{n1} {o} {n2}"
    if o == '+': finalResult = n1 + n2
    elif o == '-': finalResult = n1 - n2
    else: finalResult = n1 * n2
    return solve, finalResult

def math_quiz_Ex2():
    points = 0
    totalQues = 5

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for i in range(totalQues):
        n1 = number_limit(1, 10); n2 = number_limit(1, 6); o = function_ops()

        PROBLEM, ANSWER = function_equations(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            points += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {points}/{totalQues}")

if __name__ == "__main__":
    math_quiz_Ex2()
