# Oefening 5: statiegeld berekenen
statieKlein = 0.12
statieGroot = 0.25

aantalKlein = float(input("Aantal kleine flessen: "))
aantalGroot = float(input("Aantal grote flessen: "))

statieTotaal = round((statieKlein * aantalKlein) +
                     (statieGroot * aantalGroot), 2)

print(f"Totaal statiegeld: {statieTotaal}€")
