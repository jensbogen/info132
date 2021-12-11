
#big018_temaoppgave3

#Skjønner ikke hvorfor den printer ut 'y' forresten :/

#Oppgave 1a
x=9
y=66
print(x!=7 and y<=50)
print(x>7 or 50<y) and (x>y or y>100)

#Uttrykkene evalueres til resultatene:
#'False'
#'True'

print('>>>')

#Oppgave 1b
x=9
y=66

#Alternativ måte for (x!=7 and y<=50) er:
(not x!=7) and (not y<=50)

#Alternativ måte for (x>7 or 50<y) and (x>y or y<100) er:
(x>7 or 50<y) or not(x>y or y<100)

#Usikker på denne oppgaven, gjerne si en alternativ fremgangsmåte.



#Oppgave 2

alder = int(input('Oppgi alder: '))
tulleby = int(input('Hvor lenge har du bodd i Tulleby?: '))

print('Du er kvalifisert for:')

if alder >= 25 and tulleby >= 5:
    print('Bystyret.')

if alder < 25 and tulleby >= 5:
    print('Du har bodd her lenge nok. Men du må fylle', 25-alder, 'år til for å bli med i bystyret.')

if alder >= 25 and tulleby < 5:
    print('Du er gammel nok. Bo her i', 5-tulleby, 'år til, så kan du bli med i bystyret.')

if alder >= 30 and tulleby >= 9:
    print('Ordfører.')

if alder >= 30 and tulleby <= 9:
    print('Du er gammel nok. Men må bo her i', 9-tulleby, 'år til så kan du bli ordfører.')
  
    
if alder <= 30 and tulleby > 9:    
    print('Du er ikke gammel nok til å bli ordfører. Bo her i', 30-alder, 'år til, så du kan bli ordfører.')

print('>>>')

#Oppgave 3

#Slik jeg tolket oppgaven skulle jeg gjøre programmet om til 'chained conditionals', og unngå 'branches' som programmet oprinnelig bestod av.
#Hvis man kan unngå nøstede if-setninger burde man det, slik at det ser ryddigere ut.
#Programmet ble slikt:

x = int(input('Tall: '))

if x <= 5:
    print('Maks 5')

elif x <= 10:
    print('6, 7, 8, eller 9.')

else:
    print('Minst 10.')

print('>>>')
