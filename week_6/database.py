import pymysql
import os
from dotenv import load_dotenv


class CafeDatabase:
    def __init__(self):
        load_dotenv()
        host = os.environ.get("mysql_host")
        user = os.environ.get("mysql_user")
        password = os.environ.get("mysql_pass")
        database = os.environ.get("mysql_db")
        # Establish a database connection
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor)

    def select(self, sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            # Gets all rows from the result
            rows = cursor.fetchall()
            cursor.close()
            return rows
        except Exception as e:
            print(f"DB exception: {e}")
            return []

    def selectSingle(self, sql):
        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            # Gets all rows from the result
            row = cursor.fetchone()
            cursor.close()
            return row
        except Exception as e:
            print("DB exception: %s," % e)
            return {}

    def execute(self, query, val):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, val)
            self.connection.commit()
            cursor.close()
        except Exception as e:
            print(f"DB exception: {e}")

    def closeConnection(self):
        self.connection.close()
