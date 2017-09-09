from show_auctions import AuctionHouse
import json
import os

def calculate_projected_value():
    # ah = AuctionHouse()
    # emperium_ah_value = ah.list_item_prices(151564, 1000)

    data = json.load(open('resources\empyrium.json'))
    total = 0
    for k, v in data['drop_rate'].iteritems():
        total = total + data['price'][k] * v
    return total

def main():
    print calculate_projected_value()

if __name__ == '__main__':
    main()
