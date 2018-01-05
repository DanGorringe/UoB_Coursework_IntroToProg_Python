import shutil
import math
from termcolor import colored

#set origin to midpoint
originX = shutil.get_terminal_size().lines/2
originY = shutil.get_terminal_size().columns/2

for y in range(shutil.get_terminal_size().lines - 1):
    realY = int(originX) - y
    for x in range(shutil.get_terminal_size().columns):
        realX = x - int(originY)
        #Print the function
        if realY == int(10*math.cos(realX/10)):
            toPrint = colored("\u2588",'red')
            print(toPrint,end="")
        #create axis
        #Y axis
        elif x == int(originY):
            if y == 0:
                toPrint = colored("^",'white')
                print(toPrint,end="")
            else:
                toPrint = colored("|",'white')
                print(toPrint,end="")
        #X axis
        elif y == int(originX):
            if x == shutil.get_terminal_size().columns:
                toPrint = colored(">",'white')
                print(toPrint,end="")
            else:
                toPrint = colored("-",'white')
                print(toPrint,end="")
        #Else empty space
        else:
            print(" ",end='')

# Dan Gorringe January 2018
