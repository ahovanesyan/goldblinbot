from pushbullet import PushBullet
from datetime import datetime
# import telegram.ext

import urllib2
import json
import config
import os

def create_resources():
    """
    TODO: this method need to create all missing resource files that are not shipped with the code.
    :return:
    """

class Controller(object):

    def __init__(self):
        self.pb = PushBullet(config.PB_API)

    @staticmethod
    def get_auction_data():
        file_url = json.loads(urllib2.urlopen("https://eu.api.battle.net/wow/" + 'auction/data/' + config.REALM +
                                              "?locale=en_GB&apikey=" + config.BLIZZ_API).read())['files'][0]['url']

        return json.loads(urllib2.urlopen(file_url).read())

    @staticmethod
    def get_item_data(item_id):
        return json.loads(urllib2.urlopen("https://eu.api.battle.net/wow/item/" + str(item_id) +
                                              "?locale=en_GB&apikey=" + config.BLIZZ_API).read())

    def check_undercuts(self, ah_data):
        # print 'Checking for undercuts...'
        # alist, blist, clist, dlist, elist = ([] for i in range(5))
        # ah_data = self.get_auction_data()['auctions']
        # ah_data = data['auctions']
        owner_auctions = []
        item_on_sale = set()

        # looking for the owner's auctions
        for auction in ah_data['auctions']:
            if auction['owner'] == config.OWNER:
                owner_auctions.append(auction)
                item_on_sale.add(auction['item'])

        if len(item_on_sale) == 0:
            message = "It seems that you are not selling anything on the auction house... :("
            return
        else:
            competitors = []
            undercut_items = []
            # looking whether the owner's auctions are undercut
            for auction in ah_data['auctions']:
                if item_on_sale.__contains__(auction['item']) and not undercut_items.__contains__(auction['item']):
                    for oa in owner_auctions:
                        if oa['item'] == auction['item'] and oa['buyout'] > auction['buyout']:
                            # undercut_items.append({'item': auction['item'], 'auction': auction, 'competitor': auction['owner']})
                            competitors.append(auction)
                            undercut_items.append(auction['item'])
                            break

            # print len(undercut_items), ' items have been undercut'
            message = 'The next items have been undercut:\n'
            for item in undercut_items:
                message = message + str(item) + ': ' + str(
                    self.get_item_data(item)['name'] + '\n')

        self.push_message(message)

    @staticmethod
    def save_to_file(json_data, timestamp=datetime.now().strftime("%d-%m-%Y_%H-%M-%S")):
        location = config.WRITE_LOCATION + os.path.sep
        filename = location + 'ah_' + str(config.REALM) + "_" + str(timestamp) + '.json'
        with open(filename, 'w+') as f:
            json.dump(json_data, f)

    def push_message(self, message):
        print message
        self.pb.push_note("Goldblin Bot", message)

    def run(self):
        timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
        data = self.get_auction_data()
        self.save_to_file(data, timestamp=timestamp)
        # self.check_undercuts(data)

if __name__ == '__main__':
    controller = Controller()
    controller.run()

