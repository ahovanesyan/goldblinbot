import json
from api.blizzard import get_item_data


class Items:
    """
    Items module used to gather and store information about items
    """

    def __init__(self):
        """
            Init object.
        """
        self.items = json.load(open('resources/items.json'))

    def get(self, item_id):
        """
            Gets the item name from json memory if exists, otherwise requests it from blizz api and saves it.
        """
        if item_id in self.items:
            return self.items[item_id]
        else:
            item_name = get_item_data(item_id)['name']
            self.items[item_id] = item_name
            self.save()
            return item_name

    def save(self):
        """
            Write the current items data to file.
        """
        with open('resources/items.json', 'w') as f:
            json.dump(self.items, f)

#
# a = Items()
# print '22279' in a.items
# print a.get('22279')
