from flask import Flask
from flask import render_template
from flask import jsonify
from jieba.analyse import extract_tags
import utils

app = Flask(__name__)


@app.route('/index')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/time')
def get_time():
    return utils.get_time()

@app.route('/c1')
def get_c1_data():
    data = utils.get_c1_data()
    return jsonify({'confirm':int(data[0]),'noInfect':data[1],'heal':int(data[2]),'dead':int(data[3])})

@app.route('/c2')
def get_c2_data():
    res =[]
    for tup in utils.get_c2_data():
        res.append({'name':tup[0],'value':int(tup[1])})
    return jsonify({'data':res})

@app.route('/l1')
def get_l1_data():
    risk,region = [],[]
    for ri,re in utils.get_l1_data():
        risk.append(ri)
        region.append(re)
    return jsonify({'risk':risk,'region':region})

@app.route('/l2')
def get_l2_data():
    data = utils.get_l2_data()
    day,confirm,noInfect,heal,dead =[],[],[],[],[]
    for d,c,n,h,de in data[7:]:
        day.append(d.strftime('%m-%d'))
        confirm.append(c)
        noInfect.append(n)
        heal.append(h)
        dead.append(de)
    return jsonify({'day':day,'confirm':confirm,'noInfect':noInfect,'heal':heal,'dead':dead})

@app.route('/l3')
def get_l3_data():
    data = utils.get_l3_data()
    day,confirm_add,noInfect_add =[],[],[]
    for d,c,n in data[7:]:
        day.append(d.strftime('%m-%d'))
        confirm_add.append(c)
        noInfect_add.append(n)
    return jsonify({'day':day,'confirm_add':confirm_add,'noInfect_add':noInfect_add})

@app.route('/r1')
def get_r1_data():
    res =[]
    for tup in utils.get_r1_data():
        res.append([tup[0],int(tup[1])])
    return jsonify({'data':res})

@app.route('/r2')
def get_r2_data():
    data = utils.get_r2_data()
    res = []
    num = 21
    for i in data:
        k = i[0]
        v = num * 100  #根据资讯时间设置权重
        num -= 1
        ks = extract_tags(k)  #使用jieba，提取关键字
        for j in ks:
            if not j.isdigit():
                res.append({'name': j, 'value': v})
    return jsonify({'kws':res})

@app.route('/')
def cov():
    return render_template("main.html")

if __name__ == '__main__':
    app.run()
