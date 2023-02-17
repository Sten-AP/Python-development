maand = input("Geef een maand in: ").lower()

if maand in {"januari", "maart", "mei", "juli", "augustus", "oktober", "december"}:
    print(f"{maand} heeft 31 dagen.")
elif maand == "februari":
    print(f"{maand} heeft 28 of 29 dagen.")
else:
    print(f"{maand} heeft 30 dagen.")
