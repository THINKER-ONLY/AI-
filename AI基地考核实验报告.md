# AI基地考核实验报告

## 题目背景和要求

### 	题目：网络爬虫的实现

### 	背景：

​		你被要求编写一个爬虫程序，用于从一个新闻网站（例如：）上爬取新闻板块和标题的对应的链接，并存储到本地文件中。

## 正文：

​	实现方式：使用Python中的requests实现

​	爬取目标：新华网	

​	实现思路：使用requests进行爬取然后使用csv库进行写入。

​	实现代码：

```Python
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
```

​	个人评价：非常潦草的完成，其作用仅为爬取新华网网页上的新闻和板块的链接与标题，并写入csv文件。

​	进阶的方法：使用scrapy进行爬取，能够实现大范围全覆盖式的贪婪爬取，但我还不太会嘿嘿

​	[Github]([THINKER-ONLY/AI-](https://github.com/THINKER-ONLY/AI-))

