import math
from math import radians, cos, sin, sqrt, atan2
import re
import pygeodesy
from matplotlib import pyplot as plt
from pyproj import Transformer
import mgrs
import numpy as np


sensor_posts = []
def latlon_to_cartesian(ref_latlon, latlon_list):
    # Convert reference lat-lon point to radians
    ref_lat = radians(ref_latlon[0])
    ref_lon = radians(ref_latlon[1])

    # Calculate reference Cartesian coordinates
    ref_x = cos(ref_lat) * cos(ref_lon)
    ref_y = cos(ref_lat) * sin(ref_lon)
    ref_z = 0

    # Convert lat-lon coordinates to Cartesian coordinates
    cartesian_coords = []
    for latlon in latlon_list:
        lat = radians(latlon[0])
        lon = radians(latlon[1])

        # Calculate distance between lat-lon points in meters
        d_lat = lat - ref_lat
        d_lon = lon - ref_lon
        a = sin(d_lat/2)**2 + cos(ref_lat) * cos(lat) * sin(d_lon/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1-a))
        d = pygeodesy.haversine(ref_latlon[0], ref_latlon[1],latlon[0], latlon[1], radius=6371008.77141, wrap=False)
        theta = pygeodesy.bearing(ref_latlon[0], ref_latlon[1], latlon[0], latlon[1], wrap=False)
        # Calculate corresponding Cartesian coordinates
        x = d * cos(math.radians(360-theta))
        y = d * sin(math.radians(360-theta))
        z = 0
        sensor_posts.append([x,y,z])
    print(sensor_posts)

def mgrs_to_latlon(ref_mgrs, mgrs_list):

    # Convert reference MGRS coordinate to lat/lon
    ref_latlon = mgrs.MGRS().toLatLon(ref_mgrs[0])

    # Create transformer for converting lat/lon to ECEF coordinates
    transformer = Transformer.from_crs("epsg:4326", "epsg:4978")

    # Convert reference lat/lon to ECEF coordinates

    # Convert each MGRS coordinate to lat/lon
    latlon_list = [mgrs.MGRS().toLatLon(mgrs_coord) for mgrs_coord in mgrs_list]
    latlon_to_cartesian(ref_latlon,latlon_list)


import math

def find_angle(x1, x2, y1, y2):
    # Calculate the slope of the line
    slope = (y2 - y1) / (x2 - x1)

    # Calculate the angle between the line and the x-axis
    angle = math.atan(slope)

    # Convert the angle from radians to degrees
    angle_degrees = math.degrees(angle)
    print(180-angle_degrees)

find_angle(2.7011,   7.8941,   2.6590,   8.7897)
