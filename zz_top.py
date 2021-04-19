import numpy as np
import pandas as pd
import csv
import ipaddress

df = pd.read_csv('ip4map.csv')

# http://carrefax.com/new-blog/2018/12/17/replace-nan-values-in-pandas-column-with-string

df['country'].fillna('ZZ', inplace=True)

print(df)

df.to_csv('zz_top.csv')