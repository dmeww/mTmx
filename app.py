from modules.task import Task
import time


tasks = []

a = Task('battery')
b = Task('ip')

tasks.append(a)
tasks.append(b)

while True:
    for task in tasks:
        res = task.doCheck()
        if res:
            task.doTask()
    time.sleep(60)
