from datetime import datetime
import sys


Kalendar = [31,28,31,30,31,30,31,31,30,31,30,31]
Jahr =datetime.today().strftime('%Y')
Monat =datetime.today().strftime('%m')
Tag = datetime.today().strftime('%d')
Stunde = datetime.today().strftime('%H')
Minute = datetime.today().strftime('%M')
Sekunde = datetime.today().strftime('%S')

Jahr = int(Jahr)
Monat = int(Monat)
Tag = int(Tag)
Stunde = int(Stunde)
Minute = int(Minute)
Sekunde = int(Sekunde)


dated = input('Tag deiner Geburt(bitte als Zahl)')

datem = input('Monat deiner Geburt(bitte als Zahl):')

datey = input('Jahr deiner Geburt(bitte als Zahl):')

sex = input('Geschlecht angeben m für männlich w für weiblich:').strip().lower()

if not (dated.isdigit() and datem.isdigit() and datey.isdigit()):
    print("Fehler: Alle Eingaben müssen Zahlen sein!")
    sys.exit(1)

dated = int(dated)
datem = int(datem) 
datey = int(datey)

if not (1 <= datem <= 12):
    print("Fehler: Der Monat muss zwischen 1 und 12 liegen!")
    sys.exit(1)

def schalt(j):
    return (j % 4 == 0 and j % 100 != 0) or j % 400 == 0

if schalt(datey) and datem == 1:
    if not (1 <= dated <= 29):
        print("Fehler: Der Tag muss im Monat liegen")
        sys.exit(1)
elif not (1 <= dated <= Kalendar[datem - 1]):
    print("Fehler: Der Tag muss im Monat liegen")
    sys.exit(1)

if not (sex in ["m","w"]):
    print("Fehler: Bitte m für männlich oder w für weiblich")
    sys.exit(1)

    
def month_day(m,j):
    day = 0

    if schalt(j):
        Kalendar[1] = 29
    else:
        Kalendar [1] = 28
    for i in range(m-1):
        day = Kalendar[i] + day
    return day  
        

def year_day(j):
    day = 0
    for i in range(1,j):
        if schalt(i):
            day = day + 366
        else:
            day = day + 365
    return day 


def add(d,m,j):
    gesamt = d + month_day(m,j) + year_day(j)
    return gesamt        
    

def umwandeln(d,m,j,hd,hm,hj):
    years = hj - j
    months = hm - m
    days = hd - d

    if days < 0:
        months -= 1
        days = Kalendar[m - 1]+days

    if months < 0:
        years -= 1
        months = 12 + months

    return days, months, years


output = 'Du lebst seit {} Tagen, {} Monaten und {} Jahren'.format(*umwandeln(dated,datem,datey,Tag,Monat,Jahr))



gesamtd = add(Tag,Monat,Jahr) - add(dated,datem,datey)


def day_calc (numd,numm,numj):
    day = 0
    for i in range(numm):
        day = Kalendar[i] + day
    day = day + numd + numj * 365
    return day

def hour_calc (d):
    hour = d*24
    return hour

gesamth = hour_calc(gesamtd)

def min_calc (h):
    min = h * 60
    return min

def dec(d):
    dec = d / 365.25
    return dec

def decto_day(dec):
    day = dec * 365.25
    return day

def dectodate(dec, d, m, j):
    v = int(dec)
    h = dec - v
    j = j + v  
    h = int(decto_day(h))  

    if h > (Kalendar[m - 1] - d):
        h = h - (Kalendar[m - 1] - d)
        m = m + 1

    while h > Kalendar[m - 2]:
        if m > 11:
            j = j + 1
            m = 0
        h = h - Kalendar[m]
        m = m + 1

    if d + h > Kalendar[m - 1]:
        h = (d + h) - Kalendar[m - 1]
        d = 0
        m += 1
        if m > 11:
            j += 1
            m = 0
    d += h  

    return d, m, j


def proc(g,a):
    gg = g + a
    gg = g / gg
    return round(gg *100,2)
            




if sex == 'm':
    output_tolive = dectodate(78.2,dated,datem,datey)
    daysalive = add(*output_tolive)- add(Tag,Monat,Jahr)
elif sex == 'w':
    output_tolive = dectodate(83,dated,datem,datey)
    daysalive = add(*output_tolive)- add(Tag,Monat,Jahr)


output = 'Du lebst seit {} Tagen, {} Monaten und {} Jahren'.format(*umwandeln(dated,datem,datey,Tag,Monat,Jahr))


Rente = dectodate(67,dated,datem,datey)


print(output)
print('Oder',gesamtd, 'Tage')
print('Oder' ,hour_calc(gesamtd),'Stunden' )
print('Oder',min_calc(gesamth), 'Minuten')

print('Du wirst ungefähr noch bis zum {}.{}.{} leben'.format(*output_tolive))
print('Das sind noch',daysalive,'Tage')
print('Du hast bereits',proc(gesamtd,daysalive),'% deines Lebens gelebt')
print('Du kriegst Rente am',dectodate(67,dated,datem,datey))
print('Das sind',add(*Rente)-add(dated,datem,datey), 'Tage')

