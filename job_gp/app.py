import mail_task
import task

def do_job():
    task.do_task()
    mail_task.send_mail('myTermux','Github Pages 已刷新')




