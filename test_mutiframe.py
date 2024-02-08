# Importing libraries 
import matplotlib.pyplot as plt 
import numpy as np 
import math 
plt.figure(figsize=(12, 12))
# Placing the plots in the plane 

numberofframe = 3
height_list = [400,400,400]
width_list = [300,200,100]
colors = ['powderblue', 'red', 'green', 'blue', 'orange', 'purple', 'yellow', 'brown', 'pink', 'cyan']

def loop_of_frame(numberofframe, height_list, width_list, colors, count):
    plot = plt.subplot2grid((2, numberofframe), (0, count), colspan=1)
    rectangle = plt.Rectangle((0, 0), height_list[count], width_list[count], fill=None, edgecolor = colors[count], linewidth=1)
    plot.add_patch(rectangle)
    plot.set_xlim([-10, height_list[count]+10])
    plot.set_ylim([-10, width_list[count]+10])
    plot.set_aspect('equal')
    plot.axis('off')
    return plot

# plot1 = plt.subplot2grid((2, 3), (0, 0), colspan=1) 
# plot2 = plt.subplot2grid((2, 3), (0, 1), colspan=1) 
# plot3 = plt.subplot2grid((2, 3), (0, 2), colspan=1) 

# rectangle = plt.Rectangle((0, 0), 50, 100, fill=None, edgecolor='powderblue', linewidth=1)
# plot1.add_patch(rectangle)
# plot1.set_xlim([-10, 105])
# plot1.set_ylim([-10, 105])
# plot1.set_aspect('equal')
# plot1.axis('off')

# rectangle1 = plt.Rectangle((0, 0), 100, 100, fill=None, edgecolor='red', linewidth=1)
# plot2.add_patch(rectangle1)
# plot2.set_xlim([-10, 105])
# plot2.set_ylim([-10, 105])
# plot2.set_aspect('equal')
# plot2.axis('off')

# rectangle2 = plt.Rectangle((0, 0), 100, 100, fill=None, edgecolor='green', linewidth=1)
# plot3.add_patch(rectangle2)
# plot3.set_xlim([-10, 105])
# plot3.set_ylim([-10, 105])
# plot3.set_aspect('equal')
# plot3.axis('off')

for x in range(numberofframe):
    loop_of_frame(numberofframe, height_list, width_list, colors, x)

# plt.tight_layout() 
plt.show() 
