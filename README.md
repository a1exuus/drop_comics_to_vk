# Публикация рандомных комиксов в Telegram

## Содержание

- [Вводная информация](#вводная-информация)
- [Начало работы](#начало-работы)
- [FAQ](#faq)
- [Цель проекта](#цель-проекта)

## Вводная информация

Проект использует [бота](https://t.me/dvmn_comics_bot) для публикации рандомных комиксов с сервиса [xkcd.com](https://xkcd.com/) в [Telegram канал](https://t.me/komiksy_dvmn). Бот был написан с помощью библиотеки [python-telegram-bot](https://python-telegram-bot.org/)

## Начало работы

Что-бы начать работу, вам нужно установить зависимости(библиотеки), которые требует для работы проект. Это можно сделать командой:

```pip3 install -r requirements.txt```

А также запишите чувствительные данные в файл `.env`(если не существует создайте его) и запишите туда `chat_id` вашего канала(узнать его можно переслав сообщение из вашего канала в [этот бот](https://t.me/getmyid_bot)) а также `token` вашего бота(узнать его можно после создания вашего бота в боте [BotFather](https://t.me/BotFather)). Запись должна выглядеть так для `chat_id`:

```TG_CHANNEL_CHAT_ID=*ваш chat_id*```

И так для `token`:

```TG_BOT_TOKEN=*ваш токен*```

## FAQ

### Почему я должен вводить сам токен бота?!

Запись токена бота - **обязательный процесс**. Но почему же?

Всё потому что разработчик, не хочет что-бы его токен использовали для каких-то злодеяний. Поэтому убирает его из своего проекта. Токены ***обязательны*** для выполнения программы полностью. Также вы можете не бояться что ваш токен украдут, так как программа выложена на [GitHub](https://github.com), то вы можете в любой удобный для вас момент убедиться что программа не содержит никакого вредоносного кода. Код открыт к чтению и может быть использован любым человеком.

## Цель проекта

Проект написан в образовательных целях для онлайн курсов по программированию школы при IT-компании Бюро20. [Узнать больше](https://dvmn.org/modules)