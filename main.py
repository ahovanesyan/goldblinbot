from pushbullet import PushBullet

import urllib2
import json
import secret


def get_data(url):
    return json.loads(urllib2.urlopen(url).read())


def main():
    # alist, blist, clist, dlist, elist = ([] for i in range(5))
    pb = PushBullet(secret.PB_API)
    file_url = json.loads(urllib2.urlopen("https://eu.api.battle.net/wow/auction/data/"+secret.REALM+"?locale=en_GB&apikey="+secret.BLIZZ_API).read())
    ah_data = json.loads(urllib2.urlopen(file_url['files'][0]['url']).read())
    print 'received data'
    owner_actions = []
    item_on_sale = set()
    # looking for the owner's auctions
    for auction in ah_data['auctions']:
        if auction['owner'] == secret.OWNER:
            owner_actions.append(auction)
            item_on_sale.add(auction['item'])

    if len(item_on_sale) == 0:
        message = "It seems that you are not selling anything on the auction house... :("
        print message
        return
    else:
        competitors = []
        undercut_items = []
        # looking whether the owner's auctions are undercut
        for auction in ah_data['auctions']:
            if item_on_sale.__contains__(auction['item']) and not undercut_items.__contains__(auction['item']):
                for oa in owner_actions:
                    if oa['item'] == auction['item'] and oa['buyout'] > auction['buyout']:
                        # undercut_items.append({'item': auction['item'], 'auction': auction, 'competitor': auction['owner']})
                        competitors.append(auction)
                        undercut_items.append(auction['item'])
                        break

        print len(undercut_items), ' items have been undercut'
        message = 'The next items have been undercut:\n'
        for item in undercut_items:
            message = message + str(item) + ': ' + str(get_data('https://eu.api.battle.net/wow/item/'+str(item)+'?locale=en_GB&apikey='+secret.BLIZZ_API)['name']+'\n')

    print message
    # get the item data
    # item_data = get_data('https://eu.api.battle.net/wow/item/', ,'?locale=en_GB&apikey='+secret.BLIZZ_API)

    # send message over pushbullet
    pb.push_note("Goldblin Bot", message)

if __name__ == '__main__':
    main()
