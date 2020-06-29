import folium 
import pandas

data=pandas.read_csv('metroson.csv',encoding="utf-8")

LAT=list(data['LAT'])
LON=list(data['LON'])
name=list(data['NAME'])
picture=list(data['picture'])

fg=folium.FeatureGroup('my map')
fg.add_child(folium.GeoJson(data=(open('m1-m2.json','r',encoding='utf-8').read())))


 
for lt,ln,nm,pic in zip(LAT,LON,name,picture):
 	fg.add_child(folium.Marker(location=[lt,ln],popup="<b>Station Name: </b>"+nm+"<br> <img src="+pic+" height=250 width=400>",icon=folium.Icon(color='red')))

#height=142 width=290
map=folium.Map(location=[39.93495537428379,32.74075984954834],zoom_start=11)


map.add_child(fg)
map.save('Gülsüm&Gizem.html')



