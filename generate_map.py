import json
import folium, io
from PyQt5 import QtWebEngineWidgets
from folium.plugins import Draw, MousePosition, MeasureControl,MiniMap
import calculateParameters
import calculateParameters as Cp
import mainWindow

temp_coordinates = []
temp_cumulative = []
cumulative_coordinates = []
last_list_float = []
last_list = []
abc=[]
lat_temp=0
long_temp=0

def createMainMap(layout):
    mainmap = folium.Map(location=(51.983225, 5.900198), control_scale=True,
                         tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
                         attr='Esri', name='Esri Satellite', overlay=False, control=True, zoom_start=3,
                       detect_retina=True)

    mainmap.add_child(MiniMap())

    formatter = "function(num) {return L.Util.formatNum(num, 6) + ' º ';};"
    MousePosition(position="topright", separator=" | ", empty_string="NaN", lat_first=True, num_digits=20,
                  prefix="Coordinates:",
                  lat_formatter=formatter, lng_formatter=formatter, ).add_to(mainmap)

    mainmap.add_child(MeasureControl())

    draw = Draw(draw_options={'polyline': False, 'rectangle': False, 'polygon': False, 'circle': False,
                          'marker': False, 'circlemarker': True},edit_options={'edit': False})
    mainmap.add_child(draw)

    view = QtWebEngineWidgets.QWebEngineView()
    view.setContentsMargins(2, 5, 28, 50)
    view.setFixedSize(1205, 781)
    page = WebEnginePage(view)
    view.setPage(page)
    data = io.BytesIO()
    mainmap.save(data, close_file=False)
    view.setHtml(data.getvalue().decode())
    layout.addWidget(view)

def updateSeconder(layout):
    mainmap = folium.Map(location=(float(Cp.actual_sensor_coord[0][0]), float(Cp.actual_sensor_coord[0][1])), control_scale=True,
                         tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
                         attr='Esri', name='Esri Satellite', overlay=False, control=True, zoom_start=13,
                         detect_retina=True)

    mainmap.add_child(MiniMap())

    formatter = "function(num) {return L.Util.formatNum(num, 6) + ' º ';};"
    MousePosition(position="topright", separator=" | ", empty_string="NaN", lat_first=True, num_digits=20,
                  prefix="Coordinates:",
                  lat_formatter=formatter, lng_formatter=formatter, ).add_to(mainmap)

    mainmap.add_child(MeasureControl())

    draw = Draw(draw_options={'polyline': False, 'rectangle': False, 'polygon': False, 'circle': False,
                              'marker': False, 'circlemarker': True}, edit_options={'edit': False})
    mainmap.add_child(draw)

    for sensor in mainWindow.imported_sensor_coords:
        for k in sensor:
            folium.Marker(location=k, icon=folium.features.CustomIcon('Transparent_icon_sensor.png', icon_size=(19, 22))).add_to(mainmap)
    for event in mainWindow.imported_events:
        folium.Marker(location=event[1], icon=folium.features.CustomIcon('Transparent_icon_artillery.png', icon_size=(20, 13)),
                      popup=(event[0])).add_to(
            mainmap)
        folium.Marker(location=event[3],
                      icon=folium.features.CustomIcon('Transparent_impact_point.png', icon_size=(20, 14)),
                      popup=(event[2])).add_to(
            mainmap)

    for i in Cp.actual_sensor_coord:
        folium.Marker(location=i, icon=folium.features.CustomIcon('icon_sensor.png', icon_size=(21, 24)),
                      popup=(Cp.name_sensor[Cp.actual_sensor_coord.index(i)])).add_to(mainmap)

    view = QtWebEngineWidgets.QWebEngineView()
    view.setContentsMargins(2, 5, 28, 50)
    view.setFixedSize(1205, 781)
    page = WebEnginePage(view)
    view.setPage(page)
    data = io.BytesIO()
    mainmap.save(data, close_file=False)
    view.setHtml(data.getvalue().decode())
    layout.addWidget(view)

def updateLaunchMap(layout):
    mainmap = folium.Map(location=(float(Cp.actual_launch_coord[-1][0]), float(Cp.actual_launch_coord[-1][1])), control_scale=True,
                         tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
                         attr='Esri', name='Esri Satellite', overlay=False, control=True, zoom_start=13,
                         detect_retina=True)

    mainmap.add_child(MiniMap())

    formatter = "function(num) {return L.Util.formatNum(num, 6) + ' º ';};"
    MousePosition(position="topright", separator=" | ", empty_string="NaN", lat_first=True, num_digits=20,
                  prefix="Coordinates:",
                  lat_formatter=formatter, lng_formatter=formatter, ).add_to(mainmap)

    mainmap.add_child(MeasureControl())

    draw = Draw(draw_options={'polyline': False, 'rectangle': False, 'polygon': False, 'circle': False,
                              'marker': False, 'circlemarker': True}, edit_options={'edit': False})
    mainmap.add_child(draw)

    for sensor in mainWindow.imported_sensor_coords:
        for k in sensor:
            folium.Marker(location=k, icon=folium.features.CustomIcon('Transparent_icon_sensor.png',  icon_size=(19, 22))).add_to(mainmap)
    for event in mainWindow.imported_events:
        folium.Marker(location=event[1], icon=folium.features.CustomIcon('Transparent_icon_artillery.png', icon_size=(20, 13)),
                      popup=(event[0])).add_to(
            mainmap)
        folium.Marker(location=event[3],
                      icon=folium.features.CustomIcon('Transparent_impact_point.png',  icon_size=(20, 14)),
                      popup=(event[2])).add_to(
            mainmap)

    for j in Cp.actual_launch_coord:
        folium.Marker(location=j, icon=folium.features.CustomIcon('icon_artillery.png', icon_size=(20, 13)),
                      popup=(Cp.name_launch[Cp.actual_launch_coord.index(j)])).add_to(mainmap)
    if len(calculateParameters.actual_impact_coord) > 0:
        for j in Cp.actual_impact_coord:
            folium.Marker(location=j, icon=folium.features.CustomIcon('impact_point.png', icon_size=(20, 14)),
                          popup=(Cp.name_impact[Cp.actual_impact_coord.index(j)])).add_to(mainmap)
    else:
        pass

    view = QtWebEngineWidgets.QWebEngineView()
    view.setContentsMargins(2, 5, 28, 50)
    view.setFixedSize(1205, 781)
    page = WebEnginePage(view)
    view.setPage(page)
    data = io.BytesIO()
    mainmap.save(data, close_file=False)
    view.setHtml(data.getvalue().decode())
    layout.addWidget(view)

def updateImpactMap(layout):
    mainmap = folium.Map(location=(float(Cp.actual_impact_coord[-1][0]), float(Cp.actual_impact_coord[-1][1])), control_scale=True,
                         tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
                         attr='Esri', name='Esri Satellite', overlay=False, control=True, zoom_start=13,
                         detect_retina=True)

    mainmap.add_child(MiniMap())

    formatter = "function(num) {return L.Util.formatNum(num, 6) + ' º ';};"
    MousePosition(position="topright", separator=" | ", empty_string="NaN", lat_first=True, num_digits=20,
                  prefix="Coordinates:",
                  lat_formatter=formatter, lng_formatter=formatter, ).add_to(mainmap)

    mainmap.add_child(MeasureControl())

    draw = Draw(draw_options={'polyline': False, 'rectangle': False, 'polygon': False, 'circle': False,
                              'marker': False, 'circlemarker': True}, edit_options={'edit': False})
    mainmap.add_child(draw)

    for sensor in mainWindow.imported_sensor_coords:
        for k in sensor:
            folium.Marker(location=k, icon=folium.features.CustomIcon('Transparent_icon_sensor.png', icon_size=(19, 22))).add_to(mainmap)
    for event in mainWindow.imported_events:
        folium.Marker(location=event[1], icon=folium.features.CustomIcon('Transparent_icon_artillery.png', icon_size=(20, 13)),
                      popup=(event[0])).add_to(
            mainmap)
        folium.Marker(location=event[3],
                      icon=folium.features.CustomIcon('Transparent_impact_point.png', icon_size=(20, 14)),
                      popup=(event[2])).add_to(
            mainmap)

    for j in Cp.actual_impact_coord:
        folium.Marker(location=j, icon=folium.features.CustomIcon('impact_point.png', icon_size=(20, 14)),
                      popup=(Cp.name_impact[Cp.actual_impact_coord.index(j)])).add_to(mainmap)
    if len(calculateParameters.actual_launch_coord) > 0:
        for j in Cp.actual_launch_coord:
            folium.Marker(location=j, icon=folium.features.CustomIcon('icon_artillery.png', icon_size=(20, 13)),
                          popup=(Cp.name_launch[Cp.actual_launch_coord.index(j)])).add_to(mainmap)
    else:
        pass

    view = QtWebEngineWidgets.QWebEngineView()
    view.setContentsMargins(2, 5, 28, 50)
    view.setFixedSize(1205, 781)
    page = WebEnginePage(view)
    view.setPage(page)
    data = io.BytesIO()
    mainmap.save(data, close_file=False)
    view.setHtml(data.getvalue().decode())
    layout.addWidget(view)


def createUpdatedMap(layout):

    if last_list[-1]==Cp.actual_sensor_coord[-1]:
        mainmap = folium.Map(location=(Cp.actual_sensor_coord[-1][0],Cp.actual_sensor_coord[-1][1]), control_scale=True,
                             tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
                             attr='Esri', name='Esri Satellite', overlay=False, control=True, zoom_start=13,
                             detect_retina=True)
    elif last_list[-1]==Cp.actual_launch_coord[-1]:
        mainmap = folium.Map(location=(Cp.actual_launch_coord[-1][0],Cp.actual_launch_coord[-1][1]), control_scale=True,
                             tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
                             attr='Esri', name='Esri Satellite', overlay=False, control=True, zoom_start=13,
                             detect_retina=True)
    elif last_list[-1] == Cp.actual_impact_coord[-1]:
        mainmap = folium.Map(location=(Cp.actual_impact_coord[-1][0], Cp.actual_impact_coord[-1][1]),
                             control_scale=True,
                             tiles="https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}",
                             attr='Esri', name='Esri Satellite', overlay=False, control=True, zoom_start=13,
                             detect_retina=True)

    mainmap.add_child(MiniMap())

    formatter = "function(num) {return L.Util.formatNum(num, 6) + ' º ';};"
    MousePosition(position="topright", separator=" | ", empty_string="NaN", lat_first=True, num_digits=20,
                  prefix="Coordinates:",
                  lat_formatter=formatter, lng_formatter=formatter, ).add_to(mainmap)

    mainmap.add_child(MeasureControl())

    draw = Draw(draw_options={'polyline': False, 'rectangle': False, 'polygon': False, 'circle': False,
                              'marker': False, 'circlemarker': True}, edit_options={'edit': False})
    mainmap.add_child(draw)

    sensor_icon = folium.features.CustomIcon('icon_sensor.png', icon_size=(21, 24))
    sensor_icon_2 = folium.features.CustomIcon('icon_sensor.png', icon_size=(21, 24))
    sensor_icon_3 = folium.features.CustomIcon('icon_sensor.png', icon_size=(21, 24))
    launch_icon = folium.features.CustomIcon('icon_artillery.png', icon_size=(20, 13))
    impact_icon = folium.features.CustomIcon('impact_point.png', icon_size=(30, 30))

    for i in Cp.actual_sensor_coord:
        folium.Marker(location=i,icon = folium.features.CustomIcon('icon_sensor.png', icon_size=(21, 24)),
                      popup = (Cp.name_sensor[Cp.actual_sensor_coord.index(i)])).add_to(mainmap)
    for j in Cp.actual_launch_coord:
        folium.Marker(location=j, icon=folium.features.CustomIcon('icon_artillery.png', icon_size=(20, 13)),
                      popup=(Cp.name_launch[Cp.actual_launch_coord.index(j)])).add_to(mainmap)
    for k in Cp.actual_impact_coord:
        folium.Marker(location=k, icon=folium.features.CustomIcon('impact_point.png', icon_size=(20, 14)),
                      popup = (Cp.name_impact[Cp.actual_impact_coord.index(k)])).add_to(mainmap)

    view = QtWebEngineWidgets.QWebEngineView()
    view.setContentsMargins(2, 5, 28, 50)
    view.setFixedSize(1205, 781)
    page = WebEnginePage(view)
    view.setPage(page)
    data = io.BytesIO()
    mainmap.save(data, close_file=False)
    view.setHtml(data.getvalue().decode())
    layout.addWidget(view)

def createSmallMap(layout):
    mainmap = folium.Map(location=(float(mainWindow.cum_sensor_coord[-1][0][0]), float(mainWindow.cum_sensor_coord[-1][0][1])),
                         control_scale=True, tiles="Stamen Terrain", zoom_start=10,detect_retina=True)

    formatter = "function(num) {return L.Util.formatNum(num, 6) + ' º ';};"
    MousePosition(position="topright", separator=" | ", empty_string="NaN", lat_first=True, num_digits=20,
                  prefix="Coordinates:",
                  lat_formatter=formatter, lng_formatter=formatter, ).add_to(mainmap)

    mainmap.add_child(MeasureControl())

    for sensor in mainWindow.imported_sensor_coords:
        for k in sensor:
            folium.Marker(location=k,
                          icon=folium.features.CustomIcon('Transparent_icon_sensor.png', icon_size=(19, 22))).add_to(
                mainmap)
    for event in mainWindow.imported_events:
        folium.Marker(location=event[1],
                      icon=folium.features.CustomIcon('Transparent_icon_artillery.png', icon_size=(20, 13)),
                      popup=(event[0])).add_to(
            mainmap)
        folium.Marker(location=event[3],
                      icon=folium.features.CustomIcon('Transparent_impact_point.png', icon_size=(20, 14)),
                      popup=(event[2])).add_to(
            mainmap)
        folium.PolyLine([event[1],event[3]]).add_to(mainmap)

    view = QtWebEngineWidgets.QWebEngineView()
    view.setContentsMargins(2, 2, 28, 50)
    view.setFixedSize(520,520)
    page = WebEnginePage(view)
    view.setPage(page)
    data = io.BytesIO()
    mainmap.save(data, close_file=False)
    view.setHtml(data.getvalue().decode())
    layout.addWidget(view)

class WebEnginePage(QtWebEngineWidgets.QWebEnginePage):
    def javaScriptConsoleMessage(self, level, msg, line, sourceID):
        global last_list
        global lat_temp
        global long_temp
        global temp_cumulative
        coords_dict = json.loads(msg)
        lon = coords_dict['geometry']['coordinates'][0]
        lat = coords_dict['geometry']['coordinates'][1]
        lat_temp = lat
        long_temp = lon
        temp_coordinates.append(lat)
        temp_coordinates.append(lon)
        temp_cumulative.append(temp_coordinates)



