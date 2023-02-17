from datetime import datetime, date

Y = datetime.now().year
seizoenen = {
    'lente': [
        {'start': date(Y,  3,  20)},
        {'einde': date(Y,  6,  20)}
    ],
    'zomer': [
        {'start': date(Y,  6,  21)},
        {'einde': date(Y,  9,  21)}
    ],
    'herfts': [
        {'start': date(Y,  9,  22)},
        {'einde': date(Y,  12,  20)}
    ],
    'winter': [
        {'start': date(Y,  12,  21)},
        {'einde': date(Y,  3,  19)}
    ],
}

maand = input("Geef de maand in: ")
dag = int(input("Geef de dag van de maand in: "))
datum = date(Y, datetime.strptime(maand, '%B').month, dag)
print(seizoenen['lente']['start'])
# if datum > seizoenen['lente'] and datum < seizoenen['lente']:
#     print(f"{datum} is in de {seizoenen[0].key}")
