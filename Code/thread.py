import pandas as pd

rd = pd.read_csv('D:/Flight Databases/all.csv',header=0, delimiter=",", engine='python', na_filter=False, dtype=str, chunksize=65535)
slim_data = []




