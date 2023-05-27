import mail_task
import task

def do_refresh():
    task.do_task()
    mail_task.send_mail('myTermux','Github Pages 已刷新')




