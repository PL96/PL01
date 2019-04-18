import tushare as ts
dt=ts.get_stock_basics()
dt.to_csv('D:/1.csv')
print(dt)

