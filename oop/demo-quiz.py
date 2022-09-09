# Question

class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer==answer
# Quiz

class Quiz:
    def __init__(self, questions):
        self.questions=questions
        self.score=0
        self.questionIndex=0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        questions = self.getQuestion()
        print(f'Soru {self.questionIndex+1}: {question.text}')

        for q in question.choices:
            print('-'+q)
        answer = input('cevap: ')
        self.guess(answer)
        self.loadQuestion()

    def guess(self,answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score+=1
        self.questionIndex+=1

    def loadQuestion(self):
        if len(self.questions)==self.questionIndex:
            self.showScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print('Score: ',self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex+1

        if questionNumber>totalQuestion:
            print('Quiz bitti.')
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(100,'*'))


q1 = Question('En iyi progrsmlsms dili nedir?',['C#','python','javascript','java'],'python')
q2 = Question('En populer progrsmlsms dili nedir?',['C#','python','java','javascript'],'python')
q3 = Question('En cok kazandiran progrsmlsms dili nedir?',['C#','java','python','javascript'],'python')
q4 = Question('En cok sevilen progrsmlsms dili nedir?',['C#','java','python','javascript'],'python')
q5 = Question('En cok mutlu eden progrsmlsms dili nedir?',['C#','java','python','javascript'],'python')
questions = [q1,q2,q3,q4,q5]

quiz = Quiz(questions)
question = quiz.getQuestion()
print(question.text)
quiz.loadQuestion()



