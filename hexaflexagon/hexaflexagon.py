import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Polygon, Arrow

class Hexaflexagon:
    def __init__(self):
        self.faces = [1, 2, 3]
        self.current_state = 0
        self.face_colors = ["red", "blue", "green"]
        self.state_positions = np.array([[0, 0], [1, 0], [0.5, 1]])

    def draw_hexaflexagon(self, ax):
        ax.clear()
        ax.set_xlim(-1, 2)
        ax.set_ylim(-1, 2)
        ax.set_aspect("equal", "box")
        ax.axis("off")

        face = self.faces[self.current_state]
        x, y = 0.5, 1

        # Create hexagon vertices
        vertices = [[x - 0.5, y - 0.5], [x + 0.5, y - 0.5], [x + 1, y], [x + 0.5, y + 0.5], [x - 0.5, y + 0.5], [x - 1, y]]

        # Draw the hexagon divided into six triangles
        for i in range(6):
            triangle_vertices = [vertices[i], vertices[(i+1) % 6], [x, y]]
            triangle = Polygon(triangle_vertices, fc=self.face_colors[face - 1], lw=1, edgecolor='black')
            ax.add_patch(triangle)

    def draw_tuckerman_traverse(self, ax):
        ax.clear()
        ax.set_xlim(-1, 2)
        ax.set_ylim(-1, 2)
        ax.set_aspect("equal", "box")
        ax.axis("off")

        for i, pos in enumerate(self.state_positions):
            circle = plt.Circle(pos, 0.1, lw=1, fill=(i == self.current_state))
            ax.add_artist(circle)
            ax.text(pos[0], pos[1], str(self.faces[i]), fontsize=12, ha="center", va="center")

            if i < len(self.state_positions) - 1:
                next_pos = self.state_positions[i + 1]
            else:
                next_pos = self.state_positions[0]

            arrow = Arrow(pos[0], pos[1], next_pos[0] - pos[0], next_pos[1] - pos[1], width=0.1, alpha=0.5)
            ax.add_artist(arrow)

    def update(self, frame, ax1, ax2):
        self.current_state = frame % len(self.faces)
        self.draw_hexaflexagon(ax1)
        self.draw_tuckerman_traverse(ax2)

def main():
    hexaflexagon = Hexaflexagon()
    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    ani = FuncAnimation(fig, hexaflexagon.update, frames=range(6), fargs=(axes[0], axes[1]), interval=1000, repeat=True)
    plt.show()

if __name__ == "__main__":
    main()
