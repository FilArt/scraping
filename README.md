# Скрипт на Python3 парсящий названия книг с сайта http://books.toscrape.com

## Инструкция по запуску
### Требования: python3, модуль Scrapy.
### Для linux:
1. Скопировать в буфер обмена код файла
[books_spyder.py](https://github.com/FilArt/scraping/blob/master/books_spider.py)
2. Создать пустую папку и открыть ее в терминале.
3. Выполнить следующие в терминале:
        <p><b>scrapy startproject asd</b></p>
        <p><b>cd asd/asd/spiders</b></p>
        <p><b>xsel -b > asd.py</b></p>
        <p><b>scrapy crawl books</b></p>
        <p><b>vi books.txt</b></p>

### Для windows:
...........................
