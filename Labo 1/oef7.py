# Oefening 7: samengestelde rente
rente = 1.012
bedrag = float(input("Bedrag: "))

for i in range(1, 4):
    bedrag *= rente
    print(f"Over {i} jaar is uw bedrag: {round(bedrag, 2)}€")
