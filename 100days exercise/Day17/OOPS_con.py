import random

from docutils.parsers.rst.directives.misc import Class
from pygments.lexers import q

questions = [
    {"question": "The Earth revolves around the Sun.", "answer": True},
    {"question": "Sound travels faster than light.", "answer": False},
    {"question": "The capital of France is Paris.", "answer": True},
    {"question": "Bats are blind.", "answer": False},
    {"question": "Water boils at 100 degrees Celsius.", "answer": True},
    {"question": "There are 30 days in February.", "answer": False},
    {"question": "Humans have four lungs.", "answer": False},
    {"question": "The Great Wall of China is visible from space.", "answer": False},
    {"question": "Light is both a particle and a wave.", "answer": True},
    {"question": "Mount Everest is the tallest mountain on Earth.", "answer": True}
]
class Question:
    def __init__(self):
        q=random.choice(questions)
        self.question = q['question']
        self.answer = q['answer']
    def check(self,user_input,answer):
        global score, attemt, flag
        if answer == user_input:
            print("Correct")
            score+=1
        else:
            print("Incorrect")
            flag=True
        attemt += 1