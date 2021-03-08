# TODO-3: Create Manager class which has _class attr and search() method
# TODO-3: Implement complete search method functionality in the way you prefer
# TODO-3: `_class` attr in manager is type of composite class
# TODO-3: Add Root class and set manager class_attr None in it
# TODO-3: Add set_manager() method to the Root which set type of self to the
#       `_class` attr of instance manager

# TODO-3: Change sample() method all over your code as follows:
#    class Test:
#         def __init__(self, name, number):
#             self.name = name
#             self.number = number
#
#         @classmethod
#         def sample(cls, name='ali', number=10):
#             return cls(name=name, number=number)
# TODO-3: Add <class-name-lowercase>_list class_attr to the all classes except
#       Manager() and Root() classes

from abc import ABC


class Manager:
    def __init__(self, cls):
        self._class = cls

    def search(self, **kwargs):
        class_name = self._class.__name__.lower()
        obj_list = getattr(self._class, class_name+"_list")
        preferred = []

        for obj in obj_list:
            if all(hasattr(obj, atr) for atr in kwargs):
                if list(map(lambda atr: getattr(obj, atr), kwargs)) == list(
                        kwargs.values()):
                    preferred.append(obj)
            else:
                print('Invalid input')
                return None

        return preferred


class Root(ABC):
    manager = None

    def __init__(self):
        self.set_manager()

    @classmethod
    def set_manager(cls):
        if cls.manager is None:
            cls.manager = Manager(cls)
