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


def simple_sql():
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


def simple(request):
    row_id = simple_sql()
    print(row_id)
    row_id_dict = {'row_id': row_id}
    return render(request, 'mainApp/simple.html', context=row_id_dict)
