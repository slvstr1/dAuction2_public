import schedule
import time
import setproctitle
import os

setproctitle.setproctitle("ascheduler")

def job():
       print("I'm working...")
       os.system('python manage.py service')

schedule.every(3).seconds.do(job)

while True:
         schedule.run_pending()
         time.sleep(1)

