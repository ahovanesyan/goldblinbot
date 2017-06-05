import json
import urllib2
import config


def get_auction_data():
    file_url = json.loads(urllib2.urlopen("https://eu.api.battle.net/wow/" + 'auction/data/' + config.REALM +
                                          "?locale=en_GB&apikey=" + config.BLIZZ_API).read())['files'][0]['url']

    return json.loads(urllib2.urlopen(file_url).read())


def get_item_data(item_id):
    return json.loads(urllib2.urlopen("https://eu.api.battle.net/wow/item/" + str(item_id) +
                                      "?locale=en_GB&apikey=" + config.BLIZZ_API).read())