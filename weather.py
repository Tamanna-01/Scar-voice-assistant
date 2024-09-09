import requests

def get_weather(city_name):
    url = f"https://open-weather13.p.rapidapi.com/city/{city_name}"

    headers = {
        "X-RapidAPI-Key": "8fc338d5famsh94088b089c4ed96p1cee0cjsnb25cb8afbb4c",
        "X-RapidAPI-Host": "open-weather13.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    json_data = response.json()

    temperature = round(json_data["main"]["temp"], 1)
    description = json_data["weather"][0]["description"]

    return temperature, description
