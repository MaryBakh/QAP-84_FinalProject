import json

import requests
# from requests_toolbelt.multipart.encoder import MultipartEncoder
from common import CODE_HEADER, CODE_SIZE


class RandomMailApi:
    """Получение рандомного мэйла для регистрации"""

    def get_mail(self):
        # Запрос к https://www.1secmail.com/api/v1/ для получения рандомного email
        res = requests.get('https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1')
        status = res.status_code
        mail = ''
        if status == 200:
            try:
                result = res.json()
                mail = result[0]
            except json.decoder.JSONDecodeError:
                print("Error parse: ", res.text)
                mail = ""
        else:
            print("Error request to mail api: ", status)
            mail = ""

        return mail

    def get_message_id(self, email=''):
        # Запрос к найденному email и получение id сообщения
        # Разделяем email на логин и домен
        elems = email.split("@")

        # Узнаем id пришедшего письма
        res = requests.get(
            'https://www.1secmail.com/api/v1/?action=getMessages&login={0}&domain={1}'.format(elems[0], elems[1]))
        status = res.status_code

        print('3333', status)

        id = 0
        if (status == 200):
            try:
                result = res.json()
                id = result[0]['id']
            except Exception as e:
                print("Error parse: ", e)
                id = 0
        else:
            print("Error request to mail: ", status)
            id = 0

        print('4444', id)
        return id

    def get_confirmation_code(self, email='', id=0):
        # Запрос к email, поиск сообщения по id  и получение из него кода подтверждения"""
        # Разделяем email на логин и домен
        elems = email.split("@")

        # Находим сообщение в ящике по id и извлекаем код подтверждения
        res = requests.get(
            'https://www.1secmail.com/api/v1/?action=readMessage&login={0}&domain={1}&id={2}'.format(elems[0], elems[1], id))
        status = res.status_code

        print('5555', status)

        code = ''
        if (status == 200):
            try:
                result = res.text
                found = result.find(CODE_HEADER)
                if found != -1:
                    beg = found + len(CODE_HEADER)
                    end = beg + CODE_SIZE
                    code = result[beg:end]
                else:
                    print("Code not found: ", res.text)
                    code = ''
            except json.decoder.JSONDecodeError:
                print("Error parse: ", res.text)
                code = ''
        else:
            print("Error request to mail: ", status)
            code = ''

        return code


