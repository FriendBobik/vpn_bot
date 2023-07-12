import pymysql
from datetime import datetime, timedelta
from config import host_sql, user_sql, password_sql, db_name_sql



def sql_connect():
    return pymysql.connect(
        host=host_sql,
        port=8889,
        user=user_sql,
        password=password_sql,
        database=db_name_sql,
        cursorclass=pymysql.cursors.DictCursor
    )

def sql_create(name):
    connection = sql_connect()
    with connection.cursor() as cursor:
        current_datetime = datetime.now()
        insert_query = "INSERT INTO `user` (id, free_used, data_free_used, used, data_used, n1, n2, n3, n4, n5) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (name, 0, current_datetime, 0, current_datetime, 0, 0, 0, 0, 0)
        cursor.execute(insert_query, values)
        connection.commit()


def sql_check(name):
    connection = sql_connect()
    with connection.cursor() as cursor:
        cursor.execute("SELECT id FROM user")
        rows = cursor.fetchall()
        profile_exists = 0
        i=0
        for row in rows:
            i=i+1
            if int(row['id']) == name:
                
                profile_exists = 1
                break
    if profile_exists == 1:
        return i
    else:
        return -1
    

def sql_free_value(name):
    connection = sql_connect()
    with connection.cursor() as cursor:
        query = "SELECT free_used FROM user WHERE id = %s"
        cursor.execute(query, (name,))
        result=cursor.fetchall()
        return result[0]['free_used']

def sql_free_date(name):
    connection = sql_connect()
    with connection.cursor() as cursor:
        query = "SELECT data_free_used FROM user WHERE id = %s"
        cursor.execute(query, (name,))
        result=cursor.fetchall()
        return result[0]['data_free_used']        

def sql_change_free_value(name):
    connection = sql_connect()
    with connection.cursor() as cursor:
        query = "UPDATE user SET free_used=1 WHERE id= %s"
        cursor.execute(query, (name,))
        connection.commit()

def sql_change_free_date(name):
    current_datetime = datetime.now()
    future_datetime = current_datetime + timedelta(days=7)
    connection = sql_connect()
    with connection.cursor() as cursor:
        query = "UPDATE user SET data_free_used=%s WHERE id= %s"
        cursor.execute(query, (future_datetime, name,))
        connection.commit()




