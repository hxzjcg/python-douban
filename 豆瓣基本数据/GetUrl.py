import re
import time
import progressbar
import requests
import tqdm as tqdm
from bs4 import BeautifulSoup


class Geturl:
    def __init__(self,headers):
        self.headers=headers
        self.totalurl=[]
        self.booklist=[]

    def total_Url(self):
        for i in tqdm.tqdm(range(0,42),"对于获取顶部链接进度："):
            i=i*25
            url = 'https://www.douban.com/doulist/1264675/?start=%d&sort=seq&playable=0&sub_type=' % i
            self.totalurl.append(url)

    def get_Book_Url(self):
        for url in tqdm.tqdm(self.totalurl,"对于获取每一本书的链接，以及图片链接"):
            # 为了防止访问出现问题将时间线进行延长
            time.sleep(1)
            sc = url
            html_books = requests.get(url=sc, headers=self.headers)
            html_books.encoding="utf-8"
            html_book=html_books.text
            hb = BeautifulSoup(html_book, "html.parser")
            # 得到固定范围的字符
            texts = hb.find_all('div', class_='doulist-item')
            texts = str(texts)
            hu = BeautifulSoup(texts, "html.parser")
            text1 = hu.find_all('div', class_='post')
            # 得到的所有的书的块内容
            progress = progressbar.ProgressBar()
            for x in text1:
                x = str(x)
                # 将图书的地址和图书图片的地址单独提取出来
                all_url = r'<a href="(.*?)" target="_blank">'
                img_url = r'<img src="(.*?)"/>'
                a_url = re.findall(all_url, x)
                # 转译字符串
                for y in a_url:
                    y = str(y)
                i_url = re.findall(img_url, x)
                for z in i_url:
                    z = str(z)
                # 进行数据的保存
                with open("图书链接.txt", "a", encoding='utf-8') as file:
                    file.write(y+"\n")
                    file.close()
                with open("图书图片链接.txt", "a", encoding='utf-8') as file:
                    file.write(z+"\n")
                    file.close()
            html_books.close()



if __name__=='__main__':
    headers = {'user-agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42'
              ,
               'Cookie':'bid=5H2aYlUsk_s; __utmz=30149280.1666444852.1.1.utmcsr=so.com|utmccn=(referral)|utmcmd=referral|utmcct=/link; __gads=ID=b36281519c376d09-22bb986f78d70017:T=1666444852:RT=1666444852:S=ALNI_MayekplovfgnF2-67U9lnW0UE5yDg; ap_v=0,6.0; __gpi=UID=00000b696c044311:T=1666444852:RT=1669593854:S=ALNI_Ma-8MO_hnTmJxYVT4_gIJJrthi-Wg; __utmc=30149280; __utma=30149280.1703324647.1666444852.1666444852.1669593854.2; ll="108303"; _ga=GA1.2.1703324647.1666444852; _gid=GA1.2.754582495.1669597045; dbcl2="264827925:ofzLITzPOjA"; ck=RUZS; push_noty_num=0; push_doumail_num=0; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1669597090%2C%22https%3A%2F%2Faccounts.douban.com%2Fpassport%2Fsetting%22%5D; _pk_ses.100001.8cb4=*; __yadk_uid=K9gpjS9U0tAbJ7VqmZGCmdjb9e55kuaz; _pk_id.100001.8cb4=d574ae400f1ccf44.1669593852.2.1669597128.1669595178.; __utmt=1; __utmv=30149280.26482; __utmb=30149280.10.10.1669593854'
               ,'Host': 'www.douban.com',
               'Sec - Fetch - Dest': 'document',
               'Sec - Fetch - Mode': 'navigate',
               'Sec - Fetch - Site': 'none',
               'Sec - Fetch - User': '?1',
               'Upgrade - Insecure - Requests': '1',
               'Connection': 'keep - alive'
               }

    geturl=Geturl(headers)
    geturl.total_Url()
    geturl.get_Book_Url()



