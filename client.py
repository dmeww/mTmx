import os,time


host = ''
# 发送 POST 请求到 /data 路由
url = f'http://{host}:5005/data'

data = {}
data['device'] = ''


def get_info():
    # 获取设备 IP V4 信息
    ip_4_info = os.popen("ip addr show wlan0 | grep 'inet ' | awk '{print $2}' | cut -d/ -f1").read().strip()

    ip_6_info = os.popen("ip -6 address show wlan0 | awk '/inet6/ {print $2}' | grep -v 'fe80'").read().strip()
    # 获取用户信息
    user_info = os.popen("whoami").read().strip()
    data['ipv4'] = ip_4_info
    data['ipv6'] = ip_6_info
    data['user'] = user_info


import requests,json

calc = 0

while True:
    if calc < 20:
        # 刚启动一会，多次刷新
        time.sleep(5)
        calc+=1
    else:
        # 稳定运行后，1小时1更新
        time.sleep(3600)
        calc=1
    get_info()

    try:
        response = requests.post(url=url, data={'data':json.dumps(data)},timeout=5)
        # 输出响应内容
        print(response.text)
    except:
        pass
    
