from artifactClass import artifact
from criteriaClass import criteriaItem
from questionMathClass import questionMathsBasic

import random

#Criteria creation
correctnessCriteria = criteriaItem("Correctness","Wether the question has been answered correctly",1,True)
creativeFlaireCriteria = criteriaItem("Creative Flaire","How artisticly the piece of work has been compeleted",10)
#print(correctnessCriteria.title)

#test = artifact("X + 1 = ?, where X = 2","2","Manjit Sahota",[correctnessCriteria,creativeFlaireCriteria],[0,8])
#test.display()
#test.mark()

#Load random names into lists
q = open('./data/nameLast.txt', 'r')
nameLast = q.readlines()
q = open('./data/nameFirst.txt', 'r')
nameFirst = q.readlines()




for i in range(1,30):
    #The actual answer the question
    questionToMarkAnswer = random.randint(1,100)
    #Create a questino with an aswer created above
    questionToMark = questionMathsBasic(questionToMarkAnswer,random.randint(1,100))
    #Set the markee's answer to something closeish to the actual
    markeeAnswer = questionToMark.markeeAnswer()
    #Create an artifact, with the question created and a random name
    artifactToMark = artifact(questionToMark.display(),markeeAnswer,nameFirst[random.randint(1,len(nameFirst)-1)] + " " + nameLast[random.randint(1,len(nameLast)-1)],[correctnessCriteria],[questionToMark.answerMark(markeeAnswer)])
    #Display this artifact
    artifactToMark.display()
    #Let the player mark.
    artifactToMark.mark()
