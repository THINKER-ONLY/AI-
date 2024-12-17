import requests
from bs4 import BeautifulSoup
import csv

class TARGETS:
    def __init__(self):
        self.url = 'http://www.news.cn/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0'
        }
        self.titles = []
        self.links = []

    def get_data(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"请求发生错误：{e}")
            return None

    def parse(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        tit_divs = soup.find_all('div', class_="tit") + soup.find_all('div', class_="part bg-white") + soup.find_all('li')
        titles = [title.text.strip() for div in tit_divs for title in div.find_all('a')]
        links = [self.url + link.get('href') for div in tit_divs for link in div.find_all('a') if link.get('href')]
        return list(zip(titles, links))

    def run(self):
        html = self.get_data()
        if html:
            data = self.parse(html)
            self.write(data)

    def write(self, data):
        with open('news.csv', 'w', newline = '', encoding = 'utf-8') as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(['标题', '链接'])
            for row in data:
                csvwriter.writerow(row)

if __name__ == "__main__":
    TARGETS().run()