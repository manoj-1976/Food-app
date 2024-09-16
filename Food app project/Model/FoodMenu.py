from Model.AbstractItem import AbstractItem
from Model.FoodItem import FoodItem

class FoodMenu(AbstractItem):

    def __init__(self, name):
        super().__init__(name=name)
        self.__FoodItems = []

    @property
    def FoodItems(self):
        return self.__FoodItems

    @FoodItems.setter
    def FoodItems(self,items):
        for item in items:
            if not isinstance(item, FoodItem):
                print("Invalid FoodItems")
                return

        self.__FoodItems = items

    def DisplayItem(self,start):
        print(f"{start} >> {self.Name}")

