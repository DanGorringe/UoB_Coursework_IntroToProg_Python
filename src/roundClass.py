from tkinter import *
from tkinter import ttk

from functools import partial

import random

from PIL import Image, ImageTk

from artifactClass import artifact


#Load random names into lists
q = open('./data/nameLast.txt', 'r')
nameLast = [word.rstrip('\n') for word in q]

q = open('./data/nameFirst.txt', 'r')
nameFirst = [word.rstrip('\n') for word in q]

q = open('./data/jobTitle.txt', 'r')
jobTitle = [word.rstrip('\n') for word in q]

q = open('./data/relation.txt', 'r')
relation = [word.rstrip('\n') for word in q]

class roundInfo():

    def __init__(self,question,criteriaList,artifactList=[]):
        self.question = question
        self.criteriaList = criteriaList
        self.artifactList = artifactList
        self.markedArtifacts = {}
        self.spinboxValues = {}
        self.artifactWindowDic = {}
        self.progressVar = IntVar(0)
        self.progressRef = 0
        self.progressNamesLabels = {}
        self.stepLength = 0
        self.answerPhoto = {}
        self.complete = False
        self.score = 0

    # Find the assignment of the round
    def question(self):
        return(self.question.question())

    # Start 'playing'
    def play(self):
        self.complete = False
        self.playQuestionDisplay()
        self.playArtifactDisplay()
        self.playProgressDisplay()

    # Display the progress window
    def playProgressDisplay(self):
        self.progressWindow = Tk()
        self.progressWindow.title("Progress")
        #Could not get a timer to work
        self.timerLabel = Label(self.progressWindow,text="PROGRESS",font=("Helvetica",100))
        self.timerLabel.pack()
        self.progressRef = ttk.Progressbar(self.progressWindow,length=1000)
        self.progressRef.pack()

    # Display the quesiton window
    def playQuestionDisplay(self):
        self.questionWindow = Tk()
        self.questionWindow.title("Assignment")
        w = Label(self.questionWindow,text="The task is:").pack()
        w = Label(self.questionWindow,text=self.question.question()).pack()
        w = Label(self.questionWindow,text="To be marked on the following criteria:").pack()
        for i in range(len(self.criteriaList)):
            questionText = str(self.criteriaList[i]) + " out of a maximum of " + str(self.criteriaList[i].checkMax()) + ", and this is critical"
            if self.criteriaList[i].checkCritical() == False:
                questionText = str(self.criteriaList[i]) + " out of a maximum of " + str(self.criteriaList[i].checkMax())
            w = Label(self.questionWindow,text=questionText).pack()

    # Create a window for every artifact to be marked
    def playArtifactDisplay(self):
        for artifact in self.artifactList:
            self.spinboxValues[artifact] = []
            #Create a list of artifactWindows?
            artifactWindow = Toplevel()
            artifactWindow.title(artifact.author+"'s work")
            #Print answer and author
            w = Label(artifactWindow,text="").pack()

            self.answerPhoto[artifact] = PhotoImage(file="./data/answers/"+str(artifact.answer)+".gif",master=artifactWindow)
            Label(artifactWindow, image=self.answerPhoto[artifact]).pack()
            #w = Label(artifactWindow,image=photo).pack()

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

    # Mark the artifact given
    def playArtifactMark(self,artifact):

        self.artifactWindowDic[artifact].update()
        returningInfo = [True,0,[]]
        for i in range(len(self.criteriaList)):
            #If critical criteria failed then return 1 as false
            if self.criteriaList[i].checkCritical() == True:
                if int(self.spinboxValues[artifact][i].get()) !=  artifact.criteriaValues[i]:
                    returningInfo[0] = False
                    returningInfo[2].append(False)
                else:
                    returningInfo[2].append(1)
                    # Default score of 10 for a currect answer
                    returningInfo[1] += 10
            #Else the criteria is not crucial, return 'score'
            else:
                returningInfo[2].append(self.spinboxValues[artifact][i].get())
                returningInfo[1] += int(self.criteriaList[i].checkMax()) - int(((int(artifact.criteriaValues[i]) - int(self.spinboxValues[artifact][i].get()))**2)/(self.criteriaList[i].checkMax()/3))
        # Add dictionary entry for marked work
        self.markedArtifacts.update({artifact:returningInfo})
        # Remove artifact from list of artifacts to be marked
        self.artifactList.remove(artifact)
        # Delete the window
        self.artifactWindowDic[artifact].destroy()
        # Increment progress bar
        self.progressRef.step(self.stepLength)
        # If this was the last piece to be marked enter finishing funciton
        if self.artifactList == []:
            self.finishedMarking()

    # Create an amount of artifacts that satisfy the question and criteria
    def artifactCreation(self,quantity):
        self.stepLength = 99/quantity
        for i in range(quantity):
            #get the markee answer
            markeeAnswer = self.question.markeeAnswer()
            # Create criteriavalues suitable for their criteria
            myCriteriaValues = []
            for criteria in self.criteriaList:
                if criteria.checkCritical() == True:
                    myCriteriaValues.append(self.question.answerMark(markeeAnswer))
                else:
                    myCriteriaValues.append(random.randint(0,self.criteriaList[1].checkMax()))
            # Creating the artifact
            self.artifactList.append(artifact(self.question,markeeAnswer,(nameFirst[random.randint(1,len(nameFirst)-1)] + " " + nameLast[random.randint(1,len(nameLast)-1)]),self.criteriaList,myCriteriaValues))
            # Creating the corresponding image
            self.question.createImage(self.artifactList[i])

    def artifactScoreAppend(self,returningInfo):
        score += returningInfo[1]
        print(str(score))

    #Breakdown of how well you marked

    def finishedMarking(self):
        # Set inital score
        self.score = 0
        # Set round to complete
        self.complete = True
        # Sum score
        for artifact in self.markedArtifacts:
            self.score += self.markedArtifacts[artifact][1]
        # delete windows
        self.questionWindow.destroy()
        self.progressWindow.destroy()
        # Create debriefing window
        completionWindow = Tk()
        completionWindow.title("Debrief")
        # Passes as default
        passed = True
        for artifact in self.markedArtifacts:
            # If the first artifact incorrectly marked set passed to Flse, and accompany with appropriate label
            if self.markedArtifacts[artifact][0] == False:
                if passed == True:
                    passed = False
                    Label(completionWindow,text="You Failed",font=("Helvetica",100),fg='red').pack()
                    Label(completionWindow,text="Unfortunately Academia is a cut-throat world, it seem's you actually incorrectly marked a "+ jobTitle[random.randint(0,len(jobTitle)-1)] +"'s "+relation[random.randint(0,len(jobTitle)-1)]+"'s work wrong. This lead to them getting involved with the faculty, remoking thousands worth of funding. Hence your line manager has decided to dock you 200 score!",wraplength=1000).pack()
                    self.score -= 200
                Label(completionWindow,text="")
                for i in range(len(self.criteriaList)):
                    text2Print = ""
                    if self.markedArtifacts[artifact][2][i] == False:
                        text2Print = "You incorrectly marked " + str(artifact.author) + " on " + str(self.criteriaList[i])
                        Label(completionWindow,text=text2Print).pack()
        if passed == True:
            Label(completionWindow,text="You didn't Fail",font=("Helvetica",100)).pack()
            Label(completionWindow,text="Congratulations, you get to keep your job, marking pesky underling's work (Doesn't actually sound like a win does it?).",wraplength=1000).pack()
            Label(completionWindow,text="",wraplength=1000).pack()
            for artifact in self.markedArtifacts:
                text2Print = "You gained " + str(self.markedArtifacts[artifact][1]) + " marks, for how you scored " + str(artifact.author) + "'s work"
                Label(completionWindow,text=text2Print).pack()
        text2Print = "And after all your ardous marking you only obtained: "+str(self.score)+" marks"
        Label(completionWindow,text=text2Print,wraplength=1000).pack()
        Button(completionWindow,text="finish",command=lambda:completionWindow.destroy()).pack()

    def scoreReturn(self):
        if self.complete == True:
            return(self.score)
        else:
            return(False)



# Dan Gorringe January 2018
