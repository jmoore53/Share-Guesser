from yahoo_finance import Share

def get_stock_info():
	share = Share('AAPL')
	opening = share.get_open()
	dividend_yeild = share.get_earnings_share()

	print share.get_short_ratio()

get_stock_info()