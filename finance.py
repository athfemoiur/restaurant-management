# TODO-1: Add Bill class here
# TODO-1: Add Payment class here
# TODO-1: Add .sample() classmethod for Bill and Payment which returns

# an instance:
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
#       to get from input
# TODO-2: Change datetime attr to be assigned automatically in Payment class
# TODO-2: Add jalali_datetime property to the Payment class
# TODO-3: Set valid Payment instance for payment attr in Bill instance
# TODO-3: Add show_unpaid() classmethod to the Bill class which will return a
#       list of all unpaid bills, (Implementation is up to you)
# TODO-3: Add show_paid() classmethod to the Bill as show_unpaid() method
# TODO-3: Add paid_list() classmethod to the Payment class which will just
#       return a list of payments with True `is_paid` flag.
# TODO-3: Add pay() method to the Payment class which set is_paid flag True
# TODO-3: Add total_paid() classmethod to the Payment class which return an int
#       of total paid Payments

import uuid
from datetime import datetime
from khayyam import JalaliDatetime


from lib import Root


class Payment(Root):
    payment_list = []

    def __init__(self, payment_type, price, is_paid=False):
        self.uuid = uuid.uuid4()
        self.payment_type = payment_type
        self.is_paid = is_paid
        self.datetime = datetime.now()
        self.price = price
        self.jalali_datetime = JalaliDatetime.now()
        self.payment_list.append(self)
        super().__init__()

    def pay(self):
        self.is_paid = True

    @classmethod
    def total_paid(cls):
        return sum(pym.price for pym in cls.payment_list if pym.is_paid)

    @classmethod
    def paid_list(cls):
        return list(filter(lambda pym: pym.is_paid, cls.payment_list))

    @classmethod
    def sample(cls, payment_type='cash', price=12,
               is_paid=False):
        return cls(payment_type=payment_type, price=price,
                   is_paid=is_paid)


class Bill(Root):
    bill_list = []

    def __init__(self, total_price, payment_type):
        self.total_price = total_price
        self.payment = Payment(payment_type, total_price)
        self.uuid = uuid.uuid4()
        self.bill_list.append(self)
        super().__init__()

    @classmethod
    def show_unpaid(cls):
        return list(
            filter(lambda bill: not bill.payment.is_paid, cls.bill_list))

    @classmethod
    def show_paid(cls):
        return list(filter(lambda bill: bill.payment.is_paid, cls.bill_list))

    @classmethod
    def sample(cls, total_price=12, payment_type='cash'):
        return cls(total_price=total_price, payment_type=payment_type)
