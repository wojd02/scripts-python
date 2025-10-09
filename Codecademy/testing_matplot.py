from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as stats
import pandas as pd
import statsmodels.api as sm

x_values = [0, 1, 2, 3, 4]
y_values = [0, 1, 4, 9, 16]

days = [0,1,2,3,4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

plt.plot(days, revenue, color = 'lightgreen', linestyle = '--')
plt.plot(days, costs, color = 'purple', marker = 's')
plt.legend(['revenue', 'costs'], loc = 4) # loc = legend location
plt.show()

months = range(12)
temperature = [36, 36, 39, 52, 61, 72, 77, 75, 68, 57, 48, 48]
flights_to_hawaii = [1200, 1300, 1100, 1450, 850, 750, 400, 450, 400, 860, 990, 1000]

plt.subplot(1, 2, 1)
plt.plot(temperature, months)

plt.subplot(1,2,2)
plt.plot(temperature, flights_to_hawaii, 'o')


plt.show()

x = range(7)
straight_line = [0, 1, 2, 3, 4, 5, 6]
parabola = [0, 1, 4, 9, 16, 25, 36]
cubic = [0, 1, 8, 27, 64, 125, 216]

plt.subplot(2, 1, 1) #creates a grid with 2 rows and 1 column, and selects the first (top) box for the first plot.
plt.plot(straight_line, x)


plt.subplot(2, 2, 3) # switches to a grid with 2 rows and 2 columns, and selects the third box (bottom left) for the second plot.
plt.plot(x, parabola)

plt.subplot(2,2,4) #selects the fourth box (bottom right) in the same 2x2 grid for the third plot.
plt.plot(x, cubic)

plt.subplots_adjust(bottom = 0.2, wspace=0.35)

plt.show()
plt.clf()

word_length = [8, 11, 12, 11, 13, 12, 9, 9, 7, 9]
power_generated = [753.9, 768.8, 780.1, 763.7, 788.5, 782, 787.2, 806.4, 806.2, 798.9]
years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]

plt.close('all')

plt.figure()
plt.plot(years, word_length)
plt.savefig('winning_word_length.png')

plt.figure(figsize=(7,3)) #create a figure
plt.plot(years, power_generated)
plt.savefig('power_generated.png') #saving file

#plt.plot(x_values, y_values)
#plt.show()
#plt.clf()

#var_1 = stats.poisson.pmf()
#var_2 = stats.trim_mean([7,5,6,3,2,7,5], 0.1)
#print(var_2)

#var_3 = sm.OLS.from_formula()
#var_4 = stats.ttest_1samp()