import random

questions = ["Do you like me?", "What is your name?"]
answers = ["You know it your self.", "You don`t need to know it."]

random.shuffle(questions)
random.shuffle(answers)
for i in range(2):
    print("Mom:" + questions[i])
    print("Me:" + answers[i])
