import matplotlib.pyplot as plt

def curve_function(x, mod):
    return (x**3 - 2*x + 1) % mod

def plot_curve(mod):
    x_values = list(range(mod))
    y_values = [curve_function(x, mod) for x in x_values]

    # Find the square residues for each value in the field
    square_residues = set()
    for i in range(mod):
        square_residues.add((i**2) % mod)

    # Get the points (x, y) where y^2 is a square residue of the curve function value
    points = []
    for x, y_square in zip(x_values, y_values):
        if y_square in square_residues:
            # Find possible y values (y and -y) for the given x
            y = [i for i in range(mod) if (i**2) % mod == y_square]
            for y_value in y:
                points.append((x, y_value))

    # Plot the points
    plt.scatter(*zip(*points), marker='o', s=20)
    plt.title(f'Plot of y^2 = x^3 - 2x + 1 over Integers Modulo {mod}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

# Plot the curve over integers modulo 89
plot_curve(89)
