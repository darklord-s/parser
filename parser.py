import urllib.request
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, site):
        self.site = site

    def scrape(self):
                # Добавляем заголовки, чтобы имитировать браузер
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        req = urllib.request.Request(self.site, headers=headers)
        with open('links.txt', "w") as title:
            title.write(f'{self.site}\n\n')

        try:
            r = urllib.request.urlopen(req)
            html = r.read()
            sp = BeautifulSoup(html, 'html.parser')
            
            for tag in sp.find_all('a'):
                url = tag.get('href')
                if url is None:
                    continue
                if url.endswith('html'):
                    with open('links.txt', "a") as f:
                        f.write('\n' + url)
                    print('\n' + url)
        except Exception as e:
            print(f'Ошибка {e}')

news = 'https://books.toscrape.com/'
Scraper(news).scrape()