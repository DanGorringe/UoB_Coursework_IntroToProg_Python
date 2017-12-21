#

#Import my own classes
from artifactClass import artifact
from criteriaClass import criteriaItem
from questionMathClass import questionMathsBasic

#Import other modules
import random
from tkinter import *
from tkinter import ttk

#Load random names into lists ***seek help***
q = open('./data/nameLast.txt', 'r')
nameLast = [word.rstrip('\n') for word in q]

q = open('./data/nameFirst.txt', 'r')
nameFirst = [word.rstrip('\n') for word in q]

#Criteria creation
correctnessCriteria = criteriaItem("Correctness","Wether the question has been answered correctly",1,True)
creativeFlaireCriteria = criteriaItem("Creative Flaire","How artisticly the piece of work has been compeleted",10)

#Create main screen
root = Tk()
w = Label(root,text="Welcome to Marking Simulator 2018").pack()

#Create test artifactToMark
questionToMarkAnswer = random.randint(1,100)
questionToMark = questionMathsBasic(questionToMarkAnswer,random.randint(1,100))
markeeAnswer = questionToMark.markeeAnswer()
artifactToMark = artifact(questionToMark.display(),markeeAnswer,(nameFirst[random.randint(1,len(nameFirst)-1)] + " " + nameLast[random.randint(1,len(nameLast)-1)]),[correctnessCriteria],[questionToMark.answerMark(markeeAnswer)]).display()
#Create artifact presentation function, move this to the class??
def presentArtifact(artifact):
    artifactWindow = Tk()
    #Print answer and author
    w = Label(artifactWindow,text="").pack()
    w = Label(artifactWindow,text=artifact.answer).pack()
    w = Label(artifactWindow,text="By " + artifact.author).pack()
    #Add buttons to mark with
    for criteria in artifact.criteriaList:
        marks = StringVar()
        w = Label(artifactWindow,text="Marks for " + str(criteria.title)).pack()
        s = Spinbox(artifactWindow,from_=0,to=criteria.checkMax(),textvariable=marks).pack()
    for i in range(len(artifact.criteriaList)):
        marks[i] = StringVar()
        w = Label(artifactWindow,text="Marks for " + str(artifact.criteriaList[i].title)).pack()
        s = Spinbox(artifactWindow,from_=0,to=artifact.criteriaList[i].checkMax(),textvariable=marks[i]).pack()
    w = Button(artifactWindow,text="Mark",command=artifact.mark(marks)).pack()
    artifactWindow.mainloop()


#presentArtifact(artifactToMark)

#print(artifactToMark.author)

root.mainloop()

# Dan Gorringe December 2017
