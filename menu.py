# TODO-1: Add Item class here
# TODO-1: Add .sample() classmethod for Item which returns an instance:
# for example:
#    class Test:
#         def __init__(self, name, number):
#             self.name = name
#             self.number = number
#
#         @classmethod
#         def sample(cls):
#             return cls(name='ali', number=10)

# TODO-2: Add item_id to the Item class, item_id should be auto incremental
# TODO-2: item_types should be one of (f, s or b) for Food, Starter or Beverage
# TODO-2: Change datetime attr to be assigned automatically in Item class
# TODO-2: Add jalali_datetime property to the Item class
# TODO-3: Add show_menu() classmethod to the Item class which will print all
#       items in the menu
# TODO-3: Add prompt() method to the Item class which will get proper dict for
#       creating each single item from user input and return data

import uuid
from khayyam import JalaliDatetime
from datetime import datetime
from lib import Root


class Item(Root):
    item_id = 0
    item_list = []
    food_list = []
    starter_list = []
    beverage_list = []

    def __init__(self, name, item_type, price):
        self.uuid = uuid.uuid1()
        self.name = name
        self.item_type = item_type
        self.type_handler(self, item_type)
        self.price = price
        self.datetime = datetime.now()
        self.jalali_datetime = JalaliDatetime.now()
        self.item_id = self.id_generator()
        self.item_list.append(self)
        super().__init__()

    @classmethod
    def id_generator(cls):
        cls.item_id += 1
        return cls.item_id

    @classmethod
    def type_handler(cls, itm,  item_type):
        if item_type == 'f':
            cls.food_list.append(itm.name)
        elif item_type == 's':
            cls.starter_list.append(itm.name)
        elif item_type == 'b':
            cls.beverage_list.append(itm.name)

    @classmethod
    def show_menu(cls):
        for itm in [*cls.food_list, *cls.starter_list, *cls.beverage_list]:
            print(itm)

    @classmethod
    def prompt(cls, data_dict):
        return list(data_dict.values())

    @classmethod
    def sample(cls, name='pizza', item_type='f', price=12):
        return cls(name=name, item_type=item_type, price=price)
