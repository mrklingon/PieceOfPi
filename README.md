# PieceOfPi
**estimate Pi with the *Monte Carlo method* and a neotrinkey**

The power of randomness can be harnessed! Estimating the area of a circle by throwing darts at random gives you the means to estimate the value of Pi! 

*Monte Carlo methods are a broad class of computational algorithms that
rely on repeated random sampling to obtain numerical results. One of
the basic examples of getting started with the Monte Carlo algorithm
is the estimation of Pi.* (https://www.geeksforgeeks.org/estimating-value-pi-using-monte-carlo/)

This project iterates over a unit circle of radius one and "throws" darts at random from -1 to 1 x, and -1 to 1 y, then counts how many land **IN** the circle. Pi is estimated by multiplying 4 * **"darts inside circle"**/**all darts thrown**

The more iterations (darts) thrown, the closer you approach the value of Pi.

The program runs continuously, pausing 5 seconds between runs. While the program is running/estimating, the neopixels flash random colors. When it finishes an estimate, the neopixel displays the answer by blinking the neopixels green for the value (three times for *three*, one time for **one** and so on.). Zeroes are indicated by turning all pixels pink briefly.

If the program is run inside a REPL like Mu, it will print out the results:

```
 I will estimate Pi.
it is around : 3.14139
I will estimate Pi.
it is around : 3.13818
I will estimate Pi.
it is around : 3.13422
I will estimate Pi.
it is around : 3.1313 
```

The default value of Iterations is 100 - you can change that to higher or lower values.

#Files#
* findPi.py - copy to code.py to run
* ncount.py - helper file, provides color definitions and blinknum() to blink the digit values.
