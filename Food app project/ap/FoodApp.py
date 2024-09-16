from Controllers.FoodManager import FoodManager
from Model.User import User
from Model.UserManager import UserManger
from Controllers.MainMenu import MainMenu
class LoginSystem:
    def Login(self):
        email = input("EmailID : ")
        password  = input("Enter the Password : ")

        user =UserManger.FindUsers(email,password)

        if user is not None:
            print("Login Successfully...")
            menu =MainMenu()
            menu.Start()

        else:
            print("Invalid User...")

    def Register(self):
        name = input("Name : ")
        mobile = int(input("Mobile No : "))
        email = input("EmailID : ")
        password  = input("Enter the Password : ")

        user = User(names= name, phn=mobile, email=email, passwd=password )
        UserManger.AddUser(user)

    def Exit(self):
        print("Thankyou for using our Food App..🤝")
        exit()

    def ValidateOption(self, option):
        getattr(self,option)()


class FoodApp:

    LoginOptions = {1 : "Login", 2 : "Register", 3 : "Exit"}
    @staticmethod
    def Init(): #initial method
        print("<< Welcome to Online Food Ordering >>")

        loginsystem = LoginSystem()
        menu = MainMenu()
        #menu.Start()
        while True:
            for option in FoodApp.LoginOptions:
                print(f"{option}.{FoodApp.LoginOptions[option]}")

            try:
                choice = int(input("Please Enter Your Choice : "))
                print(FoodApp.LoginOptions[choice])
                loginsystem.ValidateOption(FoodApp.LoginOptions[choice])
            except (ValueError,KeyError):
                print("Invalid input.. Please Enter the Valid Choice")
