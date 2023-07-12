import pymysql
from datetime import datetime
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
        select_name = "SELECT id FROM `user`"
        cursor.execute(select_name)
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



def sqlwork(name,vpn_give,data):
    
    try:
        sql_connect()
        print ("successfully connected...")
    except Exception as ex:
        print ("Connection refused...")
        print (ex)

