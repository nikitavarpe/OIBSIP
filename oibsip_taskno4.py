import requests

def get_weather(city):
    api_key = "eeb29809d791543b2c0cc817722e8066"
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(base_url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        weather_desc = data["weather"][0]["description"]
        temp = main["temp"]
        humidity = main["humidity"]

        return f"Temperature: {temp}°C\nHumidity: {humidity}%\nDescription: {weather_desc.capitalize()}"
    else:
        return "City not found."


city = input("Enter city name: ")
weather_info = get_weather(city)
print(weather_info)


