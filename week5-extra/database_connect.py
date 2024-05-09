import os

from sqlalchemy import create_engine, text, Column, Integer, String, DateTime
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker
from datetime import datetime

from my_models import * 

load_dotenv() 


DB_USER = 'root'
DB_PASSWORD = os.environ.get('MYSQL_PSWD')
DB_HOST = '127.0.0.1'
DB_NAME = 'website'

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:3306/{DB_NAME}?charset=utf8mb4"


engine = create_engine(DATABASE_URL)

conn = engine.connect()

# try:
#     conn.execute(text('INSERT INTO member (name, username, password, follower_count) VALUES ("Papaya","papaya","123","6")'))

# except Exception as e:
#     print(f"Error:{e}")


# Session = sessionmaker(bind=engine)
# session = Session()

# try:
#     # 创建会话实例
#     

#     # 创建新的成员记录
#     new_member = Member(name='Orange', username='orgage', password='123', follower_count=7)

#     # 添加新记录到会话
#     session.add(new_member)

#     # 提交会话，将新成员记录插入到数据库中
#     session.commit()

#     print("New member added successfully!")

# except Exception as e:
#     print(f"Error: {e}")
#     session.rollback()  # 发生错误时回滚事务

# finally:
#     # 关闭会话
#     if session:
#         session.close()

try:
    Session = sessionmaker(bind=engine)
    session = Session()
    member_to_delete = session.query(Member).filter(Member.id.in_([8,9,12])).all()
    for member in member_to_delete:
        session.delete(member)
    session.commit()
except Exception as e:
    print(f"Error{e}")


try:
    result = conn.execute(text('SELECT * From member'))
    for row in result:
        print(row)
except Exception as e:
    print(f"Error:{e}")

finally:
    if session:
        session.close()


