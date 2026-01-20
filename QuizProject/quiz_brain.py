
class QuizBrain:
    def __init__(self, qlist):
        self.qnumber = 0
        self.qlist = qlist
        self.score = 0
    
    def still_has_questions(self):
        return self.qnumber < len(self.qlist)

    def nextQuestion(self):
        currQuestion = self.qlist[self.qnumber]
        self.qnumber += 1
        answer = input(f"Q.{self.qnumber}: {currQuestion.text}. (True/False): ")   
        self.check_answer(currQuestion.answer, answer)

    def check_answer(self,correct_answer, user_answer):

        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")
        
        print(f"Correct Answer: {correct_answer}")
        print(f"Score: {self.score}/{self.qnumber}\n")
