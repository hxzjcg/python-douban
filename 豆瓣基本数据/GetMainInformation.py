import linecache
import re
import threading
import time
import pymysql
import requests
import tqdm
from bs4 import BeautifulSoup

from Mathor import TheMysql
from Mathor import IfElse

class GetInformation():
    def __init__(self,headers):
        # threading.Thread.__init__(self)
        # self.threadId=threadId;
        # self.threadName=threadName;
        # self.ThreadCounter=ThreadCounter;
        self.headers=headers


    def run(self):
        pass

    # 得到数据库主键和外键
    def getNameIsbn(self):
        pbar = tqdm.tqdm(total=1050)
        url_list = open("图书链接.txt", 'r')
        for url in url_list:
            url = str(url)
            url = url.replace("\n", "")
            time.sleep(1)
            html_books = requests.get(url=url, headers=self.headers, allow_redirects=False)
            html_books.encoding = "utf-8"
            html_book = html_books.text
            # 正则获取ISBN和Name
            get_isbn = r'.*?<meta property="book:isbn" content="(.*?)" />.*?'
            get_name = r'.*?<meta property="og:title" content="(.*?)" />.*?'
            # 匹配
            book_isbn = re.findall(get_isbn, html_book, re.A)
            book_name = re.findall(get_name, html_book, re.A)

            # 防止不存在报错
            isbn = IfElse.IfLong(book_isbn)
            name = IfElse.IfLong(book_name)

            # 写入数据库
            TheMysql.InsertMysql(isbn, name)
            pbar.update(1)
            html_books.close()

    # 得到书籍主要内容
    def get_Book_InforMation(self):
        pbar = tqdm.tqdm(total=1050)
        url_list = open("图书链接.txt", 'r')
        line=1
        for url in url_list:
            url = url.replace("\n", "")
            time.sleep(1)
            html_books = requests.get(url=url, headers=self.headers, allow_redirects=False)
            img_url = linecache.getline('图书图片链接.txt', line)
            html_books.encoding = "utf-8"
            html_book = html_books.text
            url=str(url)
            img_url=str(img_url)
            get_isbn = r'.*?<meta property="book:isbn" content="(.*?)" />.*?'

            book_isbn = re.findall(get_isbn, html_book, re.A)
            isbn = IfElse.IfLong(book_isbn)

            # 作者，出版社，出版日期，书本价格
            # 作者获取列表部分
            get_author = r'<meta property="book:author" content="(.*?)" />'
            book_author = re.findall(get_author, html_book, re.A)

            # 出版社部分
            get_book_address = r'<span class="pl">出版社:</span>(.*?)<span.*?'
            book_address = re.findall(get_book_address, html_book, re.S)
            # 出版日期以及出版价格
            get_book_Date = r'<span class="pl">出版年:</span>(.*?)<br/>'
            get_book_prise = r'<span class="pl">定价:</span>(.*?)<br/>'
            book_Date = re.findall(get_book_Date, html_book, re.A)
            book_prise = re.findall(get_book_prise, html_book, re.A)

            # 作者值得到部分
            # 对于作者如果有多个值将所有的值录入
            author = ""
            lenght = 1
            # 有多个值的情况下判定好位置将数据按照规则写好
            for x in book_author:
                if lenght < len(book_author):
                    author = author + x + "/"
                    lenght += 1
                else:
                    author = author + x
            # 出版社一般都是一个，因此不需要多重判定
            IfElse.Dta_author(author)
            address = IfElse.Dta_book(book_address)
            date = IfElse.IfLong(book_Date)
            prise = IfElse.IfLong(book_prise)
            # 将数据库修改成一个修改方法
            # images_list = ['作者', '出版社', '出版日期', '书本价格']改为1234
            book_list = [author, address, date, prise,url,img_url]
            index = 1
            for x in book_list:
                x = str(x)
                TheMysql.UpdateAuthor(index, x, isbn)
                index += 1
            pbar.update(1)
            html_books.close()

    # 得到评分以及评分占比
    def GetStrart(self):
        pbar = tqdm.tqdm(total=1050)
        url_list = open("图书链接.txt", 'r')
        for url in url_list:
            url = url.replace("\n", "")
            time.sleep(1)
            html_books = requests.get(url=url, headers=self.headers, allow_redirects=False)
            html_books.encoding = "utf-8"
            html_book = html_books.text
            # 得到主键
            get_isbn = r'.*?<meta property="book:isbn" content="(.*?)" />.*?'
            book_isbn = re.findall(get_isbn, html_book, re.A)
            isbn = IfElse.IfLong(book_isbn)
            # 得到评分
            get_sta=r'<strong class="ll rating_num " property="v:average">(.*?)</strong>'
            book_sta=re.findall(get_sta,html_book,re.A)
            sta=IfElse.IfLong(book_sta)
            # 将评分写入数据库
            TheMysql.Update_Sta(sta,isbn)
            # 得到每个评分占比
            get_sl=r'<span class="rating_per">(.*?)</span>'
            book_sl=re.findall(get_sl,html_book,re.A)
            # 写入数据库
            index=1
            for x in book_sl:
                TheMysql.get_all_str(index,x,isbn)
                index+=1
            pbar.update(1)
            html_books.close()

    # 得到内容简介和原文摘录
    def Get_book_size(self):
        pbar = tqdm.tqdm(total=1050)
        url_list = open("图书链接.txt", 'r')
        for url in url_list:
            url = url.replace("\n", "")
            time.sleep(1)
            html_books = requests.get(url=url, headers=headers, allow_redirects=False)
            html_books.encoding = "utf-8"
            html_book = html_books.text
            # 得到主键
            get_isbn = r'.*?<meta property="book:isbn" content="(.*?)" />.*?'
            book_isbn = re.findall(get_isbn, html_book)
            isbn = IfElse.IfLong(book_isbn)

            # 得到简介
            soup = BeautifulSoup(html_book, "lxml")
            content = soup.find("div", class_="intro")
            content = str(content)
            get_jianjie = r'<p>(.*?)</p>'
            book_jianjie = re.findall(get_jianjie, content)
            jianjie = IfElse.delete(book_jianjie)

            # 得到原文
            soup1 = BeautifulSoup(html_book, 'lxml')
            content1 = soup1.find("figure", class_="")
            content1 = str(content1)
            get_yuanwen = r'<figure>(.*?)<a.*?'
            book_yuanwen = re.findall(get_yuanwen, content1, re.S)
            yuanwen = IfElse.yuanwen(book_yuanwen)

            # 录入数据库
            index = 1
            update_str = [jianjie, yuanwen]
            for x in update_str:
                TheMysql.insert_str(index, x, isbn)
                index += 1
            pbar.update(1)
            html_books.close()




if __name__=="__main__":
    headers = {'user-agent':
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 '
                   'Safari/537.36 Edg/107.0.1418.42 '
        ,
               'Cookie': 'bid=sF5I2jKVR-I; __utmc=30149280; __gads=ID=ff3b68892b4d22bf-22d0d64147da00fc:T=1677715059:RT=1677715059:S=ALNI_MallnkvCs-Y8UZEuDeAxis_utXxiA; __utmc=81379588; gr_user_id=695a31de-a6a8-47fd-89b7-e2dcd3102c55; __yadk_uid=bOh5OG49Z4SkLslGA1ZE4ctJC0U6wKZa; _vwo_uuid_v2=D063A51E807E8FBD8A55531705795C8E0|61533600702e0e914fcf431225674888; douban-fav-remind=1; __utma=30149280.804414958.1677715020.1677719856.1677733557.3; __utmz=30149280.1677733557.3.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/doulist/1264675/; __utmz=81379588.1677733557.3.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/doulist/1264675/; __utma=81379588.2145696368.1677715252.1677719856.1677733556.3; viewed="26941639_35494026_10519369"; dbcl2="268265342:o0zlvX+oKHA"; ck=qxNE; frodotk_db="4a21b729909beff2de65257cb1d3cfd6"; push_noty_num=0; push_doumail_num=0; __gpi=UID=00000bcf99520f8a:T=1677715059:RT=1677737746:S=ALNI_MbFuUTpR_X6RoOeHX9MhD9entVUQw; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=4d46a65c-77f8-4f0a-a176-700fdfeb4058; gr_cs1_4d46a65c-77f8-4f0a-a176-700fdfeb4058=user_id:1; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_4d46a65c-77f8-4f0a-a176-700fdfeb4058=true; ap_v=0,6.0; _pk_ref.100001.3ac3=["","",1677748204,"https://www.douban.com/doulist/1264675/?start=1050&sort=seq&playable=0&sub_type="]; _pk_id.100001.3ac3=aab8ac313e0962ae.1677715252.4.1677748204.1677737744.; _pk_ses.100001.3ac3=*'

        ,
               'Host': 'book.douban.com',
               'Referer': 'https://accounts.douban.com/',
               'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
               'sec-ch-ua - mobile': '?0',
               'sec-ch-ua-platform': 'Windows',
               'Sec-Fetch-Dest': 'document',
               'Sec-Fetch-Mode': 'navigate',
               'Sec-Fetch-Site': 'same-site',
               'Sec-Fetch-User': '?1',
               'Upgrade - Insecure - Requests': '1'
               }
    getInformation=GetInformation(headers)
    getInformation.Get_book_size()
