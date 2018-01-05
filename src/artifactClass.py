from tkinter import *
from tkinter import ttk

class artifact():

    global roundDic

    def __init__(self,question,answer,author,criteriaList,criteriaValues,plagaristBool=False,plagiristAccomplice="none",markSpinboxs=[]):
        #The question
        self.question = question
        #The answer
        self.answer = answer
        #The 'author' of the artifact, to have their name at the bottom
        self.author = author
        #The criteria the artifact will be marked against
        self.criteriaList = criteriaList
        #The ideal scores to be allocated
        self.criteriaValues = criteriaValues
        #If it is plagarised
        self.plagaristBool = plagaristBool
        #Who else plagarised
        self.plagiristAccomplice = plagiristAccomplice
        #List of marks spinboxs
        self.markSpinboxs = markSpinboxs

    def plagirismCheck(self,plagaristBool,plagiristAccomplice):
        if self.plagaristBool == False:
            return(False)
        else:
            return(self.plagiristAccomplice)
    def question(self):
        return(str(self.question))
    def answer(self):
        return(self.answer)
    def author(self):
        return(self.author)

    def display_old(self):
        print("The Question: " + str(self.question))
        print("and is to be marked on:")
        for i in self.criteriaList:
            print(str(i) + " out of an available " + str(i.checkMax()) + " points")
        print("The student submitting is: " + str(self.author))
        print("Their answer is: " + str(self.answer))
    #Move displaying to round class
    def display(self):
        artifactWindow = Tk()
        #Print answer and author
        w = Label(artifactWindow,text="").pack()
        w = Label(artifactWindow,text=self.answer).pack()
        w = Label(artifactWindow,text="By " + self.author).pack()
        #Add buttons to mark with
        #for criteria in self.criteriaList:
        #    marks = StringVar()
        #    w = Label(artifactWindow,text="Marks for " + str(criteria.title)).pack()
        #    s = Spinbox(artifactWindow,from_=0,to=criteria.checkMax(),textvariable=marks).pack()
        for i in range(len(self.criteriaList)):
            individualMark = IntVar()
            w = Label(artifactWindow,text="Marks for " + str(self.criteriaList[i].title)).pack()
            s = Spinbox(artifactWindow,from_=0,to=self.criteriaList[i].checkMax(),textvariable=individualMark)
            self.markSpinboxs.append(s)
            s.pack()
        w = Button(artifactWindow,text="Mark",command=self.mark).pack()
        #artifactWindow.mainloop()

    #Mark takes a list of player guesses which correspond to the list of criteria.
    def mark_manual(self):
        for i in range(len(self.criteriaValues)):
            playerAnswer = int(input("For " + str(self.criteriaList[i]) + " how many points out of an available " + str(self.criteriaList[i].checkMax()) + " are you awarding? "))
            #Check wether the criteria is critical and if player fails then fail them.
            if self.criteriaList[i].checkCritical() == True:
                print("Criteria is critical")
                if playerAnswer !=  self.criteriaValues[i]:
                    print("failed")
                if playerAnswer ==  self.criteriaValues[i]:
                    print("passed")
            #Else the criteria is not crucial, return 'score'
            else:
                #Have the 'score' proportional to the quasi chi-chi (square of the difference
                # Score = max - (actual - playerAnswer)^2
                markingPoints = self.criteriaList[i].checkMax() - (self.criteriaValues[i] - playerAnswer)**2
                print("You scored " + str(markingPoints) + " for how you marked " + str(self.criteriaList[i]) + " on " + str(self.author) + "'s piece of work'")
                return(markingPoints)
    #Return marking info in the format [(true/false),score]. true if passed, false is failed
    #Move marking to round class
    def mark(self):
        returningInfo = [True,0,[]]
        for i in range(len(self.criteriaValues)):
            #If critical criteria failed then return 1 as false
            if self.criteriaList[i].checkCritical() == True:
                if int(self.markSpinboxs[i].get()) !=  self.criteriaValues[i]:
                    returningInfo[0] = False
                    returningInfo[2].append(0)
                else:
                    returningInfo[2].append(1)
            #Else the criteria is not crucial, return 'score'
            else:
                returningInfo[2].append(self.markSpinboxs[i].get())
                returningInfo[1] += int(self.criteriaList[i].checkMax()) - (int(self.criteriaValues[i]) - int(self.markSpinboxs[i].get()))**2
                #Have the 'score' proportional to the quasi chi-chi (square of the difference
                # Score = max - (actual - answer[i])^2
                #markingPoints = int(self.criteriaList[i].checkMax()) - (int(self.criteriaValues[i]) - int(self.markSpinboxs[i].get()))**2
                #print("You scored " + str(markingPoints) + " for how you marked " + str(self.criteriaList[i]) + " on " + str(self.author) + "'s piece of work'")
                #return(markingPoints)



# Dan Gorringe January 2018
