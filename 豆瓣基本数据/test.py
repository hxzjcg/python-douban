#
# #
# # url_list = open("图书链接.txt", 'r')
# # for url in url_list:
# #     url = url.replace("\n", "")
# #     print(url)
# #
# import re
# import time
#
# import pymysql
# import requests
# from tqdm import tqdm
#
# headers = {'user-agent':
#                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 '
#                    'Safari/537.36 Edg/107.0.1418.42 '
#         ,
#                'Cookie': 'bid=sF5I2jKVR-I; __utmc=30149280; __gads=ID=ff3b68892b4d22bf-22d0d64147da00fc:T=1677715059:RT=1677715059:S=ALNI_MallnkvCs-Y8UZEuDeAxis_utXxiA; __utmc=81379588; gr_user_id=695a31de-a6a8-47fd-89b7-e2dcd3102c55; __yadk_uid=bOh5OG49Z4SkLslGA1ZE4ctJC0U6wKZa; _vwo_uuid_v2=D063A51E807E8FBD8A55531705795C8E0|61533600702e0e914fcf431225674888; douban-fav-remind=1; __utma=30149280.804414958.1677715020.1677719856.1677733557.3; __utmz=30149280.1677733557.3.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/doulist/1264675/; __utmz=81379588.1677733557.3.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/doulist/1264675/; __utma=81379588.2145696368.1677715252.1677719856.1677733556.3; viewed="26941639_35494026_10519369"; dbcl2="268265342:o0zlvX+oKHA"; ck=qxNE; frodotk_db="4a21b729909beff2de65257cb1d3cfd6"; push_noty_num=0; push_doumail_num=0; __gpi=UID=00000bcf99520f8a:T=1677715059:RT=1677737746:S=ALNI_MbFuUTpR_X6RoOeHX9MhD9entVUQw; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=4d46a65c-77f8-4f0a-a176-700fdfeb4058; gr_cs1_4d46a65c-77f8-4f0a-a176-700fdfeb4058=user_id:1; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_4d46a65c-77f8-4f0a-a176-700fdfeb4058=true; ap_v=0,6.0; _pk_ref.100001.3ac3=["","",1677748204,"https://www.douban.com/doulist/1264675/?start=1050&sort=seq&playable=0&sub_type="]; _pk_id.100001.3ac3=aab8ac313e0962ae.1677715252.4.1677748204.1677737744.; _pk_ses.100001.3ac3=*'
#
#                ,
#                'Host': 'book.douban.com',
#                'Referer': 'https://accounts.douban.com/',
#                'sec-ch-ua':'"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
#                 'sec-ch-ua - mobile': '?0',
#                 'sec-ch-ua-platform': 'Windows',
#                 'Sec-Fetch-Dest': 'document',
#                 'Sec-Fetch-Mode': 'navigate',
#                 'Sec-Fetch-Site': 'same-site',
#                 'Sec-Fetch-User': '?1',
#                 'Upgrade - Insecure - Requests': '1'
#                }
# # pbar = tqdm(total=1050)
# # url_list = open("图书链接.txt",'r')
# # for url in url_list:
# #             url=url.replace("\n","")
# #             time.sleep(1)
# #             html_books = requests.get(url=url, headers=headers, allow_redirects=False)
# #             html_books.encoding = "utf-8"
# #             html_book = html_books.text
# #             # 正则获取ISBN和Name
# #             get_isbn=r'.*?<meta property="book:isbn" content="(.*?)" />.*?'
# #             get_name=r'.*?<meta property="og:title" content="(.*?)" />.*?'
# #             # 匹配
# #             book_isbn=re.findall(get_isbn,html_book,re.A)
# #             book_name=re.findall(get_name,html_book,re.A)
# #             # 防止不存在报错
# #             if len(book_isbn)==0:
# #                 isbn=""
# #             else:
# #                 isbn = book_isbn[0]
# #             if len(book_name)==0:
# #                 name=""
# #             else:
# #                 name=book_name[0]
# #             isbn=str(isbn)
# #             name=str(name)
# #             db = pymysql.connect(
# #                 host="127.0.0.1",
# #                 port=3306,
# #                 user="root",
# #                 passwd="193750",
# #                 db="book_main_information",
# #                 charset='utf8'
# #             )
# #             # 要写入的数据库名称
# #             table = 'book_all_introduce'
# #             # 要写入的数据库列表
# #             field_array = ['ISBN码','书名','书本链接']
# #             # 使用定位将数据并行输入
# #             SQL = f"INSERT INTO {table}({','.join(field_array)}) VALUES ({','.join(['%s'] * len(field_array))})"
# #             # 将要写入的数据先行准备好
# #             values = []
# #             # 使用cursor方法创建一个游标
# #             cursor = db.cursor()
# #             if cursor:
# #                 try:
# #                     # 将要写入的数据填充
# #                     val = [isbn, name,url]
# #                     # 依次写入
# #                     values.append(tuple(val))
# #                     # 执行
# #                     cursor.executemany(SQL, values)
# #                     db.commit()
# #                 except Exception as e:
# #                     print("异常", e)
# #
# #             else:
# #                 print("连接失败")
# #             pbar.update(1)
# #             db.close()
# #             html_books.close()
#
#
# # url_list = open("图书链接.txt", 'r')
# # # for url in (url_list, "获取书籍名称以及书籍ISBN码进度："):
# # url = 'https://book.douban.com/subject/1132550/'
# # # time.sleep(1)
# # html_books = requests.get(url=url, headers=headers, allow_redirects=False)
# # html_books.encoding = "utf-8"
# # html_book = html_books.text
# # # 作者，出版社，出版日期，书本价格
# # get_author = r'<meta property="book:author" content="(.*?)" />'
# # book_author = re.findall(get_author, html_book, re.A)
# # # 如果有多个值将所有的值录入
# # author = ""
# # lenght=1
# # # 有多个值的情况下判定好位置将数据按照规则写好
# # for x in book_author:
# #     if lenght<len(book_author):
# #         author=author+x+"/"
# #         lenght+=1
# #     else:
# #         author=author+x
#
# # html_books.close()
# # list=['daw']
# # print(len(list))
#
#
# # def get_Book_InforMation(self, headers):
# pbar = tqdm(total=1050)
# url_list = open("图书链接.txt", 'r')
# # for url in (url_list, "获取书籍名称以及书籍ISBN码进度："):
# while True:
#
#         url = 'https://book.douban.com/subject/25762009/'
#         time.sleep(1)
#         html_books = requests.get(url=url, headers=headers, allow_redirects=False)
#         html_books.encoding = "utf-8"
#         html_book = html_books.text
#         get_isbn = r'.*?<meta property="book:isbn" content="(.*?)" />.*?'
#         book_isbn = re.findall(get_isbn, html_book, re.A)
#         if len(book_isbn) == 0:
#             isbn = ""
#         else:
#             isbn = book_isbn[0]
#             isbn = str(isbn)
#         # 作者，出版社，出版日期，书本价格
#
#         # 作者获取列表部分
#         get_author = r'<meta property="book:author" content="(.*?)" />'
#         book_author = re.findall(get_author, html_book, re.A)
#
#         # 出版社部分
#         get_book_address = r'<span class="pl">出版社:</span>.*?<a href=.*?>(.*?)</a>'
#         book_address = re.findall(get_book_address, html_book, re.A)
#
#         # 出版日期以及出版价格
#         get_book_Date = r'<span class="pl">出版年:</span>(.*?)<br/>'
#         get_book_prise = r'<span class="pl">定价:</span>(.*?)<br/>'
#         book_Date = re.findall(get_book_Date, html_book, re.A)
#         book_prise = re.findall(get_book_prise, html_book, re.A)
#
#         # 作者值得到部分
#         # 对于作者如果有多个值将所有的值录入
#         author = ""
#         lenght = 1
#         # 有多个值的情况下判定好位置将数据按照规则写好
#         for x in book_author:
#             if lenght < len(book_author):
#                 author = author + x + "/"
#                 lenght += 1
#             else:
#                 author = author + x
#
#         # 出版社一般都是一个，因此不需要多重判定
#         if len(book_address) == 0:
#             address = ""
#         else:
#             address = book_address[0]
#             address = str(address)
#
#         # 出版日期以及书籍价格一般都是一个，所以不做判断
#         if len(book_Date) == 0:
#             Date = ""
#         else:
#             Date = book_Date[0]
#             Date = str(Date)
#         if len(book_prise) == 0:
#             prise = ""
#         else:
#             prise = book_prise[0]
#             prise = str(prise)
#         db = pymysql.connect(
#             host="127.0.0.1",
#             port=3306,
#             user="root",
#             passwd="193750",
#             db="book_main_information",
#             charset='utf8'
#         )
#         # 要写入的数据库名称
#         table = 'book_main_information'
#         # 要写入的数据库列表
#         field_array = ['作者', '出版社', '出版日期', '书本价格']
#         # 使用定位将数据并行输入
#         SQL = f" updqte {table} set ({','.join(field_array)}) = ({','.join(['%s'] * len(field_array))}) where ISBN码 =  "
#         # 将要写入的数据先行准备好
#         SQL=SQL+isbn
#         values = []
#         # 使用cursor方法创建一个游标
#         cursor = db.cursor()
#         if cursor:
#             try:
#                 # 将要写入的数据填充
#                 val = [author, address, Date, prise]
#                 # 依次写入
#                 values.append(tuple(val))
#                 # 执行
#                 cursor.executemany(SQL, values)
#                 db.commit()
#             except Exception as e:
#                 print("异常", e)
#
#         else:
#             print("连接失败")
#         db.close()
#         pbar.update(1)
#         html_books.close()
import re
import time

import pymysql
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

from Mathor import IfElse
from Mathor import TheMysql
# # list=["da"]
# # ans=IfElse.IfLong(list)
# # print(ans)
# ans='书本评分'
# print(ans)
# TheMysql.UpdateAuthor(ans,'4562','9787501602933')
headers = {'user-agent':
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 '
                   'Safari/537.36 Edg/107.0.1418.42 '
        ,
               'Cookie': 'bid=sF5I2jKVR-I; __utmc=30149280; __gads=ID=ff3b68892b4d22bf-22d0d64147da00fc:T=1677715059:RT=1677715059:S=ALNI_MallnkvCs-Y8UZEuDeAxis_utXxiA; __utmc=81379588; gr_user_id=695a31de-a6a8-47fd-89b7-e2dcd3102c55; __yadk_uid=bOh5OG49Z4SkLslGA1ZE4ctJC0U6wKZa; _vwo_uuid_v2=D063A51E807E8FBD8A55531705795C8E0|61533600702e0e914fcf431225674888; douban-fav-remind=1; __utma=30149280.804414958.1677715020.1677719856.1677733557.3; __utmz=30149280.1677733557.3.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/doulist/1264675/; __utmz=81379588.1677733557.3.2.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/doulist/1264675/; __utma=81379588.2145696368.1677715252.1677719856.1677733556.3; viewed="26941639_35494026_10519369"; dbcl2="268265342:o0zlvX+oKHA"; ck=qxNE; frodotk_db="4a21b729909beff2de65257cb1d3cfd6"; push_noty_num=0; push_doumail_num=0; __gpi=UID=00000bcf99520f8a:T=1677715059:RT=1677737746:S=ALNI_MbFuUTpR_X6RoOeHX9MhD9entVUQw; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=4d46a65c-77f8-4f0a-a176-700fdfeb4058; gr_cs1_4d46a65c-77f8-4f0a-a176-700fdfeb4058=user_id:1; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_4d46a65c-77f8-4f0a-a176-700fdfeb4058=true; ap_v=0,6.0; _pk_ref.100001.3ac3=["","",1677748204,"https://www.douban.com/doulist/1264675/?start=1050&sort=seq&playable=0&sub_type="]; _pk_id.100001.3ac3=aab8ac313e0962ae.1677715252.4.1677748204.1677737744.; _pk_ses.100001.3ac3=*'

               ,
               'Host': 'book.douban.com',
               'Referer': 'https://accounts.douban.com/',
               'sec-ch-ua':'"Chromium";v="110", "Not A(Brand";v="24", "Microsoft Edge";v="110"',
                'sec-ch-ua - mobile': '?0',
                'sec-ch-ua-platform': 'Windows',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-site',
                'Sec-Fetch-User': '?1',
                'Upgrade - Insecure - Requests': '1'
               }

#
# def get_Book_InforMation(headers):
#     pbar = tqdm(total=1050)
#     url_list = open("图书链接.txt", 'r')
#     for url in url_list:
#     # while True:
#         url = url.replace("\n", "")
#         # url = 'https://book.douban.com/subject/2215160/'
#         time.sleep(1)
#         html_books = requests.get(url=url, headers=headers, allow_redirects=False)
#         html_books.encoding = "utf-8"
#         html_book = html_books.text
#         get_isbn = r'.*?<meta property="book:isbn" content="(.*?)" />.*?'
#
#         book_isbn = re.findall(get_isbn, html_book, re.A)
#         isbn = IfElse.IfLong(book_isbn)
#
#         # 作者，出版社，出版日期，书本价格
#         # 作者获取列表部分
#         get_author = r'<meta property="book:author" content="(.*?)" />'
#         book_author = re.findall(get_author, html_book,re.A)
#
#         # 出版社部分
#         get_book_address = r'<span class="pl">出版社:</span>(.*?)<span.*?'
#         book_address = re.findall(get_book_address, html_book,re.S)
#         # 出版日期以及出版价格
#         get_book_Date = r'<span class="pl">出版年:</span>(.*?)<br/>'
#         get_book_prise = r'<span class="pl">定价:</span>(.*?)<br/>'
#         book_Date = re.findall(get_book_Date, html_book, re.A)
#         book_prise = re.findall(get_book_prise, html_book, re.A)
#
#         # 作者值得到部分
#         # 对于作者如果有多个值将所有的值录入
#         author = ""
#         lenght = 1
#         # 有多个值的情况下判定好位置将数据按照规则写好
#         for x in book_author:
#             if lenght < len(book_author):
#                 author = author + x + "/"
#                 lenght += 1
#             else:
#                 author = author + x
#         # 出版社一般都是一个，因此不需要多重判定
#         IfElse.Dta_author(author)
#         print(author)
#         address = IfElse.Dta_book(book_address)
#         print(address)
#         date = IfElse.IfLong(book_Date)
#         prise = IfElse.IfLong(book_prise)
#         # 将数据库修改成一个修改方法
#         # images_list = ['作者', '出版社', '出版日期', '书本价格']改为1234
#         book_list = [author, address, date, prise]
#         index = 1
#         for x in book_list:
#             x=str(x)
#             TheMysql.UpdateAuthor(index,x, isbn)
#             index += 1
#         pbar.update(1)
#         html_books.close()
# get_Book_InforMation(headers)
def Get_book_size(headers):
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
        content=str(content)
        get_jianjie=r'<p>(.*?)</p>'
        book_jianjie=re.findall(get_jianjie,content)
        jianjie=IfElse.delete(book_jianjie)

        # 得到原文
        soup1=BeautifulSoup(html_book,'lxml')
        content1=soup1.find("figure",class_="")
        content1=str(content1)
        get_yuanwen=r'<figure>(.*?)<a.*?'
        book_yuanwen=re.findall(get_yuanwen,content1,re.S)
        yuanwen=IfElse.yuanwen(book_yuanwen)

        # 录入数据库
        index=1
        update_str=[jianjie,yuanwen]
        for x in  update_str:
            TheMysql.insert_str(index,x,isbn)
            index+=1
        html_books.close()
Get_book_size(headers)