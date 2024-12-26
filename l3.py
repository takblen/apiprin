import requests

def get_satellite_image(coords, filename="satellite.png"):
    url = f"https://static-maps.yandex.ru/1.x/"
    params = {
        "ll": f"{coords[1]},{coords[0]}",
        "z": 16,
        "size": "650,450",
        "l": "sat",
        "apikey": "9502d292-d0b6-4177-bbb7-1c6e81c89ce8"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Снимок создан: {filename}")
    else:
        print("Не удалось выполнить программу.")

get_satellite_image((55, 37))