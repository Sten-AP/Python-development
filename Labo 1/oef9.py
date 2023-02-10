# Oefening 9: eenheden van tijd
dagen = int(input("Dagen: "))
uren = int(input("Uren: "))
minuten = int(input("Minuten: "))
seconden = int(input("Seconden: "))

seconden += minuten * 60 + uren * 3600 + dagen * 86400

print(f"Aantal seconden: {seconden}")