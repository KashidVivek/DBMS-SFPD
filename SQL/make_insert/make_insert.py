import matplotlib.pyplot as plt  # plotting
import numpy as np  # linear algebra
import os  # accessing directory structure
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import sys

def write_file(file_name, content):
    f = open(file_name, 'w')
    f.writelines(["%s" % line for line in content])
    print("written file=[" + file_name + "]")


nRowsRead = 100  # specify 'None' if want to read whole file
# Police_Department_Incident_Reports__2018_to_Present.csv has 223958 rows in reality, but we are only loading/previewing the first 1000 rows
df = pd.read_csv('./Police_Department_Incident_Reports__2018_to_Present.csv', delimiter=',', nrows=nRowsRead,
                 skiprows=1, names=[
        "Incident Datetime", "Incident Date", "Incident Time", "Incident Year", "Incident Day of Week",
        "Report Datetime", "Row ID", "Incident ID", "Incident Number", "CAD Number", "Report Type Code",
        "Report Type Description", "Filed Online", "Incident Code", "Incident Category", "Incident Subcategory",
        "Incident Description", "Resolution", "Intersection", "CNN", "Police District", "Analysis Neighborhood",
        "Supervisor District", "Latitude", "Longitude", "point"]
                 )
df.dataframeName = 'Police_Department_Incident_Reports__2018_to_Present.csv'
nRow, nCol = df.shape
print(f'There are {nRow} rows and {nCol} columns')
#print(df.head(3))

sql_incident = []
sql_location = []
for i in range(nRow):
#   -- table Incidents
# CREATE TABLE INCIDENTS (
#   Incident_ID INT        NOT NULL,
# 	Dept_ID     INT        NOT NULL,
# 	Incident_Date DATE,
# 	Incident_Time TIMESTAMP,
# 	Incident_Year INT,
#   PRIMARY KEY (Incident_ID),
#   FOREIGN KEY(Dept_ID) REFERENCES POLICE_DEPARTMENT(Dept_ID)
# );
    line_incident = r"INSERT INTO INCIDENTS VALUES('{}','{}',TO_DATE('{}','YYYY-MM-DD'),TO_TIMESTAMP('{}', 'YYYY-MM-DD HH24:MI:SS.FF'),'{}');{}"
    line_incident = line_incident.format(i, 0, df['Incident Date'][i], df['Incident Datetime'][i], df['Incident Year'][i], "\n")
    sql_incident.append(line_incident)

# -- table Location
# CREATE TABLE LOCATION (
#     Incident_ID INT             NOT NULL,
# 	Longitude REAL              ,
# 	Latitude  REAL              ,
# 	Intersection VARCHAR(255)   ,
#     FOREIGN KEY (Incident_ID) REFERENCES INCIDENTS(Incident_ID)
# );
    line_location = r"INSERT INTO LOCATION VALUES('{}','{}','{}','{}');{}"
    t = df['Latitude'][i]
    if t != t:
        t = 'null'
    Latitude = t
    t = df['Longitude'][i]
    if t != t:
        t = 'null'
    Longitude = t
    t = df['Intersection'][i]
    if t != t:
        t = 'null'
    Intersection = t
    line_location = line_location.format(i, Longitude, Latitude, Intersection, "\n")
    sql_location.append(line_location)

write_file("ins_incident.sql", sql_incident)
write_file("ins_location.sql", sql_location)
sql_all = sql_incident + sql_location
write_file("ins_all.sql", sql_all)
