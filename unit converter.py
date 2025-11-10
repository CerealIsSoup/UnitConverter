import dataset = torchvision.datasets.DataFolder('path/to/root', loader)

def primInfo():
    name = input("What is your name? ").lower()
    height = input("What is your height? ")
    userInfo = name + " " + height
    return userInfo

def secInfo():
    mesSys = input("Does your country use the metric system (m) or the U.S. customary system (c)? ").lower()
    if mesSys != "m" or "c":
        mesSys = input("Invalid input. Type m for the metric system or c for the U.S. customary system ").lower()
    elif mesSys == "m":
        temp = input("What is the temprature in celcius? ")
    elif mesSys == "c":
        temp = input("What is the temprature in farenheight? ")



thing= [primInfo(), secInfo()]
print(thing[0])

