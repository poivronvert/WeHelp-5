import os

from mysql.connector import connect, Error
from mysql.connector.pooling import MySQLConnectionPool

from dotenv import load_dotenv

load_dotenv()

_env = os.environ

pool_name = "mypool"
pool_size = 10

config = {
  "user": "root",
  "password": _env.get("MYSQL_PASSWORD", None),
  "host": "127.0.0.1",
  "database": "website",
  "raise_on_warnings": True
}

cnxpool = MySQLConnectionPool(pool_name = pool_name,
                              pool_size = pool_size,
                              **config)
try:
  # 模擬用戶送出第一個請求，顯示所有留言
  conn1 = cnxpool.get_connection()

  if conn1.is_connected():
    conn1 = cnxpool.get_connection()
    cursor1 = conn1.cursor()
    cursor1.execute('SELECT name, content FROM website.member JOIN website.message ON website.member.id=website.message.member_id;')
    for (name, content) in cursor1:
      print(f"所有留言: name: {name}, content: {content}")
      
except Error as e:
  print(e)

finally:
  if conn1 and conn1.is_connected():
    cursor1.close()
    conn1.close()

# 模擬用戶送出第二個請求，顯示第一個留言
  conn2 = cnxpool.get_connection()

try:
  if conn2.is_connected():
      conn2 = cnxpool.get_connection()
      cursor2 = conn2.cursor()
      cursor2.execute('SELECT name, content FROM website.member JOIN website.message ON website.member.id=website.message.member_id LIMIT 1;')
      for (name, content) in cursor2:
        print(f"第一個留言: name: {name}, content: {content}")
      
except Error as e:
  print(e)

finally:
  if conn2 and conn2.is_connected():
    cursor2.close()
    conn2.close()
