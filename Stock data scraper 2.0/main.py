from database import DataBase
import scraper

db = DataBase()
msft = scraper.get_page("asdf")
print(msft)
# db.save_data(msft)
# db.get_all_tickers()