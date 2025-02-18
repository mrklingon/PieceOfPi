import random
import time
from ncount import *

#Use the Monte Carlo Method to estimate Pi
# https://www.geeksforgeeks.org/estimating-value-pi-using-monte-carlo/
# https://en.wikipedia.org/wiki/Monte_Carlo_method

Iterations = 100 #how many "darts" to throw at circle.

def pickpoint(): #choose a random point between -1 and 1
    x = (random.randrange(2000)-1000)/1000
    return x

def decimal(num): #use blinknum from ncount.py to display decimal value
    nstr = str(num)
    for c in nstr:
        if c == ".":
            docolor(blue) #indicate 'point' with blue
        else:
            if (eval(c)>0):
                blinknum(eval(c),green)
                docolor(blank)
                time.sleep(.5)
            else:
                if c == "0":
                    docolor(pink) # indicate 0 with pink
                    time.sleep(.5)


def distxy(x,y):

    dist = x**2
    dist = dist + y**2

    return dist**.5


Inside = 0
Outside = 0
print()
while True:
    for i in range(Iterations):
        pixels[random.randrange(4)]=random.choice(colors) #blink pixels to show we're "thinking"
        d = distxy(pickpoint(),pickpoint()) #how far is random x,y from center
        Outside = Outside + 1 #tally of all points
        if d < 1: #count the points within the circle
            Inside = Inside + 1

    print ("I will estimate Pi.")
    p = 4  * (Inside / Outside)

    print ("it is around : " + str(p))
    decimal(p) #blink the values
    docolor(orange) #show orange
    time.sleep(5) #pause before doing it again
