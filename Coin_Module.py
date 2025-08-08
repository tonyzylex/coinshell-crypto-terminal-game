import random


class Coin():
    def __init__(self, name, baseprice = 11.2):
        self.name = name
        self.baseprice = baseprice
    def Fluctate(self):
        self.fluctationVal = round(random.uniform(-1, 1) * 100,2) # change in percentage
        if self.baseprice == 0:
            self.result = self.fluctationVal / 100
        else:
            delta = random.uniform(-0.5, 0.5)
            self.result = self.baseprice + (self.baseprice * self.fluctationVal / 100) + delta
        self.ChangedPrice = round(self.result, 2)
    
    def GetInfo(self):
        return {
            "name": self.name,
            "CurrentPrice": self.baseprice,
            "FluctationPercentage": f"%{self.fluctationVal}",
            "ChangedPrice": self.ChangedPrice
        }
    


def Debug(): 
    Coin1 = Coin("Bitcoin")
    positive_count = 0
    negative_count = 0
    zero_count = 0
    for i in range(1000):
        Coin1.Fluctate()
        info = Coin1.GetInfo()
        print(info)

        if Coin1.baseprice > 32:
            input("Reached Peak! press enter to continue")
        if Coin1.baseprice < -32:
            input("Reached Bottom! press enter to continue")

        if info["ChangedPrice"] > 0:
            positive_count += 1
        elif info["ChangedPrice"] < 0:
            negative_count += 1
        else:
            zero_count += 1

        Coin1.baseprice = info["ChangedPrice"]

    print("After 1000 fluctuations:")
    print(f"Positive Price Count: {positive_count}")
    print(f"Negative Price Count: {negative_count}")
    print(f"Zero Price Count: {zero_count}")



