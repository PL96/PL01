# from sqlalchemy import create_engine
import pandas as pd
import tushare as ts
dt = ts.get_stock_basics()
'''engine = create_engine('mysql://user:root@127.0.0.1/db_name?charset=utf8')
dt.to_sql('tick_data',engine,if_exists='append',)
df1 = pd.read_sql('tick_data',engine)'''
print(dt)
quit



