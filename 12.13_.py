import folium
import webbrowser
latitude = 48.858497136405795 # 위도 
longitude =  2.2944383831278743 # 경도
place = folium.Map(location=[latitude, longitude], zoom_start=100) # 시작 위치, 클수록 확대

place_name = "동부중학교"
latitude = 37.5354590419139
longitude = 127.20255052514715
marker = folium.Marker(location=[latitude, longitude], popup= place_name, icon=folium.Icon(color='red'))


marker.add_to(place)

place.save('map.html')
webbrowser.open_new("map.html")
