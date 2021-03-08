# TODO-1: Add Order model here
# TODO-1: Add .sample() classmethod for Order which returns an instance:
# for example:
#    class Test:
#         def __init__(self, name, number):
#             self.name = name
#             self.number = number
#
#         @classmethod
#         def sample(cls):
#             return cls(name='ali', number=10)
# TODO-2: Replace all uuid attrs with uuid.uuid4() method and prevent class
# TODO-2: Add jalali_datetime property to the Order class
# TODO-2: uuid and datetime attrs should be assigned automatically
# TODO-2: Store a list of orders and a list for un_paid_orders
# TODO-2: Add set_bill method to the Order class which create proper Bill
#       instance according to the items in the order
# TODO-2: Add assign_table method to the Order class which assign table to the
#       client and change the table status
# TODO-2: Set I/O for in_out option in Order class
import uuid
from datetime import datetime
from finance import Bill
from lib import Root
from saloon import Table
from khayyam import JalaliDatetime


class Order(Root):
    orders = []
    un_paid_orders = []
    order_list = []

    def __init__(self, item_dict, in_out, payment_type='cash', table=None):
        self.uuid = uuid.uuid4()
        self.item_dict = item_dict
        self.in_out = in_out
        self.bill = self.set_bill(payment_type)
        self.table = table
        self.datetime = datetime.now()
        self.jalali_datetime = JalaliDatetime.now()
        self.order_list.append(self)
        super().__init__()

    def set_bill(self, payment_type):
        total_price = sum(
            itm.price * count for itm, count in self.item_dict.items())
        return Bill(total_price, payment_type)

    def assign_table(self, capacity, number):
        self.table = Table(capacity, number, True, False)

    @classmethod
    def sample(cls, item_dict={}, in_out='in', payment_type='cash'):
        return cls(item_dict=item_dict, in_out=in_out,
                   payment_type=payment_type)
