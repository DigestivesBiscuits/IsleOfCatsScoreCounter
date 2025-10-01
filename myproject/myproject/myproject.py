def main():

    print(f"{BlueCats()} points!")
    print(f"{GreenCats()} points!")
    print(f"{OrangeCats()} points!")
    print(f"{PurpleCats()} points!")
    print(f"{RedCats()} points!")
    print(f"{RareTreasure()} points!")
    print(f"{Rats()} points!")
     
    print(f"{Rooms()} points!")
    

def BlueCats():
    BlueCats = int((input("How many blue cats do you have on your boat? ")))

    totalBlueCats = 0

    if BlueCats == 3:
        totalBlueCats = 8
    elif BlueCats == 4:
        totalBlueCats = 11
    elif BlueCats >= 5 and BlueCats <= 10:
        contador = BlueCats - 5
        totalBlueCats = 10
        while contador >= 0:
            totalBlueCats += 5
            contador -= 1
    elif BlueCats > 10:
        totalBlueCats = 40
    else:
        totalBlueCats = 0

    return totalBlueCats
def GreenCats():
    GreenCats = int((input("How many green cats do you have on your boat? ")))

    totalGreenCats = 0

    if GreenCats == 3:
        totalGreenCats = 8
    elif GreenCats == 4:
        totalGreenCats = 11
    elif GreenCats >= 5 and GreenCats <= 10:
        contador = GreenCats - 5
        totalGreenCats = 10
        while contador >= 0:
            totalGreenCats += 5
            contador -= 1
    elif GreenCats > 10:
        totalGreenCats = 40
    else:
        totalGreenCats = 0

    return totalGreenCats
def OrangeCats():
    OrangeCats = int((input("How many orange cats do you have on your boat? ")))

    totalOrangeCats = 0

    if OrangeCats == 3:
        totalOrangeCats = 8
    elif OrangeCats == 4:
        totalOrangeCats = 11
    elif OrangeCats >= 5 and OrangeCats <= 10:
        contador = OrangeCats - 5
        totalOrangeCats = 10
        while contador >= 0:
            totalOrangeCats += 5
            contador -= 1
    elif OrangeCats > 10:
        totalOrangeCats = 40
    else:
        totalOrangeCats = 0

    return totalOrangeCats
def PurpleCats():
    PurpleCats = int((input("How many purple cats do you have on your boat? ")))

    totalPurpleCats = 0

    if PurpleCats == 3:
        totalPurpleCats = 8
    elif PurpleCats == 4:
        totalPurpleCats = 11
    elif PurpleCats >= 5 and PurpleCats <= 10:
        contador = PurpleCats - 5
        totalPurpleCats = 10
        while contador >= 0:
            totalPurpleCats += 5
            contador -= 1
    elif PurpleCats > 10:
        totalPurpleCats = 40
    else:
        totalPurpleCats = 0

    return totalPurpleCats
def RedCats():
    RedCats = int((input("How many red cats do you have on your boat? ")))

    totalRedCats = 0

    if RedCats == 3:
        totalRedCats = 8
    elif RedCats == 4:
        totalRedCats = 11
    elif RedCats >= 5 and RedCats <= 10:
        contador = RedCats - 5
        totalRedCats = 10
        while contador >= 0:
            totalRedCats += 5
            contador -= 1
    elif RedCats > 10:
        totalRedCats = 40
    else:
        totalRedCats = 0

    return totalRedCats
def RareTreasure():
    RareTreasure = int(input("How many rare treasures do you have on your boat? "))
    totalRareTreasure = RareTreasure * 3 
    return totalRareTreasure
def Lessons():

def Rats():
        Rats = int(input("How many rats do you have on your boat? "))
        totalRats = Rats * -5
        
        return totalRats
def Rooms():
    Rooms = int(input("How many rooms were not completely filled? "))
    totalRooms = Rooms * -5

    return totalRooms


main()
