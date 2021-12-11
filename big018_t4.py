#big018_t4

#Oppgave 1.)
#Bruker skriver inn f.eks: 'siste("Python")' eller 'siste(range(1,10))'
def siste(sekvens):
    siste = sekvens[-1]
    print(siste)
   

#Oppgave 2.)
#Bruker skriver inn f.eks: 'skriv_sekvens(range(90,100))'.

def skriv_sekvens(sekvens):
    for x in sekvens:
        print(x, sep="", end=" ")
    print("\n")

#Oppgave 3.)
startbelop = int(input('Startbeløp: '))
rentesats = int(input('Rentesats (%): '))
onsketbelop = int(input('Ønsket beløp: '))
år = 0

while startbelop < onsketbelop:
    startbelop += (rentesats/100)*startbelop
    år += 1

    print('år', år, ':', '%.2f' % startbelop)

#Oppgave 4.)
#Bruker skriver inn 'gangetabell(9).'

def gangetabell(side):
    print('    1   2       3        4       5       6       7       8        9')
    print('--|-----------------------------------------------------------------------')
    rad = 0
    for i in range(1, side+1):
        rad += 1
        print(rad, end=' | ')
        for j in range(1, side+1):
            print((i*j), end='\t')
        print()
