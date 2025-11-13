import pandas as pd
# source: https://realpython.com/pandas-dataframe/

dt = pd.date_range(start='2019-10-27 00:00:00.0', periods=24, freq='h')
temp_c = [ 8.0,  7.1,  6.8,  6.4,  6.0,  5.4,  4.8,  5.0, 9.1, 12.8, 15.3, 19.1, 21.2, 22.1, 22.4, 23.1, 
           21.0, 17.9, 15.5, 14.4, 11.9, 11.0, 10.2,  9.1]

data = pd.DataFrame(temp_c, index=dt)

print(data.head(10))

# frequency aliases: https://pandas.pydata.org/docs/user_guide/timeseries.html#offset-aliases
