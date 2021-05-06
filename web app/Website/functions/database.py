import sqlite3
from sqlite3 import Error
from datetime import datetime
import time

FILE = "database.db"
PAGES = "pages"
STATS = "stats"


class DataBase:
	"""
	used to connect, write to and read from a local sqlite3 database
	"""
	def __init__(self):
		self.conn = None
		try:
			self.conn = sqlite3.connect(FILE)
		except Error as e:
			print(e)

		self.cursor = self.conn.cursor()
		self.create_pages_table()
		self.create_stats_table()



	def close(self):
		"""
		Close the db connection
		:return: None
		"""
		self.conn.close()



	def create_pages_table(self):
		"""
		creates a a table to store html pages for each ticker symbol
		:return: None
		"""
		query = f"""
		CREATE TABLE IF NOT EXISTS {PAGES}
		(ticker text, html text, date Date, PRIMARY KEY (ticker))
		"""

		self.cursor.execute(query)
		self.conn.commit()


	def create_stats_table(self):
		"""
		creates a a table to store stats for a symbol for each ticker symbol
		:return: None
		"""
		query = f"""CREATE TABLE IF NOT EXISTS {STATS} ("ticker" text,"date" Date, "Idx" text, "PE" text, "EPS_ttm" text, "Insider_Own" text, "Shs_Outstand" text, "Perf_Week" text, "Market_Cap" text, "Forward_PE" text, "EPS_next_Y" text, "Insider_Trans" text, "Shs_Float" text, "Perf_Month" text, "Income" text, "PEG" text, "EPS_next_Q" text, "Inst_Own" text, "Short_Float" text, "Perf_Quarter" text, "Sales" text, "PS" text, "EPS_this_Y" text, "Inst_Trans" text, "Short_Ratio" text, "Perf_Half_Y" text, "Booksh" text, "PB" text, "ROA" text, "Target_Price" text, "Perf_Year" text, "Cashsh" text, "PC" text, "EPS_next_5Y" text, "ROE" text, "52W_Range" text, "Perf_YTD" text, "Dividend" text, "PFCF" text, "EPS_past_5Y" text, "ROI" text, "52W_High" text, "Beta" text, "Dividend_" text, "Quick_Ratio" text, "Sales_past_5Y" text, "Gross_Margin" text, "52W_Low" text, "ATR" text, "Employees" text, "Current_Ratio" text, "Sales_QQ" text, "Oper_Margin" text, "RSI_14" text, "Volatility" text, "Optionable" text, "DebtEq" text, "EPS_QQ" text, "Profit_Margin" text, "Rel_Volume" text, "Prev_Close" text, "Shortable" text, "LT_DebtEq" text, "Earnings" text, "Payout" text, "Avg_Volume" text, "Price" text, "Recom" text, "SMA20" text, "SMA50" text, "SMA200" text, "Volume" text, "Chg" text, PRIMARY KEY (ticker))"""
		self.cursor.execute(query)
		self.conn.commit()


	def save_page(self, dic):
		"""
		Save ticker html page into database
		:prams dic: dict
		:return: None
		"""
		query = f"INSERT INTO pages VALUES (?,?,?)"
		self.cursor.execute(query, (li[0], li[1], datetime.now()))
		self.conn.commit()


	def save_stats(self, dic):
		"""
		Inject the stats of a symbol into the "stats" table
		:prams dic: dict
		:return: None
		"""
		query = f"INSERT INTO stats VALUES (? ,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
		values = (dic["ticker"], datetime.now(), dic["Idx"], dic["PE"], dic["EPS_ttm"], dic["Insider_Own"], dic["Shs_Outstand"], dic["Perf_Week"], dic["Market_Cap"], dic["Forward_PE"], dic["EPS_next_Y"], dic["Insider_Trans"], dic["Shs_Float"], dic["Perf_Month"], dic["Income"], dic["PEG"], dic["EPS_next_Q"], dic["Inst_Own"], dic["Short_Float"], dic["Perf_Quarter"], dic["Sales"], dic["PS"], dic["EPS_this_Y"], dic["Inst_Trans"], dic["Short_Ratio"], dic["Perf_Half_Y"], dic["Booksh"], dic["PB"], dic["ROA"], dic["Target_Price"], dic["Perf_Year"], dic["Cashsh"], dic["PC"], dic["EPS_next_5Y"], dic["ROE"], dic["52W_Range"], dic["Perf_YTD"], dic["Dividend"], dic["PFCF"], dic["EPS_past_5Y"], dic["ROI"], dic["52W_High"], dic["Beta"], dic["Dividend_"], dic["Quick_Ratio"], dic["Sales_past_5Y"], dic["Gross_Margin"], dic["52W_Low"], dic["ATR"], dic["Employees"], dic["Current_Ratio"], dic["Sales_QQ"], dic["Oper_Margin"], dic["RSI_14"], dic["Volatility"], dic["Optionable"], dic["DebtEq"], dic["EPS_QQ"], dic["Profit_Margin"], dic["Rel_Volume"], dic["Prev_Close"], dic["Shortable"], dic["LT_DebtEq"], dic["Earnings"], dic["Payout"], dic["Avg_Volume"], dic["Price"], dic["Recom"], dic["SMA20"], dic["SMA50"], dic["SMA200"], dic["Volume"], dic["Chg"])
		self.cursor.execute(query,values)
		self.conn.commit()
		print("Stats for ticker: {} saved into stats table".format(dic["ticker"]))

	def stats_list(self):
		"""
		get all stored ticker pages in the pages database
		:return: list
		"""
		li = []
		self.cursor.execute("SELECT * FROM stats")
		items = self.cursor.fetchall()
		for item in items:
			li.append(item[0])
		return li

	def get_all_stats(self):
		"""
		get all stored ticker pages in the pages database
		:return: list
		"""
		li = []
		self.cursor.execute("SELECT * FROM stats")
		items = self.cursor.fetchall()
		for item in items:
			li.append(item)
		return li


	def pages_list(self):
		"""
		get all stored ticker pages in the pages database
		:return: list
		"""

		li = []
		self.cursor.execute("SELECT * FROM pages")
		items = self.cursor.fetchall()
		for item in items:
			li.append(item[0])
		return li


	def get_page(self, ticker):
		"""
		returns a tuple containing (ticker, HTML, date) from the database
		:param ticker: str
		:return: tupl
		"""
		try:
			ticker = ticker.upper()
			self.cursor.execute(f"SELECT * FROM pages WHERE ticker = '{ticker}'")
			html = self.cursor.fetchall()[0]
			return html
		except IndexError:
			print(f"Failed.{ticker} is not stored in the pages database.")
