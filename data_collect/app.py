from flask import Flask, request, render_template
import json
import time
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
    data['update'] = time.strftime("%m-%d %H:%M:%S", time.localtime(data['update']))
    data_list[data['device']] = data
    return 'Data received and stored successfully!'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5005,debug=True)