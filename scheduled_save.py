import schedule
import main
import time


class SaveScheduler:

    def __init__(self):
        self.controller = main.Controller()
        self.jobs_counter = 0

    def job(self):
        print 'Current job: ', self.jobs_counter
        self.sch.run()
        self.jobs_counter = self.jobs_counter + 1

    def run(self):
        schedule.every(1).minute.do(self.job)
        try:
            while True:
                schedule.run_pending()
                time.sleep(10)
        except KeyboardInterrupt:
            print 'interrupted'

if __name__ == '__main__':
    sch = SaveScheduler()
    sch.run()
