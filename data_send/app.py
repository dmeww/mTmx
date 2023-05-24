import os,time


host = ''
# 发送 POST 请求到 /data 路由
url = f'http://{host}:5005/data'

data = {}
data['device'] = ''


def get_info():
    # 获取设备 IP V4 信息
    ip_4_info = os.popen("ip addr show wlan0 | grep 'inet ' | awk '{print $2}' | cut -d/ -f1").read().strip()

    ip_6_info = os.popen("ip -6 addr show dev wlan0 | grep -E 'inet6 .* global' | awk '{print substr($2,20)}' | sort -u").read().strip()
    # 获取用户信息
    user_info = os.popen("whoami").read().strip()
    data['ipv4'] = ip_4_info
    data['ipv6'] = ip_6_info
    data['user'] = user_info
    if ip_6_info.__len__() < 5:
        re_open_wifi()
        time.sleep(30)
        get_info()


def re_open_wifi():
    os.system('termux-wifi-enable false')
    os.system('termux-wifi-enable true')



import requests,json

calc = 0
get_info()
while True:
    if calc != 0:
        time.sleep(10*60)
    else:
        calc +=1

    get_info()

    try:
        response = requests.post(url=url, data={'data':json.dumps(data)},timeout=5)
        # 输出响应内容
        print(response.text)
    except:
        pass
    
