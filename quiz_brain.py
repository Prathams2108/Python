class quizbrain:
    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0
    def still_has_questions(self):
        l=len(self.question_list)
        if self.question_number>l:
            return False
        else:
            return True
    def next_question(self):
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        ans=input(f"Q.{self.question_number} {current_question.q} Enter TRUE\FALSE").lower()
        self.check_answer(ans,current_question.ans)
    def check_answer(self,u_ans,c_ans):
        if u_ans.lower() == c_ans.lower():
            print("✔️You Got It Right!")
            self.score+=1
            print(f"Current Score: {self.score}/{self.question_number}")
        else:
            print("That is the wrong answer ❌")
            print(f"Current Score: {self.score}/{self.question_number}")
            print(f"The Correct answer is: {c_ans}")

