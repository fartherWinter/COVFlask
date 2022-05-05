#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/14 18:25
# @Author  : 陈念
# @File    : utils.py
# @Software: PyCharm
import time
import pymysql

def get_time():
    local_time = time.strftime("%Y{}%m{}%d{} %X")
    return local_time.format("年","月","日")

def get_conn():
    """

    :return: 连接，游标
    """
    #创建连接
    conn = pymysql.connect(host='127.0.0.1',
                           user='root',
                           password='root',
                           db = 'cov',
                           # charset='utf-8'
    )
    #创建游标
    cursor = conn.cursor()#执行完毕返回的结果集默认以元组显示
    return conn,cursor

def close_conn(conn,cursor):
    cursor.close()
    conn.close()

def query(sql,*args):
    """

    :param sql:
    :param args:
    :return:返回查询到结果，（（），（））的形式
    """
    conn,cursor=get_conn()
    cursor.execute(sql,args)
    res = cursor.fetchall()
    close_conn(conn,cursor)
    return res

def get_c1_data():
    """
    :return:返回大屏div id =  c1的数据
    """

    #因为会多次更新数据，所以取时间戳最新的那组数据
    sql = "select confirm ,noInfect," \
          "heal,dead from history " \
          "order by dates desc limit 1"
    res = query(sql)
    return res[0]

def get_c2_data():
    """
    :return:返回各省数据
    """
    sql = 'SELECT province,now_confirm FROM details WHERE id in (select Max(id) from details GROUP BY province)'
        #  "select province,sum(confirm_add) from details " \
        #   "where update_time = (select update_time from details " \
        #   "order by update_time desc limit 1)" \
        #   "group by province"
    res = query(sql)
    return res

def get_l1_data():
    """

    :return: 返回中高风险地区数据
    """
    sql = "select risk,region from regions where date in (SELECT max(date) from regions)"
    res = query(sql)
    return res

def get_l2_data():
    """

    :return: 返回最近5天的数据
    """
    sql = "select dates,confirm,noInfect,heal,dead from history"
    res = query(sql)
    return res

def get_l3_data():
    """

    :return: 返回新增数据
    """
    sql = "select dates,confirm_add,noInfect_add from history"
    res = query(sql)
    return res

def get_r1_data():
    """
    :return: 返回top5确诊的省/地区
    """
    sql = "SELECT province,now_confirm FROM details WHERE id in (select Max(id) from details GROUP BY province) ORDER BY now_confirm desc LIMIT 5"
    res = query(sql)
    return res

def get_r2_data():
    """

    :return: 返回资讯
    """
    sql = 'select title from event order by time desc limit 20'
    res = query(sql)
    return res


if __name__ == '__main__':
    print(get_l1_data())