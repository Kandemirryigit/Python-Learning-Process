

from question_model import *   # From question_model import everything to the main.py 
from data import *             # From data import everything to the main.py
from quiz_brain import *       # From quiz_brain import everything to the main.py



question_bank=[]
for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    new_question=Question(q_text=question_text,q_answer=question_answer)
    question_bank.append(new_question)


quiz=QuizBrain(question_bank)


while quiz.still_has_question():
    quiz.next_question()


print("you've completed the quiz")
print(f"your final score was: {quiz.score}/{quiz.question_number} ")