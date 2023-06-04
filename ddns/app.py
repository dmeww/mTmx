import requests
import json
import time

config = {
    'hostname':'',
    'token':''
}


try:
    f = open('data.json','r+')
except:
    print('请先进行配置')
    f = open('data.json','w')
    f.write(json.dumps(config))
    f.close()
    exit(0)

config = json.loads(f.read())

f.close()

print(f'配置读取完成 \n{config}')

while True:
    is_err = False
    try:
        ipv6 = requests.get('http://6.ipw.cn',timeout=5).text
    except Exception as e:
        is_err = True
        print('err get ipv6')
    if not is_err:
        print('next change will be in 60s later')
        basic_url = f'http://dynv6.com/api/update?hostname={[config["hostname"]]}&token={config["token"]}&ipv6={ipv6}'
    else:
        print('pass to nect tick')
    time.sleep(50)









