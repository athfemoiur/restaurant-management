# TODO-2: Add Discount class here

from lib import Root


class Discount(Root):
    discount_list = []

    def __init__(self, code, count, start_date, end_date, percentage,
                 maximum_order, minimum_order):
        self.code = code
        self.count = count
        self.start_date = start_date
        self.end_date = end_date
        self.percentage = percentage
        self.maximum_order = maximum_order
        self.minimum_order = minimum_order
        self.discount_list.append(self)
        super().__init__()

    @classmethod
    def sample(cls, code=1345, count=8, start_date=13, end_date=17,
               percentage=25, maximum_order=200, minimum_order=40):
        return cls(code=code, count=count, start_date=start_date,
                   end_date=end_date, percentage=percentage,
                   maximum_order=maximum_order, minimum_order=minimum_order)


print(Discount.__name__)
