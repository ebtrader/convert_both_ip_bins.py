import numpy as np
import pandas as pd
import csv
import ipaddress

# https://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.digitize.html#numpy-digitize
# https://cmdlinetips.com/2019/12/how-to-discretize-bin-a-variable-in-python/

#with open('top150.csv') as i:
#    reader = csv.reader(i)
#    your_list = list(reader)

#x = your_list
#print(x)
df = pd.read_csv('zz_top.csv')
#df.columns = ['height']

# https://stackoverflow.com/questions/59023756/convert-ip-address-to-integer-in-pandas

df['int_start'] = df['range_start'].apply(lambda x: int(ipaddress.IPv4Address(x)))
#df.to_csv('ip_to_integer_start_end.csv')
df['int_end'] = df['range_end'].apply(lambda x: int(ipaddress.IPv4Address(x)))
df.to_csv('ip_to_integer_start_end.csv')
print(df)