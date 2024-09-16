from Controllers.FoodManager import FoodManager
from Model.Cart import Cart

class MainMenu:

    __Options = {1:"Show Restaurant",2:"Show FoodItems",3:"Search Restaurant"}

    def ShowRestaurant(self):
        for i,res in enumerate(self.__FoodManager.Restaurants,1):
            res.DisplayItem(i)

        choice = int(input("Please Select the Restaurant: "))
        res = self.__FoodManager.Restaurants[choice-1]
        self.ShowFoodMenu(res.FoodMenus)

    def ShowFoodItems(self, FoodItem = None):
        if FoodItem is not None:
            for i,fooditem in enumerate(FoodItem,1):
                fooditem.DisplayItem(i)

            choices = list(map(int,input("Place select your Food items (eg: 1,2)").split(",")))
            cart = Cart(FoodItem,choices)
            cart.ProcessOrder(FoodItem)

        else:
            for fi in self.__FoodManager.FoodItems:
                print(f"{fi.Name} => Rating : {fi.Rating} => Price : {fi.Price}")

    def SearchRestaurant(self):
        resname = input("Enter the Restaurant name: ")
        res = self.__FoodManager.FindRestaurent(resname)
        if res is not None:
            print("Restaurant Found...")
            print(f"Name : {res.Name}, Rating : {res.Rating}")
            print(self.ShowFoodMenu(res.FoodMenus))
        else:
            print(f"No Restaurant Found on the name {resname}")

    def SearchFoodItems(self):
        foodname = input("Enter the Food name: ")
        res = self.__FoodManager.FindFoodName(foodname)
        if res is not None:
            print("Food Found...")
            print(f"Name : {res.Name}, Rating : {res.Rating}")
            print(self.ShowFoodMenu(res.FoodMenus))
        else:
            print(f"No Food Found on the name {foodname}")

    def ShowFoodMenu(self,menus):
        print("List of Menus Available : ")
        for i,menu in enumerate (menus,1):
            menu.DisplayItem(i)
        choice = int(input("Enter the Choice: "))
        fooditems = menus[choice-1].FoodItems
        self.ShowFoodItems(fooditems)


    def __init__(self):
        self.__FoodManager = FoodManager()

    def Start(self):
        while True:
            for option in MainMenu.__Options:
                print(f"{option}.{MainMenu.__Options[option]}")

            try:
                choice = int(input("Please Enter Your Choice : "))
                print(MainMenu.__Options[choice])
                value =MainMenu.__Options[choice].replace(" ","")
                getattr(self, value)()
            except (ValueError, KeyError):
                print("Invalid input.. Please Enter the Valid Choice")
