from django.shortcuts import render
from mainApp.models import *
from django.db import connection


# Create your views here.
def index(request):
    return render(request, 'mainApp/index.html')


# def user(request):
#     user_list = .objects.order_by('user_id')
#     user_dict = {'users': user_list}
#     return render(request, 'mainApp/user.html', context=user_dict)
def my_custom_sql():
    sql_str = """
    SELECT
        COUNT(*) AS cnt,
        incident_day_of_week
    FROM
        main
    GROUP BY
        incident_day_of_week
    ORDER BY
        cnt DESC"""

    with connection.cursor() as cursor:
        cursor.execute(sql_str)
        row = cursor.fetchall()
    return row


def police_page(request):
    row_id = my_custom_sql()
    print(row_id)
    row_id_dict = {'row_id': row_id}
    return render(request, 'mainApp/police_page.html', context=row_id_dict)


def register(request):
    return render(request, 'mainApp/register.html')


def user_page(request):
    return render(request, 'mainApp/user_page.html')


def exec_sql(sql_str):
    with connection.cursor() as cursor:
        cursor.execute(sql_str)
        row = cursor.fetchall()
    return row


def simple(request):
    result_t = {}
    # --1.	Determine the day of week when most crime happen.
    sql_str = """
    SELECT
        COUNT(row_id)
    FROM
        main
    """
    result = exec_sql(sql_str)
    print(result)
    result_t['r0'] = result


    # --1.	Determine the day of week when most crime happen.
    sql_str = """
    SELECT
        COUNT(*) AS cnt,
        incident_day_of_week
    FROM
        main
    GROUP BY
        incident_day_of_week
    ORDER BY
        cnt DESC"""
    result = exec_sql(sql_str)
    print(result)
    result_t['r1'] = result

    # --2.	Find the most committed crime.
    sql_str = """
    SELECT * FROM (
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
    cnt DESC
    ) WHERE rownum <= 10
    """
    result = exec_sql(sql_str)
    print(result)
    result_t['r2'] = result

    # --3.	Find a particular area of city where most of the crime happen.
    sql_str = """
    SELECT * FROM (
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
    cnt DESC
    ) WHERE rownum <= 10
    """
    result = exec_sql(sql_str)
    print(result)
    result_t['r3'] = result

    # --4.	Determine the number of cases resolved in San Francisco.
    sql_str = """
SELECT
    COUNT(*)
FROM
    main      a,
    reports   b
WHERE
    a.incident_id = b.incident_id
    AND b.resolution = 'Cite or Arrest Adult'"""
    result = exec_sql(sql_str)
    print(result)
    result_t['r4'] = result

    # --5.	Determine the safest area of the city.
    sql_str = """SELECT * FROM (
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
            cnt ASC
        ) WHERE ROWNUM <=10
    """
    result = exec_sql(sql_str)
    print(result)
    result_t['r5'] = result

    # --6.	Determine the time and a particular area where there is maximum probability of crime scene.
    # -- not doing this, no time, we could change it to date?

    # --7.	Find if reporting the crime online as soon as crime is committed can help resolve the issues faster.
    # -- RC change this to a trend

    # --8.	Find the most committed crime in every district of San Francisco.
    sql_str = """SELECT * FROM (
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
            cnt DESC
    )WHERE ROWNUM <=10
    """
    result = exec_sql(sql_str)
    print(result)
    result_t['r8'] = result

    # --9.	Find the type of crime which is hardest to resolve.
    sql_str = """SELECT * FROM (
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
    ) WHERE ROWNUM <=10
    """
    result = exec_sql(sql_str)
    print(result)
    result_t['r9'] = result

    # --10.	Determine the time period when the crime is least likely to happen.
    # -- will not do because we don't have time now

    # --11.	Determine the most prevalent crime committed in a certain region.
    # -- RC this is actually the same as #8 
    return render(request, 'mainApp/simple.html', context=result_t)
