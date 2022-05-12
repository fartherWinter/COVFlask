#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/4/18 15:33
# @Author  : chen
# @File    : spider.py
# @Software: PyCharm
import json
import traceback
import utils
import time
import requests
import hashlib




def get_tencent_data():
    """

    :return: 返回历史数据和当前数据
    """
    url_det = 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=statisGradeCityDetail,diseaseh5Shelf'
    url_his = 'https://api.inews.qq.com/newsqa/v1/query/inner/publish/modules/list?modules=chinaDayList,chinaDayAddList,nowConfirmStatis,provinceCompare'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    r_det = requests.post(url_det,headers)
    r_his = requests.post(url_his,headers)
    res_det = json.loads(r_det.text)
    res_his = json.loads(r_his.text)
    data_all_det = res_det['data']#['diseaseh5Shelf']
    data_all_his = res_his['data']

    history = {}
    for i in data_all_his['chinaDayList']:
        dates = i['y'] + "." + i['date']
        tup = time.strptime(dates,'%Y.%m.%d')
        dates = time.strftime("%Y-%m-%d", tup) #修改时间格式防止存入数据库时报错
        confirm = i['confirm']
        no_infect = i['noInfect']
        dead = i['dead']
        heal = i['heal']
        history[dates] = {"confirm": confirm, "noInfect": no_infect, "heal": heal, "dead": dead}
    for i in data_all_his['chinaDayAddList']:
        dates = i['y']+ "." + i['date']
        tup = time.strptime(dates, '%Y.%m.%d')
        dates = time.strftime("%Y-%m-%d", tup)
        confirm = i['confirm']
        local_infection_add = i['localinfectionadd']
        dead = i['dead']
        heal = i['heal']
        try:
            history[dates].update({"confirm_add":confirm,"noInfect_add":local_infection_add,
                                   "heal_add": heal,"dead_add":dead})

        except:
            continue
    #data.diseaseh5Shelf.areaTree[0].children[2].total.nowConfirm
    day_details = []
    update_time = data_all_det['diseaseh5Shelf']['lastUpdateTime']
    data_province = data_all_det["diseaseh5Shelf"]['areaTree'][0]['children']
    for pro_infos in data_province:
        province = pro_infos['name']
        now_confirm = pro_infos['total']['nowConfirm']
        for pro_city_infos in pro_infos['children']:
            city = pro_city_infos['name']
            confirm = pro_city_infos['total']['confirm']
            confirm_add = pro_city_infos['today']['confirm']
            heal = pro_city_infos['total']['heal']
            dead = pro_city_infos['total']['dead']
            day_details.append([update_time,province,city,confirm,now_confirm,confirm_add,heal,dead])
    return history,day_details

def update_details():
    """
    更新details
    :return:
    """
    cursor= None
    conn = None
    try:
        li = get_tencent_data()[1]
        print(f'{time.asctime()}开始更新最新数据')
        conn,cursor = utils.get_conn()
        sql = "insert into details(update_time,province,city,confirm,now_confirm,confirm_add,heal,dead) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        sql_query = "select %s = (select update_time from details order by id desc limit 1)"
        cursor.execute(sql_query,li[0][0])
        if not cursor.fetchone()[0]:
            print(f'{time.asctime()}更新数据完毕')
            for item in li:
                cursor.execute(sql,item)
            conn.commit()#提交事务 update delete insert 操作
        else:
            print(f'{time.asctime()}已是最新数据')

    except:
        traceback.print_exc()
    finally:
        utils.close_conn(conn,cursor)

def insert_history():
    """
    插入数据
    :return:
    """
    cursor= None
    conn = None
    try:
        dic = get_tencent_data()[0]
        print(f'{time.asctime()}开始插入历史数据')
        conn,cursor = utils.get_conn()
        sql = "insert into history values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        for k,v in dic.items():
            cursor.execute(sql,[k,v.get('confirm'),v.get('confirm_add'),
                v.get('noInfect'),v.get('noInfect_add'),v.get('heal'),
                v.get('heal_add'),v.get('dead'),v.get('dead_add')])
        conn.commit()#提交事务 update delete insert 操作
        print(f'{time.asctime()}已是最新数据')

    except:
        traceback.print_exc()
    finally:
        utils.close_conn(conn,cursor)


def update_history():
    """
    更新历史数据
    :return:
    """
    cursor= None
    conn = None
    try:
        dic = get_tencent_data()[0]
        print(f'{time.asctime()}开始更新历史数据')
        conn,cursor = utils.get_conn()
        sql = "insert into history(dates,confirm,confirm_add,noInfect,noInfect_add,heal,heal_add,dead,dead_add) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        sql_query = "select confirm from history where dates = %s"
        for k,v in dic.items():
            if not cursor.execute(sql_query,k):
                cursor.execute(sql,[k,v.get('confirm'),v.get('confirm_add'),
                                    v.get('noInfect'),v.get('noInfect_add'),v.get('heal'),
                                    v.get('heal_add'),v.get('dead'),v.get('dead_add')])

        conn.commit()#提交事务 update delete insert 操作
        print(f'{time.asctime()}历史数据更新完毕')

    except:
        traceback.print_exc()
    finally:
        utils.close_conn(conn,cursor)


def get_baidu_data():
    url = 'https://opendata.baidu.com/data/inner'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }
    data = {
        "tn": "reserved_all_res_tn",
        "dspName": "iphone",
        "from_sf": 1,
        "dsp": "iphone",
        "resource_id": "28565",
        "alr": 1,
        "query": "国内新型肺炎最新动态",
        "cb": "jsonp_1650291778879_54482"
    }
    res = requests.post(url,headers=headers,data =data).text
    res = res.replace('jsonp_1650291778879_54482(',"").replace(")","")
    res = json.loads(res)
    res_event = res['Result'][0]['DisplayData']['result']

    event=[]
    for i in res_event['items']:
        event_title = i['eventDescription']
        event_url = i['eventUrl']
        event_time = time.localtime(int(i['eventTime']))
        event_time = time.strftime("%Y-%m-%d %X",event_time)
        event.append([event_time,event_title,event_url])
    return event

def update_event():
    """
    将更新的资讯插入数据库
    :return:
    """
    cursor = None
    conn = None
    try:
        event = get_baidu_data()
        print(f'{time.asctime()}开始更新资讯')
        conn,cursor = utils.get_conn()
        sql = 'insert into event(time,title,url) values(%s,%s,%s)'
        for i in event:
            cursor.execute(sql,i)
        conn.commit()
        print(f'{time.asctime()}数据更新完毕')

    except:
        traceback.print_exc()
    finally:
        utils.close_conn(conn,cursor)


def get_weijian_data():
    url = 'http://103.66.32.242:8005/zwfwMovePortal/interface/interfaceJson'
    t1 = format(time.time()/1000,'.3f')
    t2 = t1.replace('.','')
    token = '23y0ufFl5YxIyGrI8hWRUZmKkvtSjLQA'
    noce = "123456789abcdefg"
    params = "3C502C97ABDA40D0A60FBEE50FAAD1DA"
    n = 'fTN2pfuisxTavbTuYVSsNJHetwq5bJvC'
    xwn = 'QkjjtiLM2dCratiA'
    v = str(t2+token+noce+t2).encode('utf8')
    signatureHeader = hashlib.sha256(v).hexdigest().upper()
    xws = hashlib.sha256(str(t2+n+xwn+t2).encode('utf8')).hexdigest().upper()

    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
        "Host": "bmfw.www.gov.cn",
        'Origin': "http://bmfw.www.gov.cn",
        'Referer': "http://bmfw.www.gov.cn/",
        'x-wif-nonce': xwn,
        'x-wif-paasid': 'smt-application',
        'x-wif-signature': xws,
        'x-wif-timestamp': t2
    }


    # signatureHeader = signatureHeader.decode('utf-8')
    data = {
        "appId": "NcApplication",
        "key": params,
        "nonceHeader": noce,
        "paasHeader": "zdww",
        "signatureHeader": signatureHeader,
        "timestampHeader": t2
    }
    res = requests.post(url,headers=headers,data=json.dumps(data)).json()
    update_time = res['data']['end_update_time']
    res1 = res['data']['highlist']
    res2 = res['data']['middlelist']
    risk,risk_h,risk_m = [],[],[]
    for i in res1:
        type = '高风险'
        for com in i['communitys']:
            risk_h.append([update_time,type,i['area_name']+com])
    for i in res2:
        type = '中风险'
        for com in i['communitys']:
            risk_m.append([update_time,type,i['area_name']+com])

    return risk_h,risk_m

def update_weijian():
    """
    将更新的中高风险地区插入数据库
    :return:
    """
    cursor = None
    conn = None
    try:
        risk_h,risk_m = get_weijian_data()
        print(f'{time.asctime()}开始更新中高风险地区')
        conn,cursor = utils.get_conn()
        sql = 'insert into regions(date,risk,region) values(%s,%s,%s)'
        sql_query = 'select %s = (select date from regions order by id desc limit 1 )'
        cursor.execute(sql_query,risk_h[0][0])
        if not cursor.fetchone()[0]:
            for i in risk_h:
                cursor.execute(sql,i)
            for i in risk_m:
                cursor.execute(sql,i)
            conn.commit()
            print(f'{time.asctime()}数据更新完毕')
        else:
            print(f'{time.asctime()}已是最新数据')
    except:
        traceback.print_exc()
    finally:
        utils.close_conn(conn,cursor)







if __name__ == '__main__':
   l =len(sys.argv)
    if l == 1:
        s = """
        输入参数
        参数说明：
        up_his:更新历史表
        up_event:更新资讯表
        up_det:更新每日详情
        up_reg:更新风险地区
        """
        print(s)
    else:
        order = sys.argv[1]
        if order== 'up_his':
            update_history()
        elif order=='up_det':
            update_details()
        elif order=='up_event':
            update_event()
        elif order=='up_reg':
            update_weijian()
