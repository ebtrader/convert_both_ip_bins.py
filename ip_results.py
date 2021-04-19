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
df = pd.read_csv('ecom_txns.csv')
#df.columns = ['height']
df['converted_ip'] = df['ip_address'].apply(lambda x: int(ipaddress.IPv4Address(x))).astype('float64')
print(df)

df1 = pd.read_csv('ip_to_integer_brief2.csv')
df1['int_end'] = df1['int_end'].astype('float64')

#print(df1)

df3 = df1['country'].dropna()
df3.columns = ['country']
#print(df3)

#df2 = pd.read_csv('country.csv')
#df2.columns = ['country']
#print(df2)

countries_list = df3.tolist()
print(countries_list)
#df['binned']=pd.cut(x=df['height'], bins=df1['bin_intervals'])

df['country_code']=pd.cut(x = df['converted_ip'],
                        bins = df1['int_end'],
                        labels = countries_list, ordered=False
                        )

print(df)
df.to_csv('ip_classifier1.csv')