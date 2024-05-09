from logging import getLogger
from typing import Union

import mysql.connector as mysql_conn
from mysql.connector.pooling import PooledMySQLConnection
from mysql.connector.abstracts import MySQLConnectionAbstract
from mysql.connector.cursor import MySQLCursorAbstract


from week6.setting import config as cnf

log = getLogger()

def get_connection()->tuple[Union[PooledMySQLConnection, MySQLConnectionAbstract], MySQLCursorAbstract]:
    conn = None
    try:
        conn = mysql_conn.connect(
            host=cnf.HOST,
            user=cnf.USER,
            password=cnf.PASSWORD,
            database=cnf.DATABASE
        )

        if conn.is_connected():
            log.info('成功連線')
            return conn, conn.cursor()
    except Exception as e:
        print(e)
        raise e