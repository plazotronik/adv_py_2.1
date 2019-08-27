#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests


URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
KEY_API = 'trnsl.1.1.20190704T182934Z.17f33d8db55385c6.e6d41260c9ccabfba9197455fd6d6679fec9bf38'
LNG_OUT = 'RU'


def translate(text, lang_in='en', lang_out=LNG_OUT, key=KEY_API):
    '''
    translation input text
    https://translate.yandex.net/api/v1.5/tr.json/translate
     ? [key=<API-ключ>]
     & [text=<переводимый текст>]
     & [lang=<направление перевода>]
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :return:
    translated text
    '''
    params = {
        'key': key,
        'text': text,
        'lang': '{}-{}'.format(lang_in, lang_out).lower(),
    }
    response = requests.get(URL, params=params)
    return response.json()


if __name__ == '__main__':
    result = translate('Hello')
    print(''.join(result['text']))