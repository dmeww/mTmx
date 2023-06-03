from flask import Flask, request, render_template
import json,time

app = Flask(__name__)

# 存储数据的列表
data_list = {}


@app.route('/')
def index():
    return render_template('index.html',datas=data_list)


@app.route('/data', methods=['POST'])
def data():
    data = request.form['data']
    data = json.loads(data)
    data['update'] = time.strftime("%m-%d %H:%M:%S", time.localtime())
    data_list[data['device']] = data
    return 'Data received and stored.'


@app.route('/sms')
def show_sms():
    import os
    sms_list = json.loads(os.popen('termux-sms-list -l 1'))
    return sms_list[0]



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5005,debug=True)