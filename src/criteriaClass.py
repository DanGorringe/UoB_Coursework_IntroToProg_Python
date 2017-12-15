class criteriaItem():

    def __init__(self,title,description,maximumScoring=1,critical=False):
        #Name of the marking criteria
        self.title = title
        #A brief description of this critera, to be shown to the player
        self.description = description
        #The maximum marks that can be awarded
        self.maximumScoring = maximumScoring
        #Wether the player has to guess this correctly ()
        self.critical = critical

    def __str__(self):
        return("A criteria of " + str(self.title))

    def checkCritical(self):
        return(self.critical)

    def title(self):
        return(str(self.title))

    def description(self):
        return(str(self.description))

    def checkMax(self):
        return(self.maximumScoring)
