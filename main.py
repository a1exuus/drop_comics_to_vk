import requests
from dotenv import load_dotenv
import os

load_dotenv()

url = 'https://xkcd.com/353/info.0.json'
response = requests.get(url)
response_json = response.json()
response.raise_for_status()
img_url = response_json['img']
print(response_json['alt'])
response = requests.get(img_url)
response.raise_for_status()
with open('comics.png', 'wb') as file:
    file.write(response.content)