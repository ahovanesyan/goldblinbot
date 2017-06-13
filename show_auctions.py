import schedule
import main
import time
from datetime import datetime
from urllib2 import HTTPError
from auction_house import AuctionHouse
from item_db import Items


class UpdatedList:

    def __init__(self):
        self.jobs_counter = 0
        self.ah = AuctionHouse()
        self.item_db = Items

    def job(self):
        print 'Current job: ', self.jobs_counter
        print "Starting job at", str(datetime.now())
        for i in self.ah.list_auctions(123919, 400000, 50):
            print i
        self.jobs_counter = self.jobs_counter + 1
        print "Ended job at", str(datetime.now())

    def run(self):
        self.job()  # run once the initial time
        schedule.every(5).minutes.do(self.job)
        while True:
            try:
                schedule.run_pending()
                time.sleep(60)
            except KeyboardInterrupt:
                print 'interrupted'
                break
            except HTTPError:
                pass

if __name__ == '__main__':
    print "Starting program at", str(datetime.now())
    sch = UpdatedList()
    sch.run()
