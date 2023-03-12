
import os
import json


class SysInfo(object):
    def __init__(self, device) -> None:
        self.device = device
        self.info = {}

    def getInfo(self):
        try:
            self.info.__setitem__('battery', getBattery())
        except:
            print('battery error')
        try:
            self.info.__setitem__('os', getOSType())
        except:
            print('os error')
        try:
            self.info.__setitem__('user', getUser())
        except:
            print('user error')
        try:
            self.info.__setitem__('ip', getIPaddress())
        except:
            print('ip error')
        try:
            self.info.__setitem__('disk', getDiskinfo())
        except:
            print('disk error')
        try:
            self.info.__setitem__('mem', getMemoryUsage())
        except:
            print('mem error')
        try:
            self.info.__setitem__('cpu', getCPUinfo())
        except:
            print('cpu error')

        self.info.__setitem__('device', self.device)

    def __str__(self) -> str:
        return f'{self.device} : {self.info}'


def getBattery():
    r = os.popen('termux-battery-status')
    j = json.loads(r.read())
    return j['percentage']


def getOSType():
    r = os.popen('neofetch | grep OS')
    rs = r.read()
    rss = rs.split(':')
    return rss[1].replace('\x1b[0m', '')


def getCPUinfo():
    r = os.popen('neofetch | grep CPU')
    rs = r.read()
    rss = rs.split(':')
    return rss[1].replace('\x1b[0m', '')


def getUser():
    r = os.popen('whoami')
    return r.read().replace('\x1b[0m', '')


def getIPaddress():
    r = os.popen('ifconfig | grep inet')
    rs = r.read()
    rsx = rs.split('\n')
    rsx.pop()
    rss = []

    for ip_str in rsx:
        ip = ip_str.strip().split(' ')[1]
        rss.append(ip)

    return rss


def getDiskinfo():
    r = os.popen('df -h | grep /storage/emulated')
    rs = r.read().strip()
    rsx = rs.split('  ')
    return f'Total: {rsx[4]} Used: {rsx[5]}'.replace('\x1b[0m', '')


def getMemoryUsage():
    r = os.popen('neofetch | grep Memory')
    rs = r.read()
    rs = rs.strip()
    rsx = rs.split(' ')
    return f'{rsx[1]} {rsx[2]} {rsx[3]}'.replace('\x1b[0m', '')


if __name__ == '__main__':
    sys = SysInfo('Samsung Galaxy Tab S7')
    sys.getInfo()
    print(sys.info)
