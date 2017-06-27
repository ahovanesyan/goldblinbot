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

    def list_auctions(self, item_name, max_buyout, min_quantity):
        """
            List all auctions for a specific item with a given maximum and minimum buyout
        """
        self.refresh()
        items = []
        for auction in self.ah_snapshot['auctions']:
            if auction['item'] == item_name and auction['quantity'] >= min_quantity \
                    and auction['buyout']/auction['quantity'] < max_buyout:
                items.append((auction['buyout']/(auction['quantity'] * 100), auction['quantity']))
        items.sort(key=lambda x: x[0])
        return items

    def list_item_prices(self, item_id, tail_size):
        """
        List the price of an item looking at the X cheapest items. With tail_size being the X.
        :param item_id: The id of the item
        :param tail_size: The number of cheapest items to look at.
        :return: price as double
        """
        prices = []

        # get all item_id from the snapshot
        for auction in self.ah_snapshot['auctions']:
            if auction['item'] == item_id and auction['buyout'] != 0:
                # if auction['item'] not in prices:
                #     prices[auction['item']] = [(round(auction['buyout']/(auction['quantity'] * 10000.0), 2), auction['quantity'])]
                # else:
                #     prices[auction['item']].append((round(auction['buyout']/(auction['quantity'] * 10000.0), 2), auction['quantity']))
                prices.append((round(auction['buyout']/(auction['quantity'] * 10000.0), 2), auction['quantity']))

        # for price_listing in prices:
        #     print prices[price_listing]
        #     prices[price_listing].sort(key=lambda x: x[0])
        prices.sort(key=lambda x: x[0])
        return self._filter_auction_set(prices, tail_size)

    def _filter_auction_set(self, auction_set, tail_size):
        if tail_size <= 0 or auction_set == []:
            return 0

        rest = tail_size
        total = 0.0
        auctions_buying = []
        for auction in auction_set:
            if rest > 0:
                if auction[1] <= rest:
                    total = total + auction[0] * auction[1]
                    rest = rest - auction[1]
                    auctions_buying.append(auction)
                else:
                    total = total + auction[0] * rest
                    rest = 0
                    auctions_buying.append(auction)
            else:
                break

        print auctions_buying
        if rest != 0:
            return total/(tail_size - rest)
        else:
            return total/tail_size

if __name__ == '__main__':
    ah = AuctionHouse()
    # print ah.list_auctions(123919, 700000, 50)
    print ah.list_item_prices(123919, 1000)
    # au = [(12, 1), (13, 1), (14, 0)]
    # print ah._filter_auction_set(au, 0)