import subprocess
import os
import scipy.io
import oct2py
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.interpolate import interp1d
import coordinate_cartesian

oc = oct2py.Oct2Py()

sensor_positions = []
def run_octave_function(m_file, function_name, *args):
    # Build the command to run the Octave function
    cmd = ['octave', '--eval', f'{function_name}({",".join(args)}); save my_data.mat -mat']

    # Change the current directory to the location of the .m file
    # so that Octave can find it
    with open(m_file, 'r') as f:
        subprocess.run(cmd, cwd=os.path.dirname(os.path.abspath(f.name)), capture_output=True)

run_octave_function('forward_model/fwdCompute.m','[resSE , resSW] = fwdCompute.exampleSimple')

data = scipy.io.loadmat('forward_model\my_data.mat')

validity_SW = data['resSW']['valid']
toa_SW = data['resSW']['toa']
doa_SW = data['resSW']['doa']
level_SW = data['resSW']['lev']

validity_SE = data['resSE']['valid']
toa_SE = data['resSE']['toaP']
doa_SE = data['resSE']['doaP']
impact_SE = data['resSE']['impact']
level_SE = data['resSE']['lev']
time_of_flight = data['resSE']['ToF']
debug = data['resSE']['debug']

proj_F = debug[0][0][0][0][0][0]['projF']
proj_F_N = proj_F['N'][0][0]
proj_F_x = proj_F['x'][0][0]
proj_F_vel = proj_F['vel'][0][0]
proj_F_t = proj_F['t'][0][0]
proj_F_state = proj_F['state'][0][0]
proj_F_T = proj_F['T'][0][0]
proj_F_wind = proj_F['wind'][0][0]
proj_F_c0 = proj_F['c0'][0][0]
proj_F_velRel = proj_F['velRel'][0][0]
proj_F_MAbs = proj_F['MAbs'][0][0]
proj_F_MRel = proj_F['MRel'][0][0]
proj_F_relLev0CPA = proj_F['relLev0CPA'][0][0]

proj_S = debug[0][0][0][0][0][0]['projs']
proj_S_valid = proj_S['valid']
proj_S_t = proj_S['t']
proj_S_x = proj_S['x']
proj_S_vel = proj_S['vel']
proj_S_T = proj_S['T']
proj_S_N = proj_S['N']
proj_S_wind = proj_S['wind']
proj_S_relLev0CPA = proj_S['relLev0CPA']

ray_S = debug[0][0][0][0][0][0]['rays']
ray_S_valid = ray_S['valid']
ray_S_t = ray_S['t']
ray_S_x = ray_S['x']
ray_S_p = ray_S['p']
ray_S_T = ray_S['T']
ray_S_N = ray_S['N']
ray_S_relLev_TravD = ray_S['relLev_TravD']

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot3D(proj_F_x[0], proj_F_x[1], proj_F_x[2])
ax.scatter(proj_F_x[0][-1], proj_F_x[1][-1], proj_F_x[2][-1], c = 'red')
coordinate_cartesian.mgrs_to_latlon(['35UMA3241096412'],['35UMB2850403535','35UMB2899003931','35UMB2626403309',
                                    '35UMB2496603017','35UMB2425402105', '35UMA2209199292','35UMB2273302010',
                                    '35UMB2195500272','35UMB2371404445'])

sensor_positions = coordinate_cartesian.sensor_posts
sensor_names = ['S2','S1','S3','S4','S5','S9','S6','S7','S8']

for j in range(len(sensor_positions)):
    ax.scatter(sensor_positions[j][0],sensor_positions[j][1], sensor_positions[j][2], c= 'blue', s=10)
    ax.text(sensor_positions[j][0],sensor_positions[j][1], sensor_positions[j][2], sensor_names[j])
for i in range(len(ray_S_valid[0])):
    if ray_S_valid[0][i][0][0] == 0:
        pass
    else:
        ax.plot3D(ray_S_x[0][i][0], ray_S_x[0][i][1], ray_S_x[0][i][2], linestyle = 'dotted')


ax.autoscale_view()

proj, = ax.plot3D(xs=proj_F_x[0], ys=proj_F_x[1], zs=proj_F_x[2] ,c= '#9DDFDD')
x = np.array(proj_F_x[0])
y = np.array(proj_F_x[1])
z = np.array(proj_F_x[2])


def draw_line_3d(x1, y1, z1, R, x, y, z):
    f = interp1d(x, y, kind='cubic')
    y_interp = f(x1)
    g = interp1d(x, z, kind='cubic')
    z_interp = g(x1)

    # Calculate the slope of the curve at (x1, y1, z1)
    dx = x[1] - x[0]
    dy = y_interp - y1
    dz = z_interp - z1
    slope = np.array([dx, dy, dz])

    # Normalize the slope
    slope = slope / np.linalg.norm(slope)

    # Calculate a vector perpendicular to the slope and the Z axis
    normal = np.cross(np.array([0, 0, 1]), slope)

    # Normalize the normal vector
    normal = normal / np.linalg.norm(normal)

    # Calculate the end points of the tangent line
    x2 = x1 + R * slope[0]
    y2 = y1 + R * slope[1]
    z2 = z1 + R * slope[2]
    x_tangent = np.array([x1, x2])
    y_tangent = np.array([y1, y2])
    z_tangent = np.array([z1, z2])

    # Calculate the end points of a line perpendicular to the tangent line
    x3 = x1 + R * normal[0]
    y3 = y1 + R * normal[1]
    z3 = z1 + R * normal[2]
    x_normal = np.array([x1, x3])
    y_normal = np.array([y1, y3])
    z_normal = np.array([z1, z3])

    # Calculate the points on the circle
    num_points = 36
    theta = np.linspace(0, 2 * np.pi, num_points)
    x_circle = x1 + R * np.cos(theta) * normal[0] + R * np.sin(theta) * slope[0]
    y_circle = y1 + R * np.cos(theta) * normal[1] + R * np.sin(theta) * slope[1]
    z_circle = z1 + R * np.cos(theta) * normal[2] + R * np.sin(theta) * slope[2]

    ax.plot(x, y, z, label='Curve')
    ax.plot(x_tangent, y_tangent, z_tangent, label='Tangent Line')
    ax.plot(x_circle, y_circle, z_circle, label='Circle')

    ax.legend()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

def animate_projection(i):
    proj.set_data(x[:i], y[:i])
    proj.set_3d_properties(z[:i])
    #cone.set_data(x_2[:i], y_2[:i])
    #cone.set_3d_properties(z_2[:i])
    #doa.set_data(x_3[:i], y_3[:i])
    #doa.set_3d_properties(z_3[:i])
    #ax.set_xlim(0, 50000)
    #ax.set_ylim(0, 50000)
    #ax.set_zlim(0, 20000)
    ax.set_title("Trajectory Simulation of the Event - t({})s".format(i))


# create an animation using the animate function and
# specify the number of frames and the length of the animation
#anim = FuncAnimation(fig, animate_projection, frames=500, interval=10, repeat = True)

ax.set_xlim(0, 10000)
ax.set_ylim(0, 12000)
ax.set_zlim(0, 5000)
plt.show()


