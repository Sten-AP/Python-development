aantalZijden = 0
while aantalZijden < 3 or aantalZijden > 10:
    aantalZijden = int(input("Geef het aantal zijden in: "))
    if aantalZijden < 3 or aantalZijden > 10:
        print("Geen geldig getal.")

if aantalZijden == 3:
    print("driehoek")
elif aantalZijden == 4:
    print("vierhoek")
elif aantalZijden == 5:
    print("vijfhoek")
elif aantalZijden == 6:
    print("zeshoek")
elif aantalZijden == 7:
    print("zevenhoek")
elif aantalZijden == 8:
    print("achthoek")
elif aantalZijden == 9:
    print("negenhoek")
elif aantalZijden == 10:
    print("tienhoek")
