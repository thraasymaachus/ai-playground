import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create the vertices of a regular hexagon with a given size (distance from the center to a vertex)
def create_hexagon_vertices(size):
    angle = np.linspace(0, 2 * np.pi, 7)[:-1]
    return np.column_stack((size * np.cos(angle), size * np.sin(angle)))

# Define the faces of the hexahexaflexagon
def create_hexahexaflexagon_faces():
    faces = [1, 2, 3, 4, 5, 6]
    return [
        [faces[0], faces[1], faces[2]],
        [faces[2], faces[3], faces[4]],
        [faces[4], faces[5], faces[0]],
        [faces[1], faces[3], faces[5]]
    ]

# Draw the hexahexaflexagon using matplotlib
def draw_hexahexaflexagon(ax, hexagon_vertices, hexahexaflexagon_faces, face_colors):
    for i, face in enumerate(hexahexaflexagon_faces):
        # Create a polygon patch for each face
        polygon = plt.Polygon(hexagon_vertices[[face[0] - 1, face[1] - 1, face[2] - 1]], facecolor=face_colors[i], lw=1)
        ax.add_patch(polygon)
        # Add face numbers as text labels
        for j in range(3):
            ax.text(hexagon_vertices[face[j] - 1, 0], hexagon_vertices[face[j] - 1, 1], str(face[j]), fontsize=12, ha="center", va="center")

# Draw the state diagram using matplotlib
def draw_state_diagram(ax, hexagon_vertices, hexahexaflexagon_faces):
    # Define the positions for the states in the diagram
    state_positions = np.array([
        [0, 1],
        [1, 1],
        [1, 0],
        [0, 0]
    ])

    # Draw each state as a circle with a label indicating the corresponding face configuration
    for i, face in enumerate(hexahexaflexagon_faces):
        ax.add_artist(plt.Circle((state_positions[i, 0], state_positions[i, 1]), 0.5, lw=1, fill=False))
        ax.text(state_positions[i, 0], state_positions[i, 1], f"{face[0]}-{face[1]}-{face[2]}", fontsize=12, ha="center", va="center")

# Main function to create and display the hexahexaflexagon and state diagram
def main():
    hexagon_size = 1
    hexagon_vertices = create_hexagon_vertices(hexagon_size)
    hexahexaflexagon_faces = create_hexahexaflexagon_faces()

    face_colors = ["red", "blue", "green", "yellow"]

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    draw_hexahexaflexagon(axes[0], hexagon_vertices, hexahexaflexagon_faces, face_colors)
    draw_state_diagram(axes[1], hexagon_vertices, hexahexaflexagon_faces)

    # Set up the axes for display
    for ax in axes:
        ax.set_xlim(-2 * hexagon_size, 2 * hexagon_size)
        ax.set_ylim(-2 * hexagon_size, 2 * hexagon_size)
        ax.set_aspect("equal", "box")
        ax.axis("off")

    # Display the hexahexaflexagon and state diagram
    plt.show()

# Run the main function
if __name__ == "__main__":
    main()
