import matplotlib.pyplot as plt  # plotting
import numpy as np  # linear algebra
import os  # accessing directory structure
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import sys


def write_file(file_name, content):
    f = open(file_name, 'w')
    f.writelines(["%s" % line for line in content])
    print("written file=[" + file_name + "]")


def read_txt_file(file_name):
    f = open(file_name, 'r')
    return f.readlines()


def get_dept_id(dept_name):
    if dept_name == "Out of SF":
        return 0
    elif dept_name == "Central":
        return 1
    elif dept_name == "Mission":
        return 2
    elif dept_name == "Northern":
        return 3
    elif dept_name == "Southern":
        return 4
    elif dept_name == "Tenderloin":
        return 5
    elif dept_name == "Bayview":
        return 6
    elif dept_name == "Ingleside":
        return 7
    elif dept_name == "Park":
        return 8
    elif dept_name == "Richmond":
        return 9
    elif dept_name == "Taraval":
        return 10
    else:
        return 0


nRowsRead = 1000  # specify 'None' if want to read whole file
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
print(f'There are {nRow} rows and {nCol} columns to be processed')

sql_dept = []
sql_users = []
sql_incident = []
sql_location = []
sql_comp = []
sql_reports = []
sql_init_db = []
for i in range(nRow):
    dept_id = get_dept_id(df['Police District'][i])
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
    line_incident = r"INSERT INTO INCIDENTS VALUES('{}','{}',TO_DATE('{}','YYYY-MM-DD'),TO_TIMESTAMP('{} {}', 'YYYY-MM-DD HH24:MI:SS'),'{}');{}"
    line_incident = line_incident.format(i, dept_id, df['Incident Date'][i], df['Incident Date'][i],
                                         df['Incident Time'][i], df['Incident Year'][i], "\n")
    sql_incident.append(line_incident)

    # -- table Location
    # CREATE TABLE LOCATION (
    #     Incident_ID INT             NOT NULL,
    # 	Longitude REAL              NOT NULL,
    # 	Latitude  REAL              NOT NULL,
    # 	Intersection VARCHAR(255)   NOT NULL,
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
    line_location = line_location.replace("\'null\'", "null")
    sql_location.append(line_location)

    # -- table Complainant
    # CREATE TABLE COMPLAINANT (
    #     User_ID     INT            NOT NULL,
    # 	  Incident_ID INT            NOT NULL,
    #     FOREIGN KEY (Incident_ID) REFERENCES INCIDENTS(Incident_ID),
    #     FOREIGN KEY (User_ID) REFERENCES PORTAL_USER(User_ID)
    # );
    line_comp = r"INSERT INTO COMPLAINANT VALUES ('{}','{}');{}"
    line_comp = line_comp.format(1, i, "\n")
    sql_comp.append(line_comp)

    # -- table Report
    # CREATE TABLE REPORT (
    #   Report_ID INT                     NOT NULL,
    # 	Dept_ID INT                       NOT NULL,
    #   Incident_ID                       NOT NULL,
    # 	Incident_Category VARCHAR(255)    ,
    # 	Incident_Subcategory VARCHAR(255) ,
    # 	Resolution VARCHAR(255)           ,
    # 	Report_Type VARCHAR(255)          ,
    # 	PRIMARY KEY (Report_ID),
    # 	FOREIGN KEY(Dept_ID) REFERENCES POLICE_DEPARTMENT(Dept_ID)
    # );
    fmt = r"INSERT INTO REPORT VALUES ('{}','{}', '{}', '{}','{}','{}','{}');{}"
    incident_cat = df["Incident Category"][i]
    if incident_cat != incident_cat:
        incident_cat = "null"
    incident_subcat = df["Incident Subcategory"][i]
    if incident_subcat != incident_subcat:
        incident_subcat = "null"
    resolution = df["Resolution"][i]
    if resolution != resolution:
        resolution = "null"
    report_type = df["Report Type Code"][i]
    if report_type != report_type:
        report_type = "null"
    line_report = fmt.format(i, dept_id, i, incident_cat, incident_subcat, resolution, report_type, "\n")
    line_report = line_report.replace("\'null\'", "null")
    sql_reports.append(line_report)

# read manual generated sql statements
sql_init_db = read_txt_file("init_db.sql")
sql_init_db.append("\n")
sql_dept = read_txt_file("insert_dept.sql")
sql_dept.append("\n")
sql_users = read_txt_file("insert_users.sql")
sql_users.append("\n")

# generate all the output file needed
sql_all = sql_init_db + sql_dept + sql_users + sql_incident + sql_location + sql_comp + sql_reports

write_file("insert_data.sql", sql_all)

# write down individual sql file for debugging purpose
write_file("insert_incident.sql", sql_incident)
write_file("insert_location.sql", sql_location)
write_file("insert_comp.sql", sql_comp)
write_file("insert_report.sql", sql_reports)
