
import json
import os
import uuid



class User():

    def __init__(self,name,password):

        if len(name) < 3:
            print("Name must contain more than 3 characters!")
            return
        if len(password) < 6:
            print("Password must contain more than 6 characters!")
        self.name = name
        self.Balance = 1500 # Starting balance
        self.__password = password 
        self.__UniqueId = str(uuid.uuid4())
        self.OwnedCryptoCoins = {
          
        }

    def __str__(self):
        return f"Name{self.name} || OwnedCoins:{self.OwnedCryptoCoins}"
    
    
    
    def to_dict(self):
        return {
            "UniqueId" : self.__UniqueId,
            "username": self.name,
            "password": self.__password,
            "Balance" : self.Balance,
            "OwnedCoins" : self.OwnedCryptoCoins
        }
    
    def SaveThis(self):
        user_data = self.to_dict()

        
        if not os.path.exists("UserData.json"):
            with open("UserData.json", "w") as f:
                json.dump([user_data], f, indent=4)
            print("User saved successfully.")
            return

       
        with open("UserData.json", "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []  

        
        for i, user in enumerate(data):
            if user["UniqueId"] == self.__UniqueId:
                data[i] = user_data  
                print("User updated.")
                break
        else:
            data.append(user_data)
            print("New user added.")

        
        with open("UserData.json", "w") as f:
            json.dump(data, f, indent=4)

    def GetUniId(self):
        return self.__UniqueId

    def LoadData(self,data_dict):
        self.__UniqueId = data_dict["UniqueId"]
        self.name = data_dict["username"]
        self.__password = data_dict["password"]
        self.Balance = data_dict["Balance"]
        self.OwnedCryptoCoins = data_dict["OwnedCoins"]
        print("User data loaded.")

def UserLoginDashboard():
    Run = True
    while Run:
        print("Welcome to the login/sign-up panel!")
        print("1.Log-in\n2.Register\n3.Exit")
        Choice = input("Choose an option:").strip().lower()
        match Choice:
            case "1" | "log-in" | "l":
                name = input("InputName:")
                password = input("InputPassword:")
                LoadUser = None
                with open("UserData.json", "r") as f:
                    try:
                        data = json.load(f)
                    except json.JSONDecodeError:
                        data = []  
                    for _, user in enumerate(data):
                        if user["username"] == name and user["password"] == password:
                            LoadUser = User(name,password)
                            LoadUser.LoadData(user)
                            print(LoadUser.to_dict())
                            Run = False
                            return LoadUser
                    if LoadUser == None:
                        print("Incorrect name or password!")
                                
            case "2" | "register" | "r":
                name = input("name:")
                password = input("password:")
                NewUser = User(name,password)
                if NewUser:
                    NewUser.SaveThis()
            case "3" | "exit" | "e":
                Run = False
                return "Abolish program"
            case _:
                print("Invalid Argument!")



