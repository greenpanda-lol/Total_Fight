import random
from game import hos

def adatok():
    if hos == "Kígyó Harcos":
        hp = 45
        fegyver = "(kk) Kígyó Kard"
        fegyver_sebzes = 3
        kepesseg = "(k) Kígyó"
        kepesseg_betoltes = 3
        kepesseg_sebzes = 10
    elif hos == "Bamba Marha Lovag":
        hp = 70
        fegyver = "(vk) Vaskard"
        fegyver_sebzes = 2
        kepesseg = ""
        kepesseg_betoltes = 10000000
        kepesseg_sebzes = "0"
    elif hos == "Varázsló Henrik":
        hp = 50
        fegyver = "(vb) Varázsbot"
        fegyver_sebzes = 1
        kepesseg = "(t) Tornádó"
        kepesseg_betoltes = 4
        kepesseg_sebzes = 25
    elif hos == "Csiganő":
        hp = 40
        fegyver = "(csk) Csiga Kard"
        fegyver_sebzes = 4
        kepesseg = "(csh) Csiga Halál"
        kepesseg_betoltes = 2
        kepesseg_sebzes = 15

    fegyverek = []
    maxhp = hp
    fegyverek.append(fegyver)
    kepesseg_betoltodott = 0
    return hos
    return hp
    return maxhp
    return kepesseg_betoltodott
    return kepesseg_betoltes
    return fegyver
    return fegyverek
    return fegyver_sebzes
    return kepesseg_sebzes

def harc_jatekos_statisztikak():
    adatok()
    hos = adatok()[0]
    hp = adatok()[1]
    maxhp = adatok()[2]
    kepesseg_betoltodott = adatok()[3]
    kepesseg_betoltes = adatok()[4]
    fegyverek = adatok[5]
    print(f"TE, AZAZ {hos}")
    print(f"HP: {hp}/{maxhp}")
    print(f"A képesség betöltődése: {kepesseg_betoltodott}/{kepesseg_betoltes}")
    print(f"Dolgaid: {fegyverek}")
    print()

def tamadas():
    adatok
    kepesseg_betoltodott = adatok()[3]
    kepesseg_betoltes = adatok()[4]
    fegyverek = adatok()[6]
    fegyver_sebzes = adatok()[7]
    kepesseg_sebzes = adatok()[8]
    print(f"Mivel támadsz? {fegyverek} (Zárójelbe leírtuk, hogy melyik billentyűt kell lenyomni, a támadáshoz)")
    tamado_billentyu = input("")
    if tamado_billentyu == "kk" and hos == "Kígyó Harcos":
        minuszhp = fegyver_sebzes
    elif tamado_billentyu == "vk" and hos == "Bamba Marha Lovag":
        minuszhp = fegyver_sebzes
    elif tamado_billentyu == "vb" and hos == "Varázsló Henrik":
        minuszhp = fegyver_sebzes
    elif tamado_billentyu == "csk" and hos == "Csiganő":
        minuszhp = fegyver_sebzes
    elif tamado_billentyu == "k" and hos == "Kígyó Harcos" and kepesseg_betoltodott == kepesseg_betoltes:
        minuszhp = kepesseg_sebzes
    elif tamado_billentyu == "vb" and hos == "Varázsló Henrik" and kepesseg_betoltodott == kepesseg_betoltes:
        minuszhp = kepesseg_sebzes
    elif tamado_billentyu == "csh" and hos == "Csiganő" and kepesseg_betoltodott == kepesseg_betoltes:
        minuszhp = kepesseg_sebzes
    return minuszhp

def level_1():
    hp = adatok()[1]
    maxhp = adatok[2]
    kepesseg_betoltes = adatok()[4]
    hp = maxhp
    kepesseg_betoltodott = 0
    hp_nyalkaszorny = 25
    maxhp_nyalkaszorny = hp_nyalkaszorny

    def stat_nyalkaszorny():
        print("Ő, AZAZ A NYÁLKASZÖRNY")
        print(f"HP: {hp_nyalkaszorny}/{maxhp_nyalkaszorny}")
        print("Fegyverek: [Nyálkagolyó bomba (-5 HP), Ütés (-2 HP)]")
        print()

    print("Elindulsz a Total Fight ösvényén. Szembetalálkozol egy nagy nyálkaszörnyel.")
    print("HARC!")
    print()
    harc_jatekos_statisztikak()
    stat_nyalkaszorny()
    soron_vagy = True
    while hp > 0 or hp_nyalkaszorny > 0 and soron_vagy == True:
        tamadas()
        minuszhp = tamadas()
        print(f"{minuszhp} HP-t sebeztél a nyálkaszörnybe.")
        print()

        nyalkaszorny_tamadas_kivalasztas = random.randint(1, 100)
        if nyalkaszorny_tamadas_kivalasztas <= 60:
            hp -= 2
            print("A Nyálkaszörny -2 HP-t sebzett beléd ezzel: Ütés")
        else: 
            hp -= 5
            print("A Nyálkaszörny -5 HP-t sebzett beléd ezzel: Nyálkagolyó bomba")

        harc_jatekos_statisztikak()
        stat_nyalkaszorny()
    if hp <= 0:
        if input("Meghaltál! A nyálkaszörny legyőzött. Lépj vissza a menübe, az m gomb megnyomásával.") == "m":
            from game import jatek_menu
            jatek_menu()
        else:
            print("ERROR")
    elif hp_nyalkaszorny <= 0:
        print("Sikeresen legyőzted a Nyálkaszörnyet!")
        xp += 1200
        print(f"+1200 XP (JELENLEG NEM MENTŐDIK LE!)")
        if input("Lépj vissza a menübe, az m gomb megnyomásával.") == "m":
            jatek_menu()
        else: 
            print("ERROR")