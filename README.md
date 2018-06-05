# Скрипт на Python3 парсящий названия книг с сайта http://books.toscrape.com

# Инструкция по запуску на Linux Ubuntu 18.04 и Windows 10.
## Для linux:
1. Скопировать в буфер обмена код файла
[books_spyder.py](https://github.com/FilArt/scraping/blob/master/books_spider.py)
2. Создать пустую папку и открыть ее в терминале.
3. Выполнить следующие команды в терминале:
        <p><b>scrapy startproject books</b></p>
        <p><b>cd books/books/spiders</b></p>
        <p><b>xsel -b > books.py</b></p>
        <p><b>scrapy crawl books</b></p>
        <p><b>vi books.txt</b></p>

## Для windows:
#### 1. Перейти на сайт https://conda.io/miniconda.html и скачать версию conda для своей системы. Conda должна быть выбрана в качестве интерпретатора по умолчанию. Во время установки просто не снимайте галку с соотв-го пункта.
#### 2. Запускаем Anaconda Prompt(первой вылезет при поиске через Пуск).
#### 3. Устанавливаем Scrapy и сопроводительные для него пакеты:
##### conda install -c conda-forge scrapy
#### 4. Далее создаем пустую папку, где будет храниться скрипт, и копируем путь к этой папке. После в Anaconda Prompt выполняем команду
##### cd [path_to_script]
#### Если не сработало, добавьте аргумент /d:
##### cd /d [path_to_script]
#### 6. Создаем в этой папке scrapy-проект:
##### scrapy startproject books
#### 7. Открываем папку с пауками:
##### explorer books/books/spiders
#### 8. Создаем здесь файл books_spider.py и копируем в него содержимое файла
[books_spyder.py](https://github.com/FilArt/scraping/blob/master/books_spider.py)
#### 9. Переходим в директорию проекта:
##### cd books
#### 10. Запускаем скрипт:
##### scrapy crawl books

#### После того, как скрипт выполнится, рядом с папкой проекта появится файла books.txt
##### explorer .
