# coding=utf-8

from sqlalchemy import create_engine
import tushare as ts
import pandas as pd

df = ts.get_hist_data('002175')
td = ts.get_today_all()

db_engine = create_engine("postgresql://postgres:wind@192.168.234.135/stock")
df.to_sql()

ss = pd.DataFrame