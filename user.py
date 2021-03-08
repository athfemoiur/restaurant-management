# TODO-1: Add Supervisor class Here
# TODO-1: Add .sample() classmethod for Supervisor which returns an instance:
# for example:
#    class Test:
#         def __init__(self, name, number):
#             self.name = name
#             self.number = number
#
#         @classmethod
#         def sample(cls):
#             return cls(name='ali', number=10)
from lib import Root


class Supervisor(Root):
    supervisor_list = []

    def __init__(self, username, password, phone_number):
        self.username = username
        self.password = password
        self.phone_number = phone_number
        self.supervisor_list.append(self)
        super().__init__()

    @classmethod
    def sample(cls, username='Amir', password=83456,
               phone_number='09349823402'):
        return cls(username=username, password=password,
                   phone_number=phone_number)
