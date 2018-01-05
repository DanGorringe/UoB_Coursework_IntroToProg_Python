#

#Import my own classes
from artifactClass import artifact
from criteriaClass import criteriaItem
from questionMathClass import questionMathsBasic
from roundClass import roundInfo
from questionSunClass import questionSun

#Import other modules
import random
from tkinter import *
from tkinter import ttk

#Criteria creation
correctnessCriteria = criteriaItem("Correctness","Wether the question has been answered correctly",1,True)
creativeFlaireCriteria = criteriaItem("Creative Flaire","How artisticly the piece of work has been compeleted",10)

complexityCriteria = criteriaItem("Complexity","How much detail their is",10)
onTopicCritera = criteriaItem("On Topic","How well does it stick to the brief",15)

#Create basic quesiton
def createBasicMathsQuestion():
    return(questionMathsBasic(random.randint(1,100),random.randint(1,100)))

#Create main screen
root = Tk()
root.title("Welcome")
w = Label(root,text="Welcome to Marking Simulator 2018").pack()

class menuClass():
    def __init__(self):
        self.menuButton = []
        self.score = 0
        self.scoreValue = 0
        self.menuWindow = 0
    def display(self):
        self.menuWindow = Tk()
        self.menuWindow.title("Menu")
        w = Label(self.menuWindow,text="Menu").pack()
        w = Label(self.menuWindow,text="Your current score is: "+str(self.score))
        self.score = w
        self.score.pack()
        self.displayButtons()

    def displayButtons(self):
        w = Button(self.menuWindow,text="Sun",command=lambda:self.playSun())
        self.menuButton.append(w)
        w = Button(self.menuWindow,text="Maths",command=lambda:self.playMath())
        self.menuButton.append(w)
        for i in range(len(self.menuButton)):
            self.menuButton[i].pack()

    def playSun(self):
        testQuestion = questionSun()
        self.testRound = roundInfo(testQuestion,[complexityCriteria,onTopicCritera])
        self.testRound.artifactCreation(random.randint(2,10))
        self.testRound.play()
        self.playingState()
    def playMath(self):
        testQuestion = createBasicMathsQuestion()
        self.testRound = roundInfo(testQuestion,[correctnessCriteria])
        self.testRound.artifactCreation(random.randint(2,10))
        self.testRound.play()
        self.playingState()

    def playingState(self):
        for button in self.menuButton:
            button.pack_forget()
        self.warning = Label(self.menuWindow,text="Come back once you've finished marking")
        self.warning.pack()
        self.continueButton = Button(self.menuWindow,text="Continue",command=self.updateScore)
        self.continueButton.pack()

    def updateScore(self):
        self.scoreValue += self.testRound.scoreReturn()
        self.score.config(text="Your current score is: "+str(self.scoreValue))
        self.continueButton.pack_forget()
        self.warning.pack_forget()
        for button in self.menuButton:
            button.pack()


m = menuClass()
m.display()

root.mainloop()

# Dan Gorringe January 2018
