leeftijd = 0
while leeftijd <= 0:
    leeftijd = int(input("Geef de leeftijd in: "))
    if leeftijd <= 0:
        print("Geen geldig getal.")


def telHondenJaren():
    if leeftijd <= 2:
        return leeftijd * 10.5
    return 2 * 10.5 + (leeftijd-2) * 4


print(f"Aantal hondenjaren: {telHondenJaren()}")
