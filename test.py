import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


# Function to draw a rectangle with dimensions
def draw_rectangle_with_dimensions(ax, origin, width, height):
    # Draw the rectangle
    rect = Rectangle(origin, width, height, fill=None, edgecolor='g', linewidth=1)
    ax.add_patch(rect)

    # Annotate width
    ax.annotate(f"{width}", xy=(origin[0] + width / 2, origin[1]), xytext=(0, -30),
                textcoords="offset points", ha='center', va='bottom')

    # Annotate height
    ax.annotate(f"{height}", xy=(origin[0], origin[1] + height / 2), xytext=(-30, 0),
                textcoords="offset points", ha='right', va='center')


# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Draw a rectangle with dimensions
draw_rectangle_with_dimensions(ax, (2, 2), 3, 2)

# Set aspect of the plot to be equal
ax.set_aspect('equal')

# Turn off the axes
ax.axis('off')

# Display the plot
plt.show()