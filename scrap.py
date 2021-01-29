import mysql.connector 
from functions import table

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="thy2321.",
  database='stockdata'
)
mycursor = db.cursor(buffered=True,dictionary=True)

#returns cursor output
def return_cursor(res):
	for x in mycursor: return x


# boolean, whether or not a token is in database
def in_db(t):
	#statement to check whether token is in db
	Q = "SELECT Token FROM token_data WHERE Token IN ('%s')"
	#return either a dict or None
	res = return_cursor(mycursor.execute(Q,t))
	#returns true if res is dict
	if isinstance(res, dict): 
		return True 
	else: 
		return False

def update(token, column, value):
	values = (column, value, token)
	try:
		Q = "UPDATE token_data SET %s = %s WHERE Token = %s"
		mycursor.execute(Q,values)
	except Exception as e:
		print(e)


#inserts table of data with a given token
def insert_token_data(token):
	try:
		d = table(token)
		Q1 = "INSERT INTO token_data (Token, Idx, PE, EPS_ttm, Insider_Own, Shs_Outstand, Perf_Week, Market_Cap, Forward_PE, EPS_next_Y, Insider_Trans, Shs_Float, Perf_Month, Income, PEG, EPS_next_Q, Inst_Own, Short_Float, Perf_Quarter, Sales, PS, EPS_this_Y, Inst_Trans, Short_Ratio, Perf_Half_Y, Booksh, PB, ROA, Target_Price, Perf_Year, Cashsh, PC, EPS_next_5Y, ROE, 52W_Range, Perf_YTD, Dividend, PFCF, EPS_past_5Y, ROI, 52W_High, Beta, Dividend_, Quick_Ratio, Sales_past_5Y, Gross_Margin, 52W_Low, ATR, Employees, Current_Ratio, Sales_QQ, Oper_Margin, RSI_14, Volatility, Optionable, DebtEq, EPS_QQ, Profit_Margin, Rel_Volume, Prev_Close, Shortable, LT_DebtEq, Earnings, Payout, Avg_Volume, Price, Recom, SMA20, SMA50, SMA200, Volume, Chg) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		mycursor.execute(Q1,tuple(d.values()))
		db.commit()
		print('{} data added'.format(token))

	except Exception as e:
		print(e)

update('TSLA','Sector','Tech')