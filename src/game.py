#

#Import my own classes
from artifactClass import artifact
from criteriaClass import criteriaItem
from questionMathClass import questionMathsBasic
from roundClass import roundInfo

#Import other modules
import random
from tkinter import *
from tkinter import ttk

#Criteria creation
correctnessCriteria = criteriaItem("Correctness","Wether the question has been answered correctly",1,True)
creativeFlaireCriteria = criteriaItem("Creative Flaire","How artisticly the piece of work has been compeleted",10)

#Create basic quesiton
def createBasicMathsQuestion():
    return(questionMathsBasic(random.randint(1,100),random.randint(1,100)))

#Create main screen
root = Tk()
w = Label(root,text="Welcome to Marking Simulator 2018").pack()

testQuestion = createBasicMathsQuestion()
testRound = roundInfo(testQuestion,[correctnessCriteria,creativeFlaireCriteria])
testRound.artifactCreation(2)
testRound.play()


#print(roundDic)

#artifactWindow.mainloop()
root.mainloop()

# Dan Gorringe December 2017
