import requests
import json

ip = 'your ip address'  # replace with the IP address you want to look up

response = requests.get(f'https://ipapi.co/{ip}/json/')
result = response.json()

# Save the IP data to a JSON file
with open('ip_data.json', 'w') as file:
    json.dump(result, file)

print('IP data saved to ip_data.json')
