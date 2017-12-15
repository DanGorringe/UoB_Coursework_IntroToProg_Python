import random

class questionMathsBasic():
    def __init__(self,answer,extra):
        self.answer = answer
        self.extra = extra
    def display(self):
        return("X + " + str(self.extra) + " = " + str(self.extra+self.answer) + ", what is X?")
    def answer(self):
        return(answer)
    def markeeAnswer(self):
        return(int(random.gauss(self.answer,1)))
    def answerMark(self,markeeAnswer):
        if self.answer == markeeAnswer:
            return(1)
        else:
            return(0)

class questionMathsSquare():
    def __init__(self,answer):
        self.answer = answer
    def display(self):
        return("X\u00B2 + " + str(-(int(answer[0]) + int(answer[1]))) + "x + "+ str(int(answer[0])*int(answer[1])) + " = 0, what values can X have?")
    def answer(self):
        return(answer)
    def markeeAnswer(self):
        return([int(random.gauss(self.answer[0],1)),int(random.gauss(self.answer[1],1))])
    def answerMark(self,markeeAnswer):
        if self.answer == markeeAnswer:
            return(1)
        else:
            return(0)

# Dan Gorringe December 2017
