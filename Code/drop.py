import pandas as pd
df = pd.read_csv("D:/Flight Databases/flightlist_20190101_20190131.csv")
df_new = df.drop(['number'], axis = 1, inplace=False)
df_new.to_csv("D:/Flight Databases1.0/flightlist_20190101_20190131.csv")

print(df_new)