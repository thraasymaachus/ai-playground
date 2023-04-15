import matplotlib.pyplot as plt
import numpy as np

# Set parameters for the fractal
xmin, xmax, ymin, ymax = -2.5, 1.5, -2, 2
width, height = 1000, 1000
maxiter = 100

# Create a grid of points
X, Y = np.meshgrid(np.linspace(xmin, xmax, width), np.linspace(ymin, ymax, height))

# Create a complex number from the grid of points
C = X + Y*1j

# Create a matrix of zeros
Z = np.zeros(C.shape, dtype=np.int32)

# Iterate over the matrix
for i in range(maxiter):
    Z = Z**2 + C

# Create a mask to filter out points that diverge
mask = np.abs(Z) < 2

# Plot the fractal
plt.imshow(mask, extent=[xmin, xmax, ymin, ymax])
plt.show()