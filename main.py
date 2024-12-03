import requests
from dotenv import load_dotenv
from os import environ, remove
from os.path import join
import telegram
from random import randint


ORDINAL_NUMBER = randint(0, 3018)


def get_comics(url):
    response = requests.get(url)
    response.raise_for_status()
    comics_content = response.json()
    image = requests.get(comics_content['img'])
    image.raise_for_status()
    return image.content, comics_content['alt']


def publish_comics(chat_id, alt):
    with open('img/comics.png', 'rb') as photo:
        bot.send_photo(chat_id=chat_id, photo=photo, caption=alt)


if __name__ == '__main__':
    load_dotenv()
    chat_id = environ['TG_CHANNEL_CHAT_ID']
    bot_token = environ['TG_BOT_TOKEN']
    bot = telegram.Bot(token=bot_token)
    comics_path = join('img', 'comics.png')
    url = f'https://xkcd.com/{ORDINAL_NUMBER}/info.0.json'
    try:
        image, alt = get_comics(url)
        with open('img/comics.png', 'wb') as file:
            file.write(image)
        publish_comics(chat_id, alt)
        raise ValueError("Проверка исключения")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        try:
            remove('img/comics.png')
        except FileNotFoundError:
            pass
