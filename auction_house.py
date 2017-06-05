from datetime import datetime
from api.blizzard import get_auction_data, get_item_data
import config


class AuctionHouse(object):

    def __init__(self):
        self.timestamp = ''
        self.ah_snapshot = None
        self.refresh()

    def refresh(self):
        self.timestamp = datetime.now()
        self.ah_snapshot = get_auction_data()

    def check_undercuts(self):
        # print 'Checking for undercuts...'
        owner_auctions = []
        item_on_sale = set()

        # looking for the owner's auctions
        for auction in self.ah_snapshot['auctions']:
            if auction['owner'] == config.OWNER:
                owner_auctions.append(auction)
                item_on_sale.add(auction['item'])

        if len(item_on_sale) == 0:
            return "It seems that you are not selling anything on the auction house... :("
        else:
            competitors = []
            undercut_items = []
            # looking whether the owner's auctions are undercut
            for auction in self.ah_snapshot['auctions']:
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
                    get_item_data(item)['name'] + '\n')

        return message

    def prices(self, item_list):
        for item in item_list:
            print 0