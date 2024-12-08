import requests
from dotenv import load_dotenv
from pathlib import Path, PurePosixPath
from os import environ
import telegram
from random import randint
from get_amount_of_comicses import get_amount_of_comicses


def get_comics(url):
    response = requests.get(url)
    response.raise_for_status()
    comics_content = response.json()
    image = requests.get(comics_content['img'])
    image.raise_for_status()
    return image.content, comics_content['alt']


def publish_comics(chat_id, alt, path, bot):
    with open(path, 'rb') as photo:
        bot.send_photo(chat_id=chat_id, photo=photo, caption=alt)


def main():
    load_dotenv()
    chat_id = environ['TG_CHANNEL_CHAT_ID']
    bot_token = environ['TG_BOT_TOKEN']
    bot = telegram.Bot(token=bot_token)
    comics_dir = Path('img')
    comics_dir.mkdir(exist_ok=True)
    comics_path = comics_dir / 'comics.png'
    base_url = "https://xkcd.com"
    amount_of_comicses = get_amount_of_comicses('https://xkcd.com/info.0.json')
    ordinal_number = randint(0, amount_of_comicses)
    path = PurePosixPath(str(ordinal_number), "info.0.json")
    url = f"{base_url}/{path}"

    try:
        image, alt = get_comics(url)
        with open(comics_path, 'wb') as file:
            file.write(image)
        publish_comics(chat_id, alt, comics_path, bot)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    finally:
        if comics_path.exists():
            comics_path.unlink()


if __name__ == '__main__':
    main()
