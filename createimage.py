import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import io

# Function to draw a rectangle with dimensions
def draw_rectangle_with_dimensions(width, height, dot_x, dot_y,dot_xx, dot_yy, eyelevel):
    # Draw the rectangle
    # Create a Matplotlib figure
    fig, ax = plt.subplots()

    # ax.set_xlim([-100, max(10, width)])
    # ax.set_ylim([-50, max(10, height)])
    # x_min, x_max = ax.get_xlim()
    # y_min, y_max = ax.get_ylim()

    x_offset = width * 0.03  # 2% of the x-axis range
    y_offset = height * 0.03
    print(y_offset)
    print(x_offset)
    pointtoground = height - dot_y + eyelevel - (height / 2)
    pointtoeyeslevel = height /2 - dot_y

    # frame width
    ax.annotate(f"{width}", xy=(2 + width / 2, 2), xytext=(0, -30),
                textcoords="offset points", ha='center', va='bottom')
    # frame height
    ax.annotate(f"{height}", xy=(width, 2 + height / 2), xytext=(30, 0),
                textcoords="offset points", ha='left', va='center')
    # point height
    ax.annotate(f"{dot_y}", xy=(dot_x , height - dot_y), xytext=(0, 10),
                textcoords="offset points", ha='center', va='bottom')
    # point width
    ax.annotate(f"{dot_x}", xy=(dot_x/2/2*3, height - dot_y), xytext=(0, 0),
                textcoords="offset points", ha='center', va='top')
    # point to ground
    ax.annotate(f"{pointtoground}", xy=(0, height /3 ), xytext=(-30, 0),
                textcoords="offset points", ha='center', va='bottom')
    # point to eyeslevel
    ax.annotate(f"{pointtoeyeslevel}", xy=(dot_x, height / 3 * 2), xytext=(20, 0),
                textcoords="offset points", ha='center', va='bottom')

    # Draw the rectangle
    rectangle = plt.Rectangle((0, 0), width, height, fill=None, edgecolor='blue', linewidth=1)
    ax.add_patch(rectangle)
    # Eyelevel line
    # ax.axhline(y=height /2 , linewidth=1, color='green')  # Adjust linewidth and color as needed
    ax.plot([0, width], [height /2, height /2], linewidth=1, color='green')

    dot_yfromtop = height - dot_y

    # Add the point
    dot = plt.plot(dot_x, dot_yfromtop, marker='o', color='red')[0]  # Get the plot object for customization
    dot.set_markersize(1)  # Adjust marker size as needed
    # line of point to floor
    ax.plot([-x_offset, -x_offset], [dot_yfromtop, -100], linewidth=1, color='black', ls='--')
    # point to eyeslevel line
    ax.plot([dot_x, dot_x], [dot_yfromtop, height / 2 ], linewidth=1, color='black', ls='--')

    # double point mode
    if dot_yy > 0:
        # point height
        ax.annotate(f"{dot_yy}", xy=(dot_x + dot_xx, height - dot_yy), xytext=(0, 10),
                    textcoords="offset points", ha='center', va='bottom')
        # point width
        ax.annotate(f"{dot_xx}", xy=((dot_x + dot_xx)/3*2, height - dot_yy), xytext=(0, 0),
                    textcoords="offset points", ha='center', va='top')
        # point to eyeslevel
        ax.annotate(f"{height / 2 - dot_yy}", xy=(dot_xx, height / 3 * 2), xytext=(-20, 0),
                    textcoords="offset points", ha='center', va='bottom')

        # point to eyeslevel line
        dot_yyfromtop = height - dot_yy

        ax.plot([dot_x + dot_xx, dot_x + dot_xx], [dot_yyfromtop, height / 2], linewidth=1, color='black', ls='--')
        dot1 = plt.plot(dot_x + dot_xx, dot_yyfromtop, marker='o', color='red')[0]  # Get the plot object for customization
        dot1.set_markersize(1)
    else:
        pass

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
