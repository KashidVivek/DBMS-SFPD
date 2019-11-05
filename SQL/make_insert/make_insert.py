import matplotlib.pyplot as plt # plotting
import numpy as np # linear algebra
import os # accessing directory structure
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

print("hello world")

nRowsRead = 1000 # specify 'None' if want to read whole file
# Police_Department_Incident_Reports__2018_to_Present.csv has 223958 rows in reality, but we are only loading/previewing the first 1000 rows
df1 = pd.read_csv('./Police_Department_Incident_Reports__2018_to_Present.csv', delimiter=',', nrows = nRowsRead)
df1.dataframeName = 'Police_Department_Incident_Reports__2018_to_Present.csv'
nRow, nCol = df1.shape
print(f'There are {nRow} rows and {nCol} columns')


print(df1.head(5))