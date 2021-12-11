#big018_temaoppg2

#Oppgave 1
import math

radius = int(input('Radius: '))
areal = math.pi*radius**2
print('Arealet til en sirkel med radius', radius, 'er: %.3f' % areal)

print('>>>')

#Oppgave 2

setning = str(input('Skriv setning: '))
antall = int(len(setning))
gjett = int(input("Gjett lengden på setningen: "))
print("That's", antall==gjett, '!!')

print('>>>')

#Oppgave 3
import random

tall = int(input('Skriv inn et tall: '))
t = random.randint(0,50)
print(tall,'/', t, '= %.1f' % (tall/t))





