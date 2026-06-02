import requests

url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=csv"

response = requests.get(url)

with open("satellites.csv", "w", encoding="utf-8") as file:
    file.write(response.text)

print("Satellite data downloaded successfully!")