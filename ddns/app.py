import requests
import json
import time

from timer_task.job_gp import mail_task

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

last_v6 = '_'
while True:
    is_err = False
    res = 'DDNS 更新结果\n'
    try:
        ipv6 = requests.get( 'http://6.ipw.cn' , timeout=5 ).text
    except Exception as e:
        is_err = True
        print('err get ipv6')
        res += 'err get ipv6'
    if not is_err:
        if last_v6 != ipv6:
            print('ipv6 changed')
            last_v6 = ipv6
            basic_url = f'http://dynv6.com/api/update?hostname={config["hostname"]}&token={config["token"]}&ipv6={ipv6}'
            res += requests.get(basic_url).text
            print(res)
            mail_task.send_mail('DDNS',res)
    else:
        print('get v6 err')
    time.sleep(60)









