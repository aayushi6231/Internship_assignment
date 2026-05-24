import requests

country = input("Enter country name: ")

url = f"https://restcountries.com/v3.1/name/{country}"

data = requests.get(url).json()

print("Details")

print("Country:", data[0]['name']['common'])
print("Capital:", data[0]['capital'][0])
print("Population:", data[0]['population'])
print("Region:", data[0]['region'])