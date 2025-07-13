import requests
import matplotlib.pyplot as plt
import seaborn as sns

API_KEY = 'a35330fb1e7dca09198d52b0735ab88b'  # your real key

cities = ['Chennai', 'Delhi', 'Mumbai', 'Kolkata', 'Bangalore']
temps = []

def get_current_temperature(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        temp = data['main']['temp']
        print(f"{city}: {temp}°C")  # ✅ Print temperature for each city
        return temp
    else:
        print(f"Error fetching data for {city} – {response.status_code}: {data.get('message', 'Unknown error')}")
        return None


# Collect data
for city in cities:
    temp = get_current_temperature(city)
    if temp is not None:
        temps.append({'city': city, 'temp': temp})

# Visualize
sns.set(style='whitegrid')
city_names = [entry['city'] for entry in temps]
temperatures = [entry['temp'] for entry in temps]

plt.figure(figsize=(8, 6))
sns.barplot(x=city_names, y=temperatures, hue=city_names, dodge=False, palette='coolwarm', legend=False)
plt.title('Current Temperature in Major Indian Cities')
plt.xlabel('City')
plt.ylabel('Temperature (°C)')
plt.tight_layout()
plt.show()
