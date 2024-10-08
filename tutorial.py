def run_tutorial():
    print("Üdvözöllek a Total Fight-ban!")
    print("A játék lényege, hogy harcolj szörnyekkel és egyéb dolgokkal.")
    if input("Ha készen állsz, gépeld be a w betűt.") == "w":
        hp_madarijeszto = 15
        hp_user = 30
        print("")
        print("ELLENFÉL: Madárijesztő")
        print(f"HP: {hp_madarijeszto}")
        print("Képessége: Ütés")
        print("")
        print(f"A te HP-d: {hp_user}")
        print("Képességeid: Ütés (ü)")
        while input("VÁLASZD KI A TÁMADÁSODAT!") == "ü":
            hp_madarijeszto -= 4
            print(f"Madárijesztő HP: {hp_madarijeszto}")
            print(f"A te HP-d: {hp_user}")
            print("")
            print("A Madárijesztő támad: 2 HP-t sebzett beléd.")
            hp_user -= 2
            print(f"Madárijesztő HP: {hp_madarijeszto}")
            print(f"A te HP-d: {hp_user}")
            if hp_madarijeszto <= 0:
                break
                print("Vége a Tutorialnak!")
        else:
            print("ERROR")


run_tutorial()