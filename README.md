﻿# QAP-84_FinalProject

Для запуска тестов:
 1) Установить библиотеки:
    pip install requests
    pip install selenium
 
 2) Для запуска тестов:
     python -m pytest tests_main.py
Данные тесты испытывались в среде Python 3.8.5 c библиотеками pytest 7.2.0 и selenium 4.6.0, в данном случае 
нет необходимости дополнительно прописывать путь к драйверу Chrome

При работе в альтернативной среде может понадобиться:
1) скачать драйвер для своей версии Chrome с https://chromedriver.storage.googleapis.com/index.html
2) прописать путь для файла с драйвером Chrome в переменную CHROME_DRIVER_PATH файла common.py
