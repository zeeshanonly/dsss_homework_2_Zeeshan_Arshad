import random

def random_integer_generator(min_lim: int, max_lim: int) -> int:
    """
    Generate a random integer between specified limits.

    Args:
        min_lim (int): Minimum possible random number.
        max_lim (int): Maximum possible random number.

    Returns:
        int: Random number within the specified range.

    Note:
        Before generating the random number, this function typecasts inputs to integers as a precaution.

    Examples:
        >>> random_integer_generator(1, 10)
        6
        >>> random_integer_generator(3, 6.5)
        4
    """
    # Ensure limits are integers
    min_lim, max_lim = int(min_lim), int(max_lim)
    return random.randint(min_lim, max_lim)


def operator_selector() -> str:
    """
    Randomly select a mathematical operator (+, -, *).

    Returns:
        str: A randomly chosen operator, either '+', '-', or '*'.

    Examples:
        >>> operator_selector()
        '+'
    """
    return random.choice(['+', '-', '*'])


def calculator(num1: int, num2: int, operator: str) -> (str, int):
    """
    Apply a mathematical operator to two numbers and return the problem and result.

    Args:
        num1 (int): First operand.
        num2 (int): Second operand.
        operator (str): Mathematical operator ('+', '-', '*').

    Returns:
        tuple: A tuple containing:
            - problem (str): The problem statement as a string.
            - answer (int): The result of the mathematical operation.

    Examples:
        >>> calculator(1, 10, '+')
        ('1 + 10', 11)
    """
    # Formulate the problem statement
    problem = f"{num1} {operator} {num2}"

    # Perform the calculation based on the operator
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2

    return problem, answer


def math_quiz():
    """
    Run a math quiz game with three rounds where the player answers arithmetic problems.

    Description:
        In each round, a random math problem is generated and presented to the player. The player
        gains a point for each correct answer, and the final score is displayed at the end.

    Returns:
        None
    """
    score = 0  # Initialize player score
    total_questions = 3  # Total rounds in the quiz

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems and need to provide the correct answers.")

    # Main quiz loop
    for _ in range(total_questions):
        # Generate problem parameters
        num1 = random_integer_generator(1, 10)
        num2 = random_integer_generator(1, 5)  # Avoid float values
        operator = operator_selector()

        # Get the problem and solution
        problem, answer = calculator(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        # Obtain and validate the player's answer
        PROBLEM, ANSWER = calculator(num1, num2, operator)
        print(f"\nQuestion: {PROBLEM}")
        user_answer = input("Your answer: ")
        user_answer = int(user_answer)

        # Check if the player's answer is correct
        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    # Print final score
    print(f"\nGame over! Your score is: {score}/{total_questions}")


if __name__ == "__main__":
    math_quiz()
