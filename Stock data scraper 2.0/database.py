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
		(ticker text, html text, date Date, PRIMARY KEY (ticker))
		"""

		self.cursor.execute(query)
		self.conn.commit()

	def save_data(self, dic):
		query = f"INSERT INTO main VALUES (?,?,?)"
		self.cursor.execute(query, (dic["ticker"], dic["html"], datetime.now()))
		self.conn.commit()

	def get_all_tickers(self):
		"""get all stored ticker pages in the main database"""

		self.cursor.execute("SELECT * FROM main")
		items = self.cursor.fetchall()
		for item in items:
			print(item)

