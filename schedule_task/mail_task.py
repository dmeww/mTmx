#coding=utf-8
import smtplib
from email.mime.text import MIMEText

msg_from='202807403@qq.com'                                 #发送方邮箱
passwd='cboufvgxfkymbibi'                                   #填入发送方邮箱的授权码
msg_to='2670072843@qq.com'                                  #收件人邮箱
                            
subject="python邮件测试"                                     #主题     



def send_mail(info):
    msg = MIMEText(info)
    msg['Subject'] = subject
    msg['From'] = msg_from
    msg['To'] = msg_to

    try:
        s = smtplib.SMTP_SSL("smtp.qq.com",465) #邮件服务器及端口号
        s.login(msg_from, passwd)
        s.sendmail(msg_from, msg_to, msg.as_string())
        print ("邮件发送成功")
    except :
        print ("邮件发送失败")
    finally:
        s.quit()

    return

