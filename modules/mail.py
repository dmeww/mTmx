import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

# 发件人邮箱账号
my_sender = '202807403@qq.com'  
# 发件人邮箱授权码
my_pass = 'tumumevvmspdbiad'  
# 收件人邮箱账号 
my_user = '2670072843@qq.com'  


def sendMail(Subject, Content, From):
    ret = True 
    try:
        # 发送的内容
        msg = MIMEText(Content, 'plain', 'utf-8')
        # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['From'] = formataddr([From, my_sender])  
        # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['To'] = formataddr(["Master", my_user])  
        msg['Subject'] = Subject  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25/465
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱授权码
        # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.sendmail(my_sender, [my_user, ], msg.as_string())
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret
