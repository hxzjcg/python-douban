import pymysql

# 添加主要信息
def  UpdateAuthor(which,value,isbn):
    db = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        passwd="193750",
        db="book_main_information",
        charset='utf8'
    )
    # 要修改的数据库名称
    table = 'book_all_introduce'
    # 使用定位将数据并行输入
    if which==1:
        SQL = f"update book_all_introduce set 作者 = %s where ISBN码 = %s"
    elif which==2:
        SQL = f"update book_all_introduce set 出版社 = %s where ISBN码 = %s"
    elif which==3:
        SQL = f"update book_all_introduce set 出版日期 = %s where ISBN码 = %s"
    elif which==4:
        SQL = f"update book_all_introduce set 书本价格 = %s where ISBN码 = %s"
    elif which == 5:
        SQL = f"update book_all_introduce set 书本链接 = %s where ISBN码 = %s"
    elif which == 6:
        SQL = f"update book_all_introduce set 封面链接 = %s where ISBN码 = %s"
    # 将要写入的数据先行准备好
    values = []
    # 使用cursor方法创建一个游标
    cursor = db.cursor()
    if cursor:
        try:
            # 将要写入的数据填充
            val = [value,isbn]
            # 依次写入
            values.append(tuple(val))
            # 执行
            cursor.executemany(SQL, values)
            db.commit()
        except Exception as e:
            print("异常", e)

    else:
        print("连接失败")
    db.close()

# 添加主键和书名
def    InsertMysql(isbn,name):
    db = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        passwd="193750",
        db="book_main_information",
        charset='utf8'
    )
    # 要写入的数据库名称
    table = 'book_all_introduce'
    # 要写入的数据库列表
    field_array = ['ISBN码', '书名']
    # 使用定位将数据并行输入
    SQL = f"INSERT INTO {table}({','.join(field_array)}) VALUES ({','.join(['%s'] * len(field_array))})"
    # 将要写入的数据先行准备好
    values = []
    # 使用cursor方法创建一个游标
    cursor = db.cursor()
    if cursor:
        try:
            # 将要写入的数据填充
            val = [isbn, name]
            # 依次写入
            values.append(tuple(val))
            # 执行
            cursor.executemany(SQL, values)
            db.commit()
        except Exception as e:
            print("异常", e)

    else:
        print("连接失败")
    db.close()



# 添加书籍评分
def Update_Sta(sta,isbn):
    import sys
    sys.setrecursionlimit(100000)  # 例如这里设置为十万
    db = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        passwd="193750",
        db="book_main_information",
        charset='utf8'
    )
    # 要修改的数据库名称
    table = 'book_all_introduce'
    # 使用定位将数据并行输入
    SQL = f"update book_all_introduce set 书本评分 = %s where ISBN码 = %s"
    # 将要写入的数据先行准备好
    values = []
    # 使用cursor方法创建一个游标
    cursor = db.cursor()
    if cursor:
        try:
            # 将要写入的数据填充
            val = [sta, isbn]
            # 依次写入
            values.append(tuple(val))
            # 执行
            cursor.executemany(SQL, values)
            db.commit()
        except Exception as e:
            print("异常", e)

    else:
        print("连接失败")
    db.close()

def get_all_str(which,value,isbn):
    db = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        passwd="193750",
        db="book_main_information",
        charset='utf8'
    )
    # 要修改的数据库名称
    table = 'book_all_introduce'
    # 使用定位将数据并行输入
    if which==1:
        SQL = f"update book_all_introduce set 五星占比 = %s where ISBN码 = %s"
    elif which==2:
        SQL = f"update book_all_introduce set 四星占比 = %s where ISBN码 = %s"
    elif which==3:
        SQL = f"update book_all_introduce set 三星占比 = %s where ISBN码 = %s"
    elif which==4:
        SQL = f"update book_all_introduce set 二星占比 = %s where ISBN码 = %s"
    elif which == 5:
        SQL = f"update book_all_introduce set 一星占比 = %s where ISBN码 = %s"
    # 将要写入的数据先行准备好
    values = []
    # 使用cursor方法创建一个游标
    cursor = db.cursor()
    if cursor:
        try:
            # 将要写入的数据填充
            val = [value,isbn]
            # 依次写入
            values.append(tuple(val))
            # 执行
            cursor.executemany(SQL, values)
            db.commit()
        except Exception as e:
            print("异常", e)

    else:
        print("连接失败")
    db.close()


# 录入简介和主要内容
def insert_str(which,value,isbn):
    db = pymysql.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        passwd="193750",
        db="book_main_information",
        charset='utf8'
    )
    # 要修改的数据库名称
    table = 'book_all_introduce'
    # 使用定位将数据并行输入
    if which==1:
        SQL = f"update book_all_introduce set 内容简介 = %s where ISBN码 = %s"
    elif which==2:
        SQL = f"update book_all_introduce set 原文摘录 = %s where ISBN码 = %s"
    # 将要写入的数据先行准备好
    values = []
    # 使用cursor方法创建一个游标
    cursor = db.cursor()
    if cursor:
        try:
            # 将要写入的数据填充
            val = [value,isbn]
            # 依次写入
            values.append(tuple(val))
            # 执行
            cursor.executemany(SQL, values)
            db.commit()
        except Exception as e:
            print("异常", e)

    else:
        print("连接失败")
    db.close()