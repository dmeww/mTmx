import schedule
import time
import datetime

import mail_task
import task

def job():
    task.do_task()
    with open('nohup.out','r') as f:
        mail_task.send_mail(f.read())
        f.seek(0)
        f.truncate()

# 计算下一次定时任务的时间
def calculate_next_run_time():
    now = datetime.datetime.now()
    target_time = datetime.datetime(now.year, now.month, now.day, 19, 0, 0)
    if now >= target_time:
        target_time += datetime.timedelta(days=1)
    return target_time

# 定义定时任务
schedule.every().day.at('19:00').do(job)

# 计算下一次定时任务的时间
next_run_time = calculate_next_run_time()
print(f'下一次定时任务将在 {next_run_time} 执行')

# 循环执行定时任务
while True:
    schedule.run_pending()
    time.sleep(1)
    now = datetime.datetime.now()
    if now >= next_run_time:
        # 计算下一次定时任务的时间
        next_run_time = calculate_next_run_time()
        print(f'下一次定时任务将在 {next_run_time} 执行')