%matplotlib osx
import matplotlib.pyplot as plt
import numpy as np

# Generate a seq of nums from -10 to 10 w/100 steps in between.
x = np.linspace(-10, 10, 100)
# Create a second array using the sine function.
y = np.sin(x)
# The plot function makes a line chart of one array against the other. 
plt.plot(x, y, marker="x")

 