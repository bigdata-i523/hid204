import matplotlib.pyplot as plt  #import the required libraries
import numpy as np

n = 100
x = np.random.randn(n)  #create a numpy array x with 100 random values taken from a normal distribution
y = x * np.random.randn(n) #create a numpy array y with 100 random values taken from a normal distribution multiplied by respective x values

figure, ax = plt.subplots() # save the output tuple into variables figure and ax
fit = np.polyfit(x, y, deg=1) # fit a polynomial of degree 1 according to the values of x and y arrays and returns an array of coefficients of the polynomial
ax.plot(x, fit[0] * x + fit[1], color='blue') # plot the line with respect to the coefficients returned (something like ax + b)
ax.scatter(x, y) # scatter plot the values in the array x and y

figure.show() # output the resulting figure

#The program tries to find the best fit line that can represent the points(x,y) which are stored in numpy arrays x and y respectively.
#If we increase the degree , we will get a polynomial which can fit the given points in an even better way.
