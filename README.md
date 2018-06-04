# Скрипт на Python3 парсящий названия книг с сайта http://books.toscrape.com

## Инструкция по запуску
### Требования: python3, модуль Scrapy.
### Для linux:
1. Скопировать в буфер обмена код файл
[books_spyder.py](https://github.com/FilArt/scraping/blob/master/books_spider.py)
2. Создать пустую папку и открыть ее в терминале.
3. Выполнить следующие команды в терминале:
    scrapy startproject asd
    cd asd/asd
    vim asd.py
    i
    Shift+Insert
    Esc
    :wq
    scrapy crawl books

После этого создастся файл books.txt в котором будут записаны названия всех книжек с этого сайта.

### Для windows:
#### В разработке)
