import sqlite3
from sqlite3 import Error
from datetime import datetime
import time


FILE = "main.db"
MAIN = "main"

class DataBase:
	def __init__(self):
		self.conn = None
		try:
			self.conn = sqlite3.connect(FILE)
		except Error as e:
			print(e)

		self.cursor = self.conn.cursor()
		self.create_table()

	def close(self):
		self.conn.close()

	def create_table(self):

		query = f"""
		CREATE TABLE IF NOT EXISTS {MAIN}
		(ticker text, html text, date text, PRIMARY KEY (ticker))
		"""

		self.cursor.execute(query)
		self.conn.commit()

db = DataBase()