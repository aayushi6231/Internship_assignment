import requests

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=8e4c9c35d3848c06fa3059c7ced88227&units-metric"

data = requests.get(url).json()

print("\nWeather Details")

print("City:", data['name'])
print("Country:", data['sys']['country'])
print("Temperature:", data['main']['temp'], "°C")
print("Feels Like:", data['main']['feels_like'], "°C")
print("Humidity:", data['main']['humidity'], "%")
print("Pressure:", data['main']['pressure'])
print("Wind Speed:", data['wind']['speed'])
print("Weather:", data['weather'][0]['description'])