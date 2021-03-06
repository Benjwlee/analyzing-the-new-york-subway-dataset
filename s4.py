from pandas import *
from ggplot import *
import pprint

import datetime
import itertools
import operator

import brewer2mpl
import ggplot as gg
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

turnstile_weather=pd.read_csv( "C:/move - bwlee/Data Analysis/Nano/\
Intro to Data Science/project/code/turnstile_data_master_with_weather.csv")

tbht = turnstile_weather[["Hour", "ENTRIESn_hourly", "rain"]]
#print tbht
turnstile_by_hour=turnstile_weather[["Hour","rain","ENTRIESn_hourly"]] \
  .groupby(["Hour","rain"]).sum()
turnstile_by_hour.index.name='Hour'
turnstile_by_hour=turnstile_by_hour.reset_index()
#plot=ggplot(aes(x='ENTRIESn_hourly', color='rain'), data=tbht) \
#  +geom_histogram(binwidth=500)+xlab("ENTRIESn_hourly")+ylab("Frequency") \
#  +ggtitle("Frequency of Entry per Hour, red=No rain, blue = rain")
#print plot
#plot=ggplot(turnstile_by_hour, aes("Hour", weight="ENTRIESn_hourly")) \
#  +geom_histogram()+xlab("Hour")+ylab("ENTRIESn_hourly")+ggtitle("T")
#print plot
#plot=ggplot(turnstile_by_hour, aes("Hour", weight="ENTRIESn_hourly")) \
#  +geom_bar()+scale_y_continuous(labels='coma')+xlab("Hour") \
#  +ylab("ENTRIESn_hourly")+ggtitle("T")
#print plot

#tbh=pd.melt(tbht[["Hour", "ENTRIESn_hourly", "rain"]], id_vars=['Hour'])
#plot=ggplot(tbh, aes(x="Hour", y="value", colour="variable")) \
#  +geom_bar(stat="bar")
#print plot
turnstile_by_hour.to_csv('dump.csv')
plot=ggplot(turnstile_by_hour,aes(x="Hour",y="ENTRIESn_hourly",fill="rain")) \
  +geom_bar(stat="identity")+xlab("Hour of Day")+ylab("ENTRIESn_hourly") \
  +ggtitle("Stacked bar of Turnstile Entry histogram Rain=red/No Rain=blue")
print plot