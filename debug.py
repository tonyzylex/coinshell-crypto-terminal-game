import User_module
import q_command
import json
import os


def SetUser():
    if os.path.exists("UserData.json"):
        AutoUser = User_module.User("mahawan","porkchop")
        with open("UserData.json", "r") as f:
                    try:
                        data = json.load(f)
                    except json.JSONDecodeError:
                        data = []  
                    for _, user in enumerate(data):
                        if user["username"] == AutoUser.name and user["password"] == AutoUser.GetPassword():
                            AutoUser = User_module.User(AutoUser.name,AutoUser.GetPassword())
                            AutoUser.LoadData(user)
                            print(AutoUser.to_dict())
                            Run = False
                            return AutoUser
                    if AutoUser == None:
                        print("Incorrect name or password!")
    else:
         print("It does not exist!")

def DebugMethods():
     PreUse = SetUser()
     q_command.main(PreUse)


DebugMethods()


 