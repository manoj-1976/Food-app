from turtledemo.penrose import start

from Model.AbstractItem import AbstractItem
from Model.FoodMenu import FoodMenu
class Restaurant(AbstractItem):

    def __init__(self, name, rating, location, offer):
        super().__init__(name=name,rating=rating)
        self.Location = location
        self.Offer = offer
        self.FoodMenu = None

        @property
        def FoodMenu(self):
            return self.__FoodItems

        @FoodMenu.setter
        def FoodMenu(self, items):
            for item in items:
                if not isinstance(items, FoodMenu):
                    print("Invalid FoodMenu")
                    return

            self.__FoodItems = items

    def DisplayItem(self,start):
        print(f"{start} >> {self.Name} => Rating : {self.Rating}")
