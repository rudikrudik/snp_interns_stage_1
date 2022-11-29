from task_11 import Dessert


class JellyBean(Dessert):

    def __init__(self, flavor=None):
        super().__init__()
        self._flavor = flavor

    @property
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, value):
        self._flavor = value

    def is_delicious(self):
        return self._flavor != 'black licorice'