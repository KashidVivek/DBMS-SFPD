--1.	Determine the day of week when most crime happen.
SELECT
    COUNT(*) AS cnt,
    incident_day_of_week
FROM
    main
GROUP BY
    incident_day_of_week
ORDER BY
    cnt DESC;
    
--2.	Find the most committed crime.

SELECT
    COUNT(*) AS cnt,
    a.incident_code       AS c,
    b.incident_category   AS n
FROM
    main       a,
    incident   b
WHERE
    a.incident_code = b.incident_code
GROUP BY
    a.incident_code,
    b.incident_category
ORDER BY
    cnt DESC;


--3.	Find a particular area of city where most of the crime happen.

SELECT
    COUNT(*) AS cnt,
    c.analysis_neighborhood AS an
FROM
    main               a,
    incident           b,
    incident_address   c
WHERE
    a.incident_code = b.incident_code
    AND a.cnn = c.cnn
    AND c.analysis_neighborhood <> 'null'
GROUP BY
    c.analysis_neighborhood
ORDER BY
    cnt DESC;

--4.	Determine the number of cases resolved in San Francisco.
SELECT
    COUNT(*)
FROM
    main      a,
    reports   b
WHERE
    a.incident_id = b.incident_id
    AND b.resolution = 'Cite or Arrest Adult';
    
--5.	Determine the safest area of the city.
SELECT
    COUNT(*) AS cnt,
    c.analysis_neighborhood AS an
FROM
    main               a,
    incident           b,
    incident_address   c
WHERE
    a.incident_code = b.incident_code
    AND a.cnn = c.cnn
    AND c.analysis_neighborhood <> 'null'
GROUP BY
    c.analysis_neighborhood
ORDER BY
    cnt ASC;
    
--6.	Determine the time and a particular area where there is maximum probability of crime scene.
-- not doing this, no time, we could change it to date?

SELECT
    COUNT(*) AS cnt,
    a.incident_datetime as incident_date, 
    c.analysis_neighborhood AS an
FROM
    main               a,
    incident           b,
    incident_address   c
WHERE
    a.incident_code = b.incident_code
    AND a.cnn = c.cnn
    AND c.analysis_neighborhood <> 'null'
GROUP BY
    c.analysis_neighborhood, a.incident_datetime
ORDER BY
    cnt DESC;

--7.	Find if reporting the crime online as soon as crime is committed can help resolve the issues faster.
-- RC change this to a trend

--8.	Find the most committed crime in every district of San Francisco. 
SELECT
    COUNT(*) AS cnt,
    b.incident_category       AS n,
    c.analysis_neighborhood   AS an
FROM
    main               a,
    incident           b,
    incident_address   c
WHERE
    a.incident_code = b.incident_code
    AND a.cnn = c.cnn
GROUP BY
    c.analysis_neighborhood,
    b.incident_category
ORDER BY
    cnt DESC;


--9.	Find the type of crime which is hardest to resolve. 
SELECT
    COUNT(*) as cnt, 
    c.incident_category,
    b.resolution
FROM
    main      a,
    reports   b,
    incident  c
WHERE
    a.incident_id = b.incident_id
    AND b.resolution = 'Open or Active'
    AND a.incident_code = c.incident_code 
GROUP  BY
    c.incident_category, b.resolution
Order BY
    cnt DESC
    ;

--10.	Determine the time period when the crime is least likely to happen.
-- will not do because we don't have time now

--11.	Determine the most prevalent crime committed in a certain region.
-- RC this is actually the same as #8 
