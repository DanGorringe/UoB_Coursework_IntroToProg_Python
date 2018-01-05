import random
from tkinter import *
from tkinter import ttk

from PIL import ImageFont, ImageDraw, Image

class questionMathsBasic():
    def __init__(self,answer,extra):
        self.answer = answer
        self.extra = extra
    def question(self):
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
    def display(self):
        questionWindow = Tk()
        w = Label(questionWindow,text=self.question()).pack()
        #questionWindow.mainloop()

    def createImage(self,artifact):
        image = Image.new("RGB", (20, 15), "White")
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("FreeMono.ttf",15)
        draw.text((0,0),str(artifact.answer),font=font,fill="Black")
        #image.save(,str(artifact.answer)+".jpg","JPEG")
        image.save("./data/answers/"+str(artifact.answer)+".gif")

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



# Dan Gorringe January 2018
