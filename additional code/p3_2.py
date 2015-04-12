from pandas import *
from ggplot import *
import pprint

import itertools

import ggplot as gg
import numpy as np
import pandas as pd
from datetime import datetime, date, time

turnstile_weather=pandas.read_csv("C:/move - bwlee/Data Analysis/Nano/Intro to Data Science/project/code/turnstile_data_master_with_weather.csv")

df = turnstile_weather[['DATEn', 'ENTRIESn_hourly', 'rain']]
 
dfm=[0.0]*7
dfc=[0.0]*7
dfa=[0.0]*7
df['DATEw']=[int(datetime.strptime(elem, "%Y-%m-%d").weekday()) for elem in df['DATEn']]
print df.head(n=3)
for index, line in df.iterrows():
  day=line['DATEw']
  dfm[day]+=line['ENTRIESn_hourly']
  dfc[day]+=1.0
for i in range(7):
  dfa[i]=dfm[i]/dfc[i]
rddf=pd.DataFrame({'weekday': range(7), 'hourlyentries': dfa}, columns=['weekday', 'hourlyentries'])

print rddf

plot=ggplot(rddf, aes('weekday', 'hourlyentries')) + \
  geom_bar(fill = 'steelblue', stat='bar') + \
  scale_x_continuous(name="weekday", breaks=[0, 1, 2, 3, 4, 5, 6], 
    labels=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]) + \
  ggtitle("average ENTRIESn_hourly by weekday") + \
  ylab("ENTRIESn_hourly")
print plot
