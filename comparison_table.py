import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

# Generate some random data for 9 arrows
angles = [157.2,162.9,139.7,125.8,123.3,105.6,113.9,108.6,130.6,157.44,161.86,138.77,128.16,118.87,90.68,113.74,97.68,130.26]
angles_model = [157.44,161.86,138.77,128.16,118.87,90.68,113.74,97.68,130.26]
num_arrows = 18
  # random angles between 0 and 360 degrees
times = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
  # random time points between 0 and 10 seconds

# Create the plot
fig, ax = plt.subplots(figsize=(8, 8))

# Add the arrows and angle circles to the plot
for i in range(num_arrows):
    x, y = times[i], i + 3
    dx, dy = np.cos(np.deg2rad(angles[i])), np.sin(np.deg2rad(angles[i]))
    ax.arrow(x, y, dx, dy, width=0.01, head_width=0.1, head_length=0.1, color='#636363')

    # Add degree labels to arrows
    degree_label = '{:.0f}°'.format(angles[i])
    ax.text(x + 1.5 * dx, y + 1.5 * dy, degree_label, fontsize=10, color='black', va='center', ha='center')

    # Add angle circles to arrows
    circle = plt.Circle((x, y), radius=0.3, color='#636363', alpha=0.2)
    ax.add_artist(circle)
    arc_patch = Arc((x, y), width=0.5, height=0.5, angle=0, theta1=0, theta2=angles[i],
                    color='#F0B20B')
    ax.add_patch(arc_patch)

# Set the x and y limits
ax.set_xlim(-1, 20)
ax.set_ylim(0, num_arrows +3)
ax.set_aspect('equal', adjustable='box')

# Set the ticks and tick labels
ax.set_yticks(np.arange(1, num_arrows + 1))
ax.set_xticks(times)



# Set the axis labels
ax.set_xlabel('Time (seconds)')
ax.set_ylabel('Arrows')
ax.grid(linestyle='-', linewidth='0.5', color='lightgrey', alpha=0.7)
# Show the plot

plt.show()


