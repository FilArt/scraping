import scrapy


class BooksSpider(scrapy.Spider):
    name = "books"

    def start_requests(self):
        urls = [
            'http://books.toscrape.com/catalogue/page-{}.html'.format(n_p) for n_p in range(1, 51)
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        books = response.xpath('//h3/a').re(r'title="(.*)"')

        with open('books.txt', 'a') as f:
            for book in books:
                f.write(book)
                f.write('\n')
