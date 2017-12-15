class artifact():

    def __init__(self,question,answer,author,criteriaList,criteriaValues,plagaristBool=False,plagiristAccomplice="none"):
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
        return(str(self.author))

    def display(self):
        print("The Question: " + str(self.question))
        print("and is to be marked on:")
        for i in self.criteriaList:
            print(str(i) + " out of an available " + str(i.checkMax()) + " points")
        print("The student submitting is: " + str(self.author))
        print("Their answer is: " + str(self.answer))

    #Mark takes a list of player guesses which correspond to the list of criteria.
    def mark(self):
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
