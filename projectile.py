import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
import numpy as np

'''time = []
X_pos = []
Y_pos = []
Z_pos = []
Vx_list = []
Vy_list = []
Vz_list = []
X_2 = []
Y_2 = []
Z_2 = []

time_2 = []
X_pos_2 = []
Y_pos_2 = []
Z_pos_2 = []
Vx_list_2 = []
Vy_list_2 = []
Vz_list_2 = []

t_end = 0

def generate_datapoints(selection,x_t ,y_t ,z_t ,azimuth,elevation,C_drag,Caliber_diameter,Caliber_mass, air_density, muzzle_velocity):
    global X_pos, Y_pos, Z_pos, time, Vx_list, Vy_list, Vz_list, \
        X_pos_2, Y_pos_2, Z_pos_2, time_2, Vx_list_2, Vy_list_2, Vz_list_2, t_end

    g = 9.8066
    V0_z = muzzle_velocity * np.sin(elevation*0.0174532925)
    V0_x = muzzle_velocity * np.cos(elevation*0.0174532925) * np.cos(azimuth*0.0174532925)
    V0_y = muzzle_velocity * np.cos(elevation*0.0174532925) * np.sin(azimuth*0.0174532925)
    Caliber_cross_section = np.pi * (Caliber_diameter*0.001)**2
    V_terminal = (2 * Caliber_mass * g / (C_drag * air_density * Caliber_cross_section))**0.5
    V_z = V0_z
    V_x = V0_x
    V_y = V0_y
    t_peak = 0
    while True:
        D_z = 0.5 * C_drag * air_density * Caliber_cross_section * V_z
        D_x = 0.5 * C_drag * air_density * Caliber_cross_section * V_x
        D_y = 0.5 * C_drag * air_density * Caliber_cross_section * V_y
        V_z = V_z - (g + (D_z / Caliber_mass))
        V_x = V_x - (D_x / Caliber_mass)
        V_y = V_y - (D_y / Caliber_mass)
        x_t = x_t + V_x
        y_t = y_t + V_y
        z_t = z_t + V_z
        if selection == 1:
            X_pos.append(x_t)
            Y_pos.append(y_t)
            Z_pos.append(z_t)
        elif selection ==2:
            X_pos_2.append(x_t)

            Y_pos_2.append(y_t)
            Z_pos_2.append(z_t)
        if V_z <= 0:
            H_max = z_t
            H_max_x = x_t
            H_max_y = y_t
            break
        else:
            t_peak = t_peak + 1
    z_t = H_max
    x_t = H_max_x
    y_t = H_max_y
    t_end = t_peak
    while True:
        D_z = 0.5 * C_drag * air_density * Caliber_cross_section * V_z
        D_x = 0.5 * C_drag * air_density * Caliber_cross_section * V_x
        D_y = 0.5 * C_drag * air_density * Caliber_cross_section * V_y
        V_x = V_x - (D_x / Caliber_mass)
        V_y = V_y - (D_y / Caliber_mass)
        V_z = V_z + (g - (D_z / Caliber_mass))
        x_t = x_t + (V_x)
        y_t = y_t +(V_y)
        z_t = z_t - V_z
        if selection == 1:
            X_pos.append(x_t)
            Y_pos.append(y_t)
            Z_pos.append(z_t)
        elif selection == 2:
            X_pos_2.append(x_t)
            Y_pos_2.append(y_t)
            Z_pos_2.append(z_t)
        if V_z >= V_terminal:
            V_z = V_terminal
        else:
            pass
        if z_t <= 0:
            break
        else:
            t_end = t_end + 1

    if selection == 1:
        X_pos.reverse()
        Y_pos.reverse()
    else:
        X_pos_2.reverse()
        Y_pos_2.reverse()


generate_datapoints(1, 0, 0, 0, 45, 25, 0.5, 155, 50, 1.225, 750)
generate_datapoints(2, 0, 0, 0, 45, 35, 0.5, 155, 50, 1.225, 650)

fig = plt.figure()
# define the x, y, and z data for the parabolic line

ax = plt.axes(projection='3d')
ax.set_xlim3d(25000, 35000)
ax.set_ylim3d(20000, 30000)
ax.set_zlim3d(0, 2000)
ax.xaxis._axinfo["grid"].update({"linewidth":0.1, 'color':'black', 'linestyle':'dashed'})
ax.yaxis._axinfo["grid"].update({"linewidth":0.1, 'color':'black'})
ax.zaxis._axinfo["grid"].update({"linewidth":0.1, 'color':'black'})
ax.w_xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.w_yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
ax.w_zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))

colors = ['#7FBB87', '#D66272', '#BA86F8', '#F9B52E']
count = 0
for i in [Z_pos[45],Z_pos[51],Z_pos[32],Z_pos[39]]:
        r = 10
        z0 = i # To have the tangent at y=0
        y0 = Y_pos[Z_pos.index(i)]
        x0 = X_pos[Z_pos.index(i)]

        # Theta varies only between pi/2 and 3pi/2. to have a half-circle
        theta = np.linspace(0, 2*np.pi, 201)
        a = 1.1
        color = colors[count]
        h = [45,51,32,39]
        for j in range(11):
            z_2 = (3*r*np.cos(theta) + z0)  # y - y0 = r*cos(theta)
            y_2 = 4*r*np.sin(theta) + y0 # z - z0 = r*sin(theta)
            x_2 = 4*r*np.sin(-theta) + x0
            a = a - 0.1
            r = r+100 # To have the tangent at y=0
            y0 = Y_pos[Z_pos.index(Z_pos[h[count]-j])]
            x0 = X_pos[Z_pos.index(Z_pos[h[count]-j])]
            X_2.append(x_2)
            Y_2.append(y_2)
            Z_2.append(z_2)
        count = count + 1

X_Sensor=[9000,12000,28000,33000]
Y_Sensor=[35000,37500,25000,23000]
Z_Sensor=[0,0,0,0]

txt = ['CASTLE-1','CASTLE-2','CASTLE-3','CASTLE-4']

ax.scatter(xs=X_Sensor, ys=Y_Sensor, zs=Z_Sensor, s =10,c= 'blue')

for k in range (4):
    ax.text(X_Sensor[k], Y_Sensor[k], Z_Sensor[k], txt[k], size = 5, zorder=1, color='k')


X_arrow=[]
Y_arrow=[]
Z_arrow=[]
for l in [Z_pos[51],Z_pos[45],Z_pos[32],Z_pos[39]]:
    X_arrow.append(X_pos[Z_pos.index(l)])
    Y_arrow.append(Y_pos[Z_pos.index(l)])
    Z_arrow.append(l)
colors_2 = ['#D66272','#7FBB87', '#BA86F8', '#F9B52E']

for m in range(4):
    sketch_x = []
    sketch_y = []
    sketch_z = []
    sketch_x.append(X_arrow[m])
    sketch_y.append(Y_arrow[m])
    sketch_z.append(Z_arrow[m])
    sketch_x.append(X_Sensor[m])
    sketch_y.append(Y_Sensor[m])
    sketch_z.append(Z_Sensor[m])

doa, = ax.plot3D(sketch_x, sketch_y, sketch_z, c=colors_2[m], alpha=0.5)
proj, = ax.plot3D(xs=X_pos, ys=Y_pos, zs=Z_pos ,c= '#9DDFDD')
ax.plot3D(xs=X_pos, ys=Y_pos, zs=Z_pos ,c= '#9DDFDD', linestyle = 'dotted')
cone, = ax.plot3D(x_2, y_2, z_2, linestyle='--', alpha = a, c=color)
ax.margins(x=0, y=-0.4)
x = np.array(X_pos)
y = np.array(Y_pos)
z = np.array(Z_pos)


x_2 = np.squeeze(np.array(X_2))
y_2 = np.squeeze(np.array(Y_2))
z_2 = np.squeeze(np.array(Z_2))

x_3 = np.squeeze(np.array(X_arrow))
y_3 = np.squeeze(np.array(Y_arrow))
z_3 = np.squeeze(np.array(Z_arrow))



ax.set_xlim(0, 50000)

ax.set_ylim(0, 50000)

ax.set_zlim(0, 20000)

X_2 = np.array(X_2)
Y_2 = np.array(Y_2)
Z_2 = np.array(Z_2)
def animate_projection(i):
    proj.set_data(x[-i:], y[-i:])
    proj.set_3d_properties(z[-i:])
    #cone.set_data(x_2[:i], y_2[:i])
    #cone.set_3d_properties(z_2[:i])
    #doa.set_data(x_3[:i], y_3[:i])
    #doa.set_3d_properties(z_3[:i])
    ax.set_xlim(0, 50000)
    ax.set_ylim(0, 50000)
    ax.set_zlim(0, 20000)
    ax.set_title("Trajectory Simulation of the Event - t({})s".format(i))



def update(i):
    # Update the plotted data for the current frame
    ax.set_xlim(0, 50000)
    ax.set_ylim(0, 50000)
    ax.set_zlim(0, 20000)
    ax.plot3D(X_2[:i, 0], Y_2[:i, 1], Z_2[:i, 2])

# create an animation using the animate function and
# specify the number of frames and the length of the animation
anim = FuncAnimation(fig, animate_projection, frames=100, interval=1000, repeat = True)
anim_2 = FuncAnimation(fig, update, frames=100, interval=1000)

# show the animated 3D graph'''
