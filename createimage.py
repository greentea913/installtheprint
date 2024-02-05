import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import io

# Function to draw a rectangle with dimensions
def draw_rectangle_with_dimensions(width, height, dot_x, dot_y,dot_xx, dot_yy, eyelevel):
    # Draw the rectangle
    # Create a Matplotlib figure
    fig, ax = plt.subplots()

    # frame width
    ax.annotate(f"{width}", xy=(2 + width / 2, 2), xytext=(0, -30),
                textcoords="offset points", ha='center', va='bottom')

    # frame height
    ax.annotate(f"{height}", xy=(width, 2 + height / 2), xytext=(30, 0),
                textcoords="offset points", ha='right', va='center')
    # point width
    ax.annotate(f"{dot_y}", xy=(dot_x , height - dot_y), xytext=(0, 10),
                textcoords="offset points", ha='center', va='bottom')
    # point height
    ax.annotate(f"{dot_x}", xy=(dot_x, height - dot_y), xytext=(-15, -5),
                textcoords="offset points", ha='center', va='bottom')
    # point to group
    ax.annotate(f"{height - dot_y + eyelevel - (height / 2)}", xy=(0, height /3 ), xytext=(-30, 0),
                textcoords="offset points", ha='center', va='bottom')
    # point to eyeslevel
    ax.annotate(f"{height /2 - dot_y}", xy=(dot_x, height / 3 * 2), xytext=(20, 0),
                textcoords="offset points", ha='center', va='bottom')

    # Draw the rectangle
    rectangle = plt.Rectangle((0, 0), width, height, fill=None, edgecolor='blue', linewidth=1)
    ax.add_patch(rectangle)
    # Eyelevel line
    # ax.axhline(y=height /2 , linewidth=1, color='green')  # Adjust linewidth and color as needed
    ax.plot([0, width], [height /2, height /2], linewidth=1, color='green')

    dot_y = height - dot_y

    # Add the point
    dot = plt.plot(dot_x, dot_y, marker='o', color='red')[0]  # Get the plot object for customization
    dot.set_markersize(1)  # Adjust marker size as needed
    # point to floor line
    ax.plot([-10, -10], [dot_y, -100], linewidth=1, color='black', ls='--')
    # point to eyeslevel line
    ax.plot([dot_x, dot_x], [dot_y, height / 2 ], linewidth=1, color='black', ls='--')

    if dot_yy > 0:
        # point width
        ax.annotate(f"{dot_yy}", xy=(dot_xx, height - dot_yy), xytext=(10, 10),
                    textcoords="offset points", ha='center', va='bottom')
        # point height
        ax.annotate(f"{dot_xx}", xy=(dot_x + dot_xx, height - dot_yy), xytext=(-15, -5),
                    textcoords="offset points", ha='center', va='bottom')
        # point to eyeslevel
        ax.annotate(f"{height / 2 - dot_yy}", xy=(dot_xx, height / 3 * 2), xytext=(-20, 0),
                    textcoords="offset points", ha='center', va='bottom')
        # point to eyeslevel line
        dot_yy = height - dot_yy
        ax.plot([dot_x + dot_xx, dot_x + dot_xx], [dot_yy, height / 2], linewidth=1, color='black', ls='--')
        dot1 = plt.plot(dot_x + dot_xx, dot_yy, marker='o', color='red')[0]  # Get the plot object for customization
        dot1.set_markersize(1)
    else:
        pass
    ax.set_xlim([-100, max(10, width)])
    ax.set_ylim([0, max(10, height)])
    ax.set_aspect('equal')
    ax.axis('off')

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi = 300)
    # Close the figure to release resources
    plt.close(fig)

    # Seek to the beginning of the buffer to be able to read its contents
    buf.seek(0)
    # Return the PNG image data as a bytes object
    return buf.read()
# # Set up the figure and axis

# Draw a rectangle with dimensions

# Display the plot
