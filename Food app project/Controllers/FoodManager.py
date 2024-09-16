from  Model.FoodItem import FoodItem
from Model.FoodMenu import FoodMenu
from Model.Restaurant import Restaurant
class FoodManager:

    def __init__(self):
        self.Restaurants = self.__PrepareRestaurant()
        self.FoodItems = self.__PrepareFoodItems()
        self.FoodMenus = self.__PrepareFoodMenues()

    def __PrepareFoodItems(self):
        item1 = FoodItem(name="VegBiriyani",rating=4,price=150,description="***")
        item2 = FoodItem(name="ChickenBiriyani",rating=4.2,price=200,description="***")
        item3 = FoodItem(name="Parota",rating=4.3,price=50,description="***")
        item4 = FoodItem(name="Noodles",rating=4.4,price=250,description="***")
        item5 = FoodItem(name="Dosa",rating=3.8,price=80,description="***")
        return [item1,item2,item3,item4,item5]

    def __PrepareFoodMenues(self):
        FoodItems = self.__PrepareFoodItems()
        menu1 = FoodMenu("Veg")
        menu1.FoodItems = [FoodItems[0],FoodItems[4]]
        menu2 = FoodMenu("Non-Veg")
        menu2.FoodItems = [FoodItems[1],FoodItems[2]]
        menu3 = FoodMenu("chinese")
        menu3.FoodItems = [FoodItems[3]]
        return [menu1,menu2,menu3]

    def __PrepareRestaurant(self):
        FoodMenus = self.__PrepareFoodMenues()
        res1 = Restaurant(name="A2B",rating=4.6, location='CBE',offer=10)
        res1.FoodMenus = [FoodMenus[0]]
        res2 = Restaurant(name="Anbu",rating=4.5, location='CBE',offer=15)
        res2.FoodMenus = [FoodMenus[0],FoodMenus[1]]
        res3 = Restaurant(name="Frends",rating=5, location='CBE',offer=20)
        res3.FoodMenus = [FoodMenus[1],FoodMenus[2]]
        return [res1,res2,res3]

    def FindRestaurent(self, name):
        for res in self.Restaurants:
            if res.Name == name:
                return res

    def FindFoodName(self, name):
        for res in self.FoodItems:
            if res.Name == name:
                return res