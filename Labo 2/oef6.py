from datetime import datetime, date

Y = datetime.now().year  # dummy leap year to allow input X-02-29 (leap day)
seizoenen = [('winter', (date(Y,  1,  1),  date(Y,  3, 20))),]

maand = input("Geef de maand in: ")
dag = int(input("Geef de dag van de maand in: "))

