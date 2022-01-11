while True:
    try:
        #Input section
        BestFriends = int(input("How Many Best Friends?:   "))
        UltraFriends = int(input("How Many Ultra Friends?: "))
        GreatFriends = int(input("How Many Great Friends?: "))
        GoodFriends = int(input("How Many Good Friends?:   "))

        EggActive = str(input("Do You/Will You Have A Lucky Egg Active? (Y/N): ")).upper()

        # Math Section
        BestFriendExp = 100000
        UltraFriendExp = 50000
        GreatFriendXp = 10000
        GoodFriendXp = 3000

        TotalExp = (BestFriends * BestFriendExp) + (UltraFriends * UltraFriendExp) + (GreatFriends * GreatFriendXp) + (GoodFriends * GoodFriendXp)

        if (EggActive == "Y"):
            TotalExp = TotalExp * 2

        print("\n\n")
        print("Total Exp Gained {0}".format(TotalExp))
        print("\n\n")
        break

    except ValueError:
        print("You provided a invaild input - Please try again")
        print("\n\n")
