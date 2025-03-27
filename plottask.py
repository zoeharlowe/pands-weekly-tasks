# plottask.py
# This program displays:
# a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2 
# and a plot of the function  h(x)=x3 in the range 0 to 10
# on the same set of axes
# Author: Zoe McNamara Harlowe

import numpy as np
import matplotlib.pyplot as plt

# Create a normal distribution of 1000 values with a mean of 5 and standard deviation of 2
mean = 5
std = 2
size = 1000
np.random.seed(1)
values = np.random.normal(mean, std, size)

# Create the function h(x)=x^3 in the range 0 to 10
xpoints = np.array(range(0,11))
ypoints = xpoints * xpoints * xpoints

# Plot h(x)=x^3
plt.plot(xpoints, ypoints, label='h(x)=x^3', color = 'red')
plt.title('Normal Distribution and h(x)=x^3')

# Plot histogram on same set of axes
plt.hist(values, label='Histogram of Normal Distribution', color = 'green', edgecolor = 'black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()

# Limit the height of the y-axis to clearly display histogram
# I found out how to do this on Stack Overflow: https://stackoverflow.com/questions/45699759/how-do-you-limit-the-y-axis-height-in-matplotlib
plt.ylim(0, 400)

plt.savefig('plot-task.png')
plt.show()