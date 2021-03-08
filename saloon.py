# TODO-1: Add Table class here
# TODO-1: Add .sample() classmethod for Table which returns  an instance:
# for example:
#    class Test:
#         def __init__(self, name, number):
#             self.name = name
#             self.number = number
#
#         @classmethod
#         def sample(cls):
#             return cls(name='ali', number=10)
import uuid
from lib import Root


class Table(Root):
    table_list = []

    def __init__(self, capacity, number, reserved=False, is_available=True):
        self.uuid = uuid.uuid1()
        self.capacity = capacity
        self.number = number
        self.reserved = reserved
        self.is_available = is_available
        self.table_list.append(self)
        super().__init__()

    @classmethod
    def sample(cls, capacity=6, number=1, reserved=False, is_available=True):
        return cls(capacity=capacity, number=number, reserved=reserved,
                   is_available=is_available)


