from Model.User import User

class UserManger:
    __User = []

    @classmethod
    def AddUser(cls, userobj):
        if isinstance(userobj,User):
            cls.__User.append(userobj)
            print("You have been Successfully Registered")
        else:
            print("Invalid User")

    @classmethod
    def FindUsers(cls, email, passwd):
        for user in cls.__User:
             if user.Email == email and user.Password == passwd:
                return user