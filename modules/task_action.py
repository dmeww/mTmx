from modules.mail import sendMail
import os


def sendBattery():
    r = os.popen('termux-battery-status')
    sendMail('电量通知',r.read(),'Tab S7')
    

def sendIPAddress():
    r = os.popen('ifconfig')
    sendMail('IP Address',r.read(),'Tab S7')
