import matplotlib.pyplot as plt
import numpy as np

# Create a list of angles
angles = np.linspace(0, 2*np.pi, 360)

# Set the radius
r = 1

# Calculate the x and y coordinates of points on a circle
x = r*np.cos(angles)
y = r*np.sin(angles)

# Set up the figure
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)

# Draw a pretty fractal
ax.plot(angles, x, color='red', linewidth=2)
ax.plot(angles, y, color='blue', linewidth=2)
ax.plot(angles, x*y, color='green', linewidth=2)

# Show the plot
plt.show()

