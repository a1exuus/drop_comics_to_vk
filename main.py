import requests
from dotenv import load_dotenv
from os import getenv, remove
import telegram
from random import randint


def get_comics(url):
    response = requests.get(url)
    response.raise_for_status()
    comics_content = response.json()
    image = requests.get(comics_content['img'])
    image.raise_for_status()
    return image.content, comics_content['alt']


def publish_comics(chat_id, alt):
    bot.send_photo(chat_id=chat_id, photo=open('img/comics.png', 'rb'), caption=alt)
    remove('img/comics.png')


if __name__ == '__main__':
    load_dotenv()
    ordinal_number = randint(0, 3018)
    chat_id = getenv('TG_CHANNEL_CHAT_ID')
    bot_token = getenv('TG_BOT_TOKEN')
    bot = telegram.Bot(token=bot_token)
    url = f'https://xkcd.com/{ordinal_number}/info.0.json'
    image, alt = get_comics(url)
    with open('img/comics.png', 'wb') as file:
        file.write(image)
    publish_comics(chat_id, alt)