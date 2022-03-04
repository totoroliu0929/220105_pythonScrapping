#!/usr/bin/python3.10
#sql = INSERT INTO pm25 (site,county,pm25,date,unit) VALUES ()
import requests
import sqlite3
from sqlite3 import Error

urlpath = 'https://data.epa.gov.tw/api/v1/aqx_p_02?limit=1000&api_key=9be7b239-557b-4c10-9775-78cadfc555e9&sort=ImportDate%20desc&format=json'

def create_connection(db_file):
    """
    連線至資料庫
    :param db_file: 資料庫的檔案名稱
    :return: Connection物件
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
        return

    return conn

def delete_table_pm25(conn):
    sql = 'DROP TABLE pm25;'
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

def create_table_pm25(conn):
    sql = '''
    CREATE TABLE IF NOT EXISTS pm25 (
	id INTEGER PRIMARY KEY,
	site TEXT,
	county TEXT,
	pm25 REAL,
	date TEXT,
	unit TEXT
    );
    '''
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()

def select_pm25(conn):
    sql = '''
    SELECT * FROM pm25 WHERE id = 1
    '''
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    return data

def insert_pm25(conn, values):
    """
    新增資料至projects資料庫
    :param conn:Connection物件
    :param project:tuple(加入至資料庫的內容)
    :return:自動建立id的最後一筆
    """
    sql = ''' 
    INSERT INTO pm25 (site,county,pm25,date,unit)
    VALUES (?,?,?,?,?)
    '''
    cursor = conn.cursor()
    cursor.execute(sql, values)
    conn.commit()

def saveToDataBase(datas):
    '''
    儲存資料至資料庫db25
    :param datas: list->tuple
    :return:
    '''
    conn = create_connection('pm25.db')
    print("資料庫連線成功")
    with conn:
        if datas[0][3] == select_pm25(conn)[0][4]:
            print("資料已是最新資料")
            return
        delete_table_pm25(conn)
        create_table_pm25(conn)
        for item in datas:
            insert_pm25(conn,item)
        print("資料已更新")


def downloadData():
    def stringToFloat(s):
        try:
            return float(s)
        except:
            return 999.0
    response = requests.get(urlpath)
    if response.status_code == 200:
        print('下載成功')
        data = response.json()
        datas = data["records"]
        importData = [
            (item['Site'], item['county'], stringToFloat(item['PM25']), item['DataCreationDate'], item['ItemUnit']) for
            item in datas]
        return importData

def download_save_to_DataBase():
    importData = downloadData()
    saveToDataBase(importData)

def get_city_name():
    conn = create_connection('pm25.db')
    print("資料庫連線成功")

    sql = ''' 
        SELECT DISTINCT county
        FROM pm25
        '''
    with conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        city_name_list = [row[0] for row in rows]
        return  city_name_list

def get_site_pm25(county):
    conn = create_connection('pm25.db')
    print("資料庫連線成功")

    sql = f''' 
            SELECT DISTINCT site, pm25
            FROM pm25
            WHERE county = "{county}"
            '''

    with conn:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        data_list = [list(row) for row in rows]
        return data_list

def get_site_info(site):
    conn = create_connection('pm25.db')
    print("資料庫連線成功")
    sql = '''
        SELECT  *
        FROM pm25
        WHERE site=? AND pm25=?
        LIMIT 1
        '''
    cursor = conn.cursor()
    #cursor.execute(sql, (site[0],))
    cursor.execute(sql, site)
    rows = cursor.fetchone()
    return {'id':rows[0], '站點':rows[1], '城市':rows[2], 'pm25':rows[3], '日期':rows[4], '單位':rows[5]}

def get_better():
    conn = create_connection('pm25.db')
    print("資料庫連線成功")
    sql = '''
        SELECT  *
        FROM pm25
        WHERE pm25 <= 35
        '''
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows

def get_normal():
    conn = create_connection('pm25.db')
    print("資料庫連線成功")
    sql = '''
        SELECT  *
        FROM pm25
        WHERE pm25 BETWEEN 35 AND 53
        '''
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows

def get_bad():
    conn = create_connection('pm25.db')
    print("資料庫連線成功")
    sql = '''
            SELECT  *
            FROM pm25
            WHERE pm25 > 53
            '''
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    return rows