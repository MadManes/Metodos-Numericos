import matplotlib.pyplot as plt 
import numpy as np

def funcion(x):
    return 1/x

t = np.arange(0., 5., 0.2)


fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot(t, 1/t)   # Plot some data on the Axes.
plt.show()                           # Show the figure.