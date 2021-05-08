from flask import Flask, render_template, request, redirect, url_for, session, flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
import csv

import functions.scraper as scraper
import functions.database as database


app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)


temp_ticker_list = []
temp_page_list = []
temp_stats_list = []

header_list = ['ticker', 'Idx', 'PE', 'EPS_ttm', 'Insider_Own', 'Shs_Outstand', 'Perf_Week', 'Market_Cap', 'Forward_PE', 'EPS_next_Y', 'Insider_Trans', 'Shs_Float', 'Perf_Month', 'Income', 'PEG', 'EPS_next_Q', 'Inst_Own', 'Short_Float', 'Perf_Quarter', 'Sales', 'PS', 'EPS_this_Y', 'Inst_Trans', 'Short_Ratio', 'Perf_Half_Y', 'Booksh', 'PB', 'ROA', 'Target_Price', 'Perf_Year', 'Cashsh', 'PC', 'EPS_next_5Y', 'ROE', '52W_Range', 'Perf_YTD', 'Dividend', 'PFCF', 'EPS_past_5Y', 'ROI', '52W_High', 'Beta', 'Dividend_', 'Quick_Ratio', 'Sales_past_5Y', 'Gross_Margin', '52W_Low', 'ATR', 'Employees', 'Current_Ratio', 'Sales_QQ', 'Oper_Margin', 'RSI_14', 'Volatility', 'Optionable', 'DebtEq', 'EPS_QQ', 'Profit_Margin', 'Rel_Volume', 'Prev_Close', 'Shortable', 'LT_DebtEq', 'Earnings', 'Payout', 'Avg_Volume', 'Price', 'Recom', 'SMA20', 'SMA50', 'SMA200', 'Volume', 'Chg']


@app.route('/', methods=['GET', 'POST'])
def home():
    global temp_ticker_list
    ticker = ""

    if request.method == 'GET':
        return render_template('index.html', ticker=ticker, header_list=header_list)

    if request.method == "POST":
        form = request.form
        if request.form['ticker']:
            ticker = request.form['ticker']
            try:
                page_li, stats_dic = scraper.get_all(ticker)
                temp_page_list.append(page_li)
                temp_stats_list.append(stats_dic)
                temp_ticker_list.append(ticker)
            except Exception as e:
                print(e)

            return render_template('index.html', 
                ticker=ticker,
                header_list=header_list,
                temp_ticker_list=temp_ticker_list,
                temp_stats_list=temp_stats_list,
                temp_page_list=temp_page_list,
                form=form
            )


@app.route('/save', methods=['GET', 'POST'])
#save tickers to Database
def save():
    if request.method =="POST":
        
        return redirect(url_for("home"))


# @app.route("/database", methods=["GET","POST"])
# def view():
#     if request.method == 'GET':
#         return render_template('view.html')


if __name__ == "__main__":
    database.DataBase()
    app.run(debug=True)