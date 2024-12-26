import folium
from geopy.distance import geodesic


def create_map(temp):
    map = folium.Map(location=coords[0], zoom_start=12)
    folium.PolyLine(coords, color="blue", weight=2.5, opacity=1).add_to(map)

    middle_index = len(temp) // 2
    middle_point = coords[middle_index]
    folium.Marker(location=middle_point, popup="Средняя точка").add_to(map)

    map.save("map.html")
    print("Карта пути создана: map.html")

    total_distance = 0
    for i in range(len(coords) - 1):
        total_distance += geodesic(coords[i], coords[i + 1]).meters
    return total_distance

coords = [(55, 37), (55.5, 37.5), (56, 38)]
print(f"Длина пути: {create_map(coords)}м")
