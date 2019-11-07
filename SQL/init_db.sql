DROP TABLE COMPLAINANT;
DROP TABLE REPORT;
DROP TABLE LOCATION;
DROP TABLE INCIDENTS;
DROP TABLE POLICE_OFFICIAL;
DROP TABLE PORTAL_USER;
DROP TABLE POLICE_DEPARTMENT;

-- table Portal User
CREATE TABLE PORTAL_USER (
    User_ID INT             NOT NULL,
    Email VARCHAR(255)      NOT NULL,
    phone_number INT        NOT NULL,
	Password VARCHAR(255)   NOT NULL,
	DOB DATE                NOT NULL,
	Name VARCHAR(255)       NOT NULL,
    PRIMARY KEY (User_ID)
);

-- table Police Department
CREATE TABLE POLICE_DEPARTMENT (
	Dept_ID INT              NOT NULL,
	District VARCHAR(255)    NOT NULL,
	Location VARCHAR(255)    NOT NULL,
	CNN INT                  NOT NULL,
	Telephone INT            NOT NULL,
	Supervisor VARCHAR(255)  NOT NULL,
    PRIMARY KEY (Dept_ID)
);

-- table Police Offical
CREATE TABLE POLICE_OFFICIAL (
    User_ID INT               NOT NULL,
	Dept_ID INT               NOT NULL,
	Offical_Rank VARCHAR(255) NOT NULL,
    FOREIGN KEY (User_ID) REFERENCES PORTAL_USER(User_ID),
    FOREIGN KEY(Dept_ID) REFERENCES POLICE_DEPARTMENT(Dept_ID)
);

-- table Incidents
CREATE TABLE INCIDENTS (
    Incident_ID INT        NOT NULL,
	Dept_ID     INT        NOT NULL,
	Incident_Date DATE,
	Incident_Time TIMESTAMP,
	Incident_Year INT,
    PRIMARY KEY (Incident_ID),
    FOREIGN KEY(Dept_ID) REFERENCES POLICE_DEPARTMENT(Dept_ID)
);

-- table Complainant
CREATE TABLE COMPLAINANT (
    User_ID     INT            NOT NULL,
	Incident_ID INT            NOT NULL,
    FOREIGN KEY (Incident_ID) REFERENCES INCIDENTS(Incident_ID),
    FOREIGN KEY (User_ID) REFERENCES PORTAL_USER(User_ID)
);

-- table Report
CREATE TABLE REPORT (
    Report_ID INT                     NOT NULL,
	Dept_ID INT                       NOT NULL,
	Incident_Category VARCHAR(255)    NOT NULL,
	Incident_Subcategory VARCHAR(255) NOT NULL,
	Resolution VARCHAR(255)           NOT NULL,
	Report_Type VARCHAR(255)          NOT NULL,
	PRIMARY KEY (Report_ID),
	FOREIGN KEY(Dept_ID) REFERENCES POLICE_DEPARTMENT(Dept_ID)
);

-- table Location
CREATE TABLE LOCATION (
    Incident_ID INT             NOT NULL,
	Longitude REAL              NOT NULL,
	Latitude  REAL              NOT NULL,
	Intersection VARCHAR(255)   NOT NULL,
    FOREIGN KEY (Incident_ID) REFERENCES INCIDENTS(Incident_ID)
);

