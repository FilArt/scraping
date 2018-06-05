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
Перейти на сайт https://conda.io/miniconda.html и скачать версию conda для своей системы.
Conda должна быть выбрана в качестве интерпретатора по умолчанию. Во время установки просто не снимайте галку с соотв-го пункта.
Запускаем Anaconda Prompt(первой вылезет при поиске через Пуск).
Устанавливаем Scrapy и сопроводительные для него пакеты:
#### <b>conda install -c conda-forge scrapy</b>
Наконец создаем пустую папку, где будет храниться скрипт, копируем путь этой папке и в Anaconda Prompt выполняем команду
#### <b>cd [path_to_script]</b>
Создаем в этой папке scrapy-проект:
#### <b>scrapy startproject books</b>
Переходим в папку с пауками:
#### <b>cd books/books/spiders
#### explorer books/books/spiders
Создаем здесь файл books_spider.py и копируем в него содержимое файла
[books_spyder.py](https://github.com/FilArt/scraping/blob/master/books_spider.py)
Запускаем скрипт:
#### <b>scrapy crawl books</b>
