password="23"

import string

def passwordStrengthChecker(password:str)->int:
    if len(password) >= 8 and len(password) < 18:
        # lowercase, uppercase, symbols, numbers
        point = [0,0,0,0]
        for i in password:
            if i in string.ascii_lowercase:
                point[0]=1
            if i in string.ascii_uppercase:
                point[1]=1
            if i in string.punctuation:
                point[2]=1
            if i in string.digits:
                point[3]=1
    return sum(point)

def resultPrinter(points:int):
    if points == 4:
        print("STRONG PASSWORD !!!")
    elif points >= 2 and points <=3:
        print("Password is OK!!!")
    else:
        print("TRY Another STRONG Password [Weak password...]")

resultPrinter(passwordStrengthChecker(input("Enter the Password...[validate the Strength at $0\n>>>")))