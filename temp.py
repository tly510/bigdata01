# DB
import sqlite3

conn = sqlite3.connect('cafe.db')
cur = conn.cursor()

cur.execute('''
create table ticket (
id integer primary key auto increment,
number integer not null
)
''')
conn.commit()
conn.close() # free db instance


# 날짜시간 모듈
#import datetime

#now = datetime.datetime.now()
#print(now)
#print(f"현재 시각 : {now.strftime('%Y-%m-%d %H:%M:%S')}")
#print(f"현재 시각 : {now.strftime('%Y년 %m월 %d일 %H시 %M분 %S초')}")

# file 10
#file = open("ticket.txt", "w")
#file.close()


