import numpy as np
import matplotlib.pyplot as plt

class Hexahexaflexagon:
    def __init__(self, size=1, face_colors=None):
        self.size = size
        self.faces = self.create_hexahexaflexagon_faces()
        self.state_positions = np.array([
            [0, 1],
            [1, 1],
            [1, 0],
            [0, 0]
        ])
        self.current_state = 0
        self.face_colors = face_colors if face_colors else ["red", "blue", "green", "yellow", "cyan", "magenta"]

    def create_hexahexaflexagon_faces(self):
        faces = [1, 2, 3, 4, 5, 6]
        return [
            [faces[0], faces[1], faces[2]],
            [faces[2], faces[3], faces[4]],
            [faces[4], faces[5], faces[0]],
            [faces[1], faces[3], faces[5]]
        ]

    def draw(self, axes):
        axes[0].clear()
        axes[1].clear()
        self.draw_hexahexaflexagon(axes[0])
        self.draw_tuckerman_traverse(axes[1])

        for a in axes:
            a.set_xlim(-2 * self.size, 2 * self.size)
            a.set_ylim(-2 * self.size, 2 * self.size)
            a.set_aspect("equal", "box")
            a.axis("off")

    def draw_hexahexaflexagon(self, ax):
        # Define the layout of the hexahexaflexagon
        layout = [
            [1, 2],
            [3, 4],
            [5, 6]
        ]

        face = self.faces[self.current_state]
        for i, f in enumerate(face):
            x_offset = layout[i][0] - 1
            y_offset = layout[i][1] - 1
            ax.add_patch(plt.Rectangle((x_offset, y_offset), 1, 1, facecolor=self.face_colors[f - 1], lw=1))
            ax.text(x_offset + 0.5, y_offset + 0.5, str(f), fontsize=12, ha="center", va="center")

    def draw_tuckerman_traverse(self, ax):
        edges = [
            (0, 1),
            (1, 2),
            (2, 3),
            (3, 0)
        ]

        for i, edge in enumerate(edges):
            x1, y1 = self.state_positions[edge[0]]
            x2, y2 = self.state_positions[edge[1]]
            ax.plot([x1, x2], [y1, y2], "k-", lw=1)

            circle = plt.Circle((self.state_positions[i, 0], self.state_positions[i, 1]), 0.5, lw=1, fill=(i == self.current_state))
            ax.add_artist(circle)

    def on_click(self, event):
        if event.inaxes is None: return
        if event.button != 1: return

        nearest_state = np.argmin(np.sum((self.state_positions - [event.xdata, event.ydata])**2, axis=1))
        self.current_state = nearest_state
        self.draw(event.inaxes.figure.axes)

def main():
    hexahexaflexagon = Hexahexaflexagon()

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))
    hexahexaflexagon.draw(axes)

    def on_click(event):
        hexahexaflexagon.on_click(event)

    # Connect the click event to the on_click function
    fig.canvas.mpl_connect('button_press_event', on_click)

    # Display the interactive hexahexaflexagon and Tuckerman traverse
    plt.show()

if __name__ == "__main__":
    main()

