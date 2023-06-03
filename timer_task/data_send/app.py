import os,time,requests
import requests,json

data = {}

re_try = 0


def get_info():
    ip_6_info = ''

    while True:
        try:
            req = requests.get('http://6.ipw.cn')
        except:
            re_open_wifi()
            time.sleep(10)
            continue
        resp = req.text
        if resp.__len__() == 0:
            re_open_wifi()
            time.sleep(10)
        else:
            ip_6_info = resp
            break
    
    # 获取设备 IP V4 信息
    ip_4_info = os.popen("ip addr show wlan0 | grep 'inet ' | awk '{print $2}' | cut -d/ -f1").read().strip()

    # ip_6_info = os.popen("ip -6 addr show dev wlan0 | grep -E 'inet6 .* global' | awk '{print substr($2,20)}' | sort -u").read().strip()

    # 获取用户信息
    user_info = os.popen("whoami").read().strip()
    data['ipv4'] = ip_4_info
    data['ipv6'] = ip_6_info
    data['user'] = user_info
        


def re_open_wifi():
    if re_try ==5:
        re_try = 0
        time.sleep( 6 * 60 * 60 )
    os.system('termux-wifi-enable false')
    os.system('termux-wifi-enable true')
    re_try += 1


    
def do_send(host:str,device:str):
    url = f'http://{host}:5005/data'
    data['device'] = device
    get_info()
    try:
        response = requests.post(url=url, data={'data':json.dumps(data)},timeout=5)
        # 输出响应内容
        print(response.text)
    except:
        pass
    pass