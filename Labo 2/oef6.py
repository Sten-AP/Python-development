from datetime import datetime, date
import locale

locale.setlocale(locale.LC_ALL, 'nl_NL')

Y = datetime.now().year
seizoenen = {
    'lente': {
        'start': date(Y,  3,  20),
        'einde': date(Y,  6,  20)
    },
    'zomer': {
        'start': date(Y,  6,  21),
        'einde': date(Y,  9,  21)
    },
    'herfts': {
        'start': date(Y,  9,  22),
        'einde': date(Y,  12,  20)
    },
    'winter': {
        'start': date(Y,  12,  21),
        'einde': date(Y+1,  3,  19)
    }

}

maand = input("Geef de maand in: ")
dag = int(input("Geef de dag van de maand in: "))
datum = date(Y, datetime.strptime(maand, '%B').month, dag)

if datum > seizoenen['lente']['start'] and datum < seizoenen['lente']['einde']:
    print(f"{datum} is in de {list(seizoenen.keys())[0]}")
elif datum > seizoenen['zomer']['start'] and datum < seizoenen['zomer']['einde']:
    print(f"{datum} is in de {list(seizoenen.keys())[1]}")
elif datum > seizoenen['herfts']['start'] and datum < seizoenen['herfts']['einde']:
    print(f"{datum} is in de {list(seizoenen.keys())[2]}")
elif datum > seizoenen['winter']['start'] and datum < seizoenen['winter']['einde']:
    print(f"{datum} is in de {list(seizoenen.keys())[3]}")
