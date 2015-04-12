from pandas import *
import scipy.stats

turnstile_weather=pandas.read_csv("C:/move - bwlee/Data Analysis/Nano/Intro to Data Science/project/code/turnstile_data_master_with_weather.csv")

wrm=np.mean(turnstile_weather[turnstile_weather.rain == 1]['ENTRIESn_hourly'])
wnrm=np.mean(turnstile_weather[turnstile_weather.rain == 0]['ENTRIESn_hourly'])
print "Mean when rain: {0}\nMean no rain: {1}".format(wrm, wnrm)

[U,p]=scipy.stats.mannwhitneyu(turnstile_weather[turnstile_weather.rain == 1]['ENTRIESn_hourly'],
  turnstile_weather[turnstile_weather.rain == 0]['ENTRIESn_hourly'])
print "MW\nStatistic {0}\np-Value {1}".format(U, p)
