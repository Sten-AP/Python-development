letter = input("Geef een letter in: ").lower()

if letter in {"a", "e", "i", "o", "u"}:
    print(f"{letter} is een klinker.")
elif letter == "y":
    print(f"{letter} is een soms een klinker en soms een medeklinker.")
else:
    print(f"{letter} is een medeklinker.")
