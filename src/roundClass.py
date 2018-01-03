from tkinter import *
from tkinter import ttk

from functools import partial

import random

from artifactClass import artifact
from criteriaClass import criteriaItem
from questionMathClass import questionMathsBasic

#Load random names into lists
q = open('./data/nameLast.txt', 'r')
nameLast = [word.rstrip('\n') for word in q]

q = open('./data/nameFirst.txt', 'r')
nameFirst = [word.rstrip('\n') for word in q]

class roundInfo():

    def __init__(self,question,criteriaList,artifactList=[],score=0,markedArtifacts={},spinboxValues={},artifactWindowDic={}):
        self.question = question
        self.criteriaList = criteriaList
        self.artifactList = artifactList
        self.markedArtifacts = markedArtifacts
        self.spinboxValues = spinboxValues
        self.artifactWindowDic = artifactWindowDic
        self.progressVar = IntVar(0)

    def question(self):
        return(self.question.question())

    def play(self):
        self.playQuestionDisplay()
        self.playArtifactDisplay()
        self.playProgressDisplay()




    def playQuestionDisplay(self):
        questionWindow = Tk()
        w = Label(questionWindow,text="The task is:").pack()
        w = Label(questionWindow,text=self.question.question()).pack()
        w = Label(questionWindow,text="To be marked on the following criteria:").pack()
        for i in range(len(self.criteriaList)):
            questionText = str(self.criteriaList[i]) + " out of a maximum of " + str(self.criteriaList[i].checkMax()) + ", and this is critical"
            if self.criteriaList[i].checkCritical() == False:
                questionText = str(self.criteriaList[i]) + " out of a maximum of " + str(self.criteriaList[i].checkMax())
            w = Label(questionWindow,text=questionText).pack()

    def playArtifactDisplay(self):
        for artifact in self.artifactList:
            self.spinboxValues[artifact] = []
            #Create a list of artifactWindows?
            artifactWindow = Tk()
            #Print answer and author
            w = Label(artifactWindow,text="").pack()
            w = Label(artifactWindow,text=artifact.answer).pack()
            w = Label(artifactWindow,text="By " + artifact.author).pack()
            #Add buttons to mark with
            for i in range(len(self.criteriaList)):
                individualMark = IntVar()
                w = Label(artifactWindow,text="Marks for " + str(self.criteriaList[i].title)).pack()
                s = Spinbox(artifactWindow,from_=0,to=self.criteriaList[i].checkMax(),textvariable=individualMark)
                self.spinboxValues[artifact].append(s)
                s.pack()
            w = Button(artifactWindow,text="Mark",command=partial(self.playArtifactMark,artifact)).pack()
            self.artifactWindowDic[artifact] = artifactWindow

    def playArtifactMark(self,artifact):
        self.artifactWindowDic[artifact].update()
        print(artifact.author)
        returningInfo = [True,0,[]]
        for i in range(len(self.criteriaList)):
            #If critical criteria failed then return 1 as false
            if self.criteriaList[i].checkCritical() == True:
                if int(self.spinboxValues[artifact][i].get()) !=  artifact.criteriaValues[i]:
                    returningInfo[0] = False
                    returningInfo[2].append(0)
                else:
                    returningInfo[2].append(1)
            #Else the criteria is not crucial, return 'score'
            else:
                returningInfo[2].append(self.spinboxValues[artifact][i].get())
                returningInfo[1] += int(self.criteriaList[i].checkMax()) - (int(artifact.criteriaValues[i]) - int(self.spinboxValues[artifact][i].get()))**2
                #Have the 'score' proportional to the quasi chi-chi (square of the difference
        self.markedArtifacts.update({artifact:returningInfo})
        self.artifactList.remove(artifact)
        print(returningInfo)
        #for i in range(len(self.criteriaList)):
        #    print(self.criteriaList[i])
        #    print(self.spinboxValues[artifact][i].get())
        self.artifactWindowDic[artifact].destroy()

    # Create an amount of artifacts that satisfy the question and criteria
    def artifactCreation(self,quantity):
        for i in range(quantity):
            #save the markee answer in a variable to use twice
            markeeAnswer = self.question.markeeAnswer()
            self.artifactList.append(artifact(self.question,markeeAnswer,(nameFirst[random.randint(1,len(nameFirst)-1)] + " " + nameLast[random.randint(1,len(nameLast)-1)]),self.criteriaList,[self.question.answerMark(markeeAnswer),random.randint(0,self.criteriaList[1].checkMax())]))

    def artifactScoreAppend(self,returningInfo):
        score += returningInfo[1]
        print(str(score))
