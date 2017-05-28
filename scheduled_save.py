import schedule
import main
import time
from datetime import datetime

class SaveScheduler:

    def __init__(self):
        self.controller = main.Controller()
        self.jobs_counter = 0

    def job(self):
        print 'Current job: ', self.jobs_counter
        print "Starting job at", str(datetime.now())
        self.controller.run()
        self.jobs_counter = self.jobs_counter + 1
        print "Ended job at", str(datetime.now())

    def run(self):
        schedule.every(3).minutes.do(self.job)
        try:
            while True:
                schedule.run_pending()
                time.sleep(60)
        except KeyboardInterrupt:
            print 'interrupted'


if __name__ == '__main__':
    sch = SaveScheduler()
    sch.run()
