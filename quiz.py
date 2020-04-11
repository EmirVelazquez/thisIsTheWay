# Importing the Question class from questionsFile
from questionsFile import Question

# Questions and answers for quis to use with question class
questions_prompt = [
    "What's the third planet from the sun?\n[A] Mars\n[B] Earth\n[C] Venus\n\n",
    "What's the oldest programming language?\n[A] Fortran\n[B] Cobol\n[C] Basic\n\n",
    "What's the first video game ever made?\n[A] Asteroids\n[B] Tetris\n[C] Pong\n\n",
]
# Creating question and answer objects here
questions = [
    Question(questions_prompt[0], "b"),
    Question(questions_prompt[1], "a"),
    Question(questions_prompt[2], "c"),
]

# function to handle running the quiz, storing number of correct answers
# looping through all of the questions, printing result in terminal
def run_quiz(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You scored " + str(score) + "/" + str(len(questions)) + " correct.")


# Initializing the quiz here
run_quiz(questions)
