from tutorial import run_tutorial

run_tutorial()
print("Vége a tutorialnak!")
# Tutorial

print()

print("Válassz hőst!")
print("(1) Kígyó Harcos: HP: 45, Alap fegyver: Kígyó Kard (3-at sebez, 3 sebzésenként betölt a kígyó, ami 10-et sebez.)")
print("(2) Bamba Marha Lovag: HP: 70, Alap fegyver: Vaskard (2-at sebez, nincs semmilyen képesség.)")
print("(3) Varázsló Henrik: HP: 50, Alap fegyver: Varázsbot (1-at sebez, 4 sebzésenként betölt a tornádó, ami 25-öt sebez.)")
print("(4) Csiganő: HP: 40, Alap fegyver: Csiga Kard (4-at sebez, 2 sebzésenként betölt a Csiga Halál, ami 15-öt sebez.)")
# Hősök

vhsz_hos_szam = int(input("Írd be a választott hősödnek a számát."))
if vhsz_hos_szam == 1:
    hos = "Kígyó Harcos"
elif vhsz_hos_szam == 2:
    hos = "Bamba Marha Lovag"
elif vhsz_hos_szam == 3:
    hos = "Varázsló Henrik"
elif vhsz_hos_szam == 4:
    hos = "Csiganő"

print()