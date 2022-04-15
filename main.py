from data import question_data
from question_model import Question
from quiz_brain import quizbrain
question_bank=[]
for q in question_data:
    q_text=q["text"]
    q_ans=q["answer"]
    question=Question(q_text,q_ans)
    question_bank.append(question)
quiz=quizbrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You Have Finshed The Quiz")
print(f"Your Final Score Is :{quiz.score}/{quiz.question_number}")


