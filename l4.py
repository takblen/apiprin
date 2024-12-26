import requests

def find_city(cities):
    res = None
    min_latitude = float("inf")

    for city in cities:
        geocode_url = f"https://geocode-maps.yandex.ru/1.x/"
        geocode_params = {
            "geocode": city,
            "format": "json",
            "apikey": "9502d292-d0b6-4177-bbb7-1c6e81c89ce8"
        }
        response = requests.get(geocode_url, params=geocode_params).json()
        try:
            point = response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
            lon, lat = map(float, point.split())
            if lat < min_latitude:
                res = city
                min_latitude = lat
        except (KeyError, IndexError):
            print(f"Не удалось найти координаты для города {city}.")

    print(f"Самый южный город: {res}")

find_city(["Москва", "Сочи", "Воронеж"])