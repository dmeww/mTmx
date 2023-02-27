from modules.mail import sendMail
import os


def sendBattery():
    print('Send Battery')

def sendIPAddress():
    r = os.popen('ipconfig')
    sendMail('IP Address',r.read(),'Windows')
