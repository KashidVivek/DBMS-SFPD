from django.shortcuts import render
from mainApp.models import *
from django.db import connection
import string
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

def mark_ann(ann_data, width, height):
    API_KEY = "&key=AIzaSyDzG7agJsgEFdigIRPO_bhk6hpxd3bUiWs"
    locations = {'South of Market': (37.777537573999664, -122.406580109256203),
                 'Bernal Heights': (37.740769566867813, -122.415664319656129),
                 'Russian Hill': (37.799941027422978, -122.418902309631447),
                 'Outer Richmond': (37.77794512181484, -122.49072320183385),
                 'Treasure Island': (37.8264854724547, -122.374343658987),
                 'Japantown': (37.785224794269727, -122.434656028162636),
                 'Hayes Valley': (37.774718344556745, -122.4278980407455),
                 'Seacliff': (37.786488437803446, -122.4856050115308),
                 'Lakeshore': (37.72046784794244, -122.481350351517606),
                 'West of Twin Peaks': (37.735116111476448, -122.459963178580664),
                 'Marina': (37.800577333305262, -122.436714314128453),
                 'Western Addition': (37.781852669041229, -122.430784391268277),
                 'Golden Gate Park': (37.769515668283686, -122.475015640246942),
                 'Lincoln Park': (37.7815147468806, -122.49585682387475),
                 'Bayview Hunters Point': (37.730669269056457, -122.391470894943076),
                 'Lone Mountain/USF': (37.777803869776424, -122.449566493098221),
                 'Potrero Hill': (37.75910747871955, -122.396599741633787),
                 'McLaren Park': (37.720267514643223, -122.415520271271352),
                 'Tenderloin': (37.78383850833851, -122.415298086652224),
                 'Financial District/South Beach': (37.789527088646421, -122.399283288992746),
                 'Mission': (37.759611270217274, -122.416581363620441),
                 'Excelsior': (37.719180027102677, -122.432291113730816),
                 'Nob Hill': (37.791732736060923, -122.414696723196403),
                 'Outer Mission': (37.720274203678128, -122.443068324199128),
                 'null': (37.70826303419995, -122.436214937626), 'Chinatown': (37.796166628208461, -122.4071113206567),
                 'Mission Bay': (37.770781714206707, -122.395717732066339),
                 'Haight Ashbury': (37.768215031628186, -122.444100882203),
                 'Glen Park': (37.737876665571102, -122.433290670416),
                 'Inner Richmond': (37.7807677434141, -122.465611046905494),
                 'Twin Peaks': (37.752819479579238, -122.44689411988108),
                 'Visitacion Valley': (37.713173562059788, -122.409401287137715),
                 'Inner Sunset': (37.758535365857894, -122.465031358730918),
                 'North Beach': (37.802308895817212, -122.40843938188217),
                 'Pacific Heights': (37.790806335560613, -122.435016462623216),
                 'Oceanview/Merced/Ingleside': (37.717706223465826, -122.46066369173882),
                 'Castro/Upper Market': (37.762078176532479, -122.435942407682387),
                 'Sunset/Parkside': (37.748493740776172, -122.492013546486453),
                 'Presidio Heights': (37.786446066094551, -122.451854967682459),
                 'Noe Valley': (37.749217893413229, -122.433315325933885),
                 'Portola': (37.726834897170642, -122.40907809167776),
                 'Presidio': (37.799710580872862, -122.466937579893083)}

    urlbase = r"https://maps.googleapis.com/maps/api/staticmap?"
    url = urlbase
    url = url + "center=san+francisco&"
    url = url + "size={}x{}".format(width, height)
    for key, value in ann_data.items():
        p = locations.get(key, (0, 0))
        if p != (0, 0):
            marker = "&markers=label:{}%7c{},{}".format(value, p[0], p[1])
            url = url + marker + "%7c"

    url = url + API_KEY
    return url

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
    ann_data = {}
    r2 = []
    i = 0
    n = list(string.ascii_uppercase)
    for t in result:
        ann_data[t[1]] = n[i]
        t2 = (*t, n[i])
        r2.append(t2)
        i = i + 1
    map_url = mark_ann(ann_data, 800, 600)
    result_t['r3'] = r2
    print(r2)
    result_t['r3_map'] = map_url

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
    ann_data = {}
    r2 = []
    i = 0
    n = list(string.ascii_uppercase)
    for t in result:
        ann_data[t[1]] = n[i]
        t2 = (*t, n[i])
        r2.append(t2)
        i = i + 1
    map_url = mark_ann(ann_data, 800, 600)
    result_t['r5'] = r2
    print(r2)
    result_t['r5_map'] = map_url


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
