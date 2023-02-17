aantalZijden = 0
while aantalZijden < 3 or aantalZijden > 10:
    aantalZijden = int(input("Geef het aantal zijden in: "))
    if aantalZijden < 3 or aantalZijden > 10:
        print("Geen geldig getal.")

vormen = ["driehoek", "vierhoek", "vijfhoek",
          "zeshoek", "zevenhoek", "achthoek", "negenhoek", "tienhoek"]

print(vormen[aantalZijden-3])
