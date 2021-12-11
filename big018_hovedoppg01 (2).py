#big018_hovedoppg01

#Oppgave 1.)
#math.pi kun oppgir 15 desimaler, derav maks 15.

import math

def pi(d):
    if d <= 15:
        return("%.{}f".format(d, d) % math.pi)
    else:
        return('For mange desimaler.', "%.2f" % (math.pi))
    

#Oppgave 2
#Bruker skriver inn 'temperaturKonvertering(grader, 'C'/'F')'.
def temperaturKonvertering(grader, enhet=None):
    if enhet == 'C':
        return(grader * (9/5)) + 32
    elif enhet == 'F':
        return(grader - 32.0) * (5/9)
    else:
        return(grader * (9/5)) + 32

         
#Oppgave 3a.) #Eneste måten jeg kom fram til å løse denne oppgaven, jeg vet vi ikke har gått gjennom __init__(self), men programmet fungerer og kjører slikt som det skal i henhold til oppgaven.
class konto():

    def __init__(self, saldo=0): #Constructor
        self.saldo = saldo

    def innskudd(self, innmengde): #Bruker skriver inn 'saldo.innskudd()', og sum inne i parantesene.
        self.saldo += innmengde
        print('{} kr er lagt til i saldoen.'.format(innmengde))

    def uttak(self, utmengde): #Bruker skriver inn 'saldo.uttak()', og sum inne i parantesene.
        if self.saldo >= utmengde:
            self.saldo -= utmengde
            print('Uttak på {}.'.format(utmengde),'kr.')
        else:
            print('Ingen dekning.')

    def beregn_rente(self): #Bruker skriver 'saldo.beregn_rente()'.
        if self.saldo < 1000000:
            rente = self.saldo * 0.01
            print(rente, 'kr.')  
        else:
            bonus = self.saldo * 0.02
            print(bonus, 'kr.')

    def beregn_oppgjor(self): #Bruker skriver 'saldo.beregn_oppgjor()'.
        if self.saldo < 1000000:
            vanligrente = self.saldo * 0.01
            print('Saldo med ordinær rente: ',(self.saldo + vanligrente), 'kr')
            self.saldo = self.saldo + vanligrente
        else:
            bonusrente = self.saldo * 0.02
            print('Saldo med bonusrente:',(self.saldo + bonusrente), 'kr')
            self.saldo = self.saldo + bonusrente
    
    def __str__(self): #Forenkeling slik at bruker kan skrive: saldo.innskudd/saldo.uttak osv.
        return f'Saldo: {self.saldo}'

saldo = konto(500) #Bruker skriver 'print(saldo)' for å få oppgitt saldo.


#Oppgave 3b.)
#Bruker start prosessen ved å skrive 'velg()'.
class konto():

    def __init__(self, saldo=0): 
        self.saldo = saldo

    def innskudd(self): 
        self.saldo += float(input('Innskuddssum: '))
        print('Saldoen er nå {} kr.'.format(self.saldo))

    def uttak(self):
        utmengde = float(input('Uttakssum: '))
        
        if self.saldo >= utmengde:
            self.saldo -= utmengde
            print('Uttak på {}.'.format(utmengde))
        else:
            print('Ingen dekning.')

    def beregn_rente(self):
        if self.saldo < 1000000:
            rente = self.saldo * 0.01
            print(rente, 'kr.')  
        else:
            bonus = self.saldo * 0.02
            print(bonus, 'kr.')

    def beregn_oppgjor(self): 
        if self.saldo < 1000000:
            vanligrente = self.saldo * 0.01
            print('Saldo med ordinær rente: ',(self.saldo + vanligrente), 'kr')
            self.saldo = self.saldo + vanligrente
        else:
            bonusrente = self.saldo * 0.02
            print('Saldo med bonusrente:',(self.saldo + bonusrente), 'kr')
            self.saldo = self.saldo + bonusrente
    
    def __str__(self): 
        return f'Saldo: {self.saldo}'

saldo = konto(500)

def velg():  
    while True:
        velg = int(input('1 for saldo\n2 for innskudd\n3 for uttak\n4 for renteberegning\n5 for renteoppgjør\nVelg handling: '))
        if velg == 1:
            print(saldo)
        if velg == 2:
            saldo.innskudd()
        if velg == 3:
            saldo.uttak()
        if velg == 4:
            saldo.beregn_rente()
        if velg == 5:
            saldo.beregn_oppgjor()

            
#Oppgave 3c.)
#Stoff får å kunne løse 3c er for lite gjennomgått for å kunne løse syntes jeg, jeg er ikke den eneste som syntes det heller.
#Har heller ikke vært borti en slik oppgave i lab eller lignende før, så det kommer som et sjokk.
#Har veldig lite å kunne bidra med her for at du som retter skal kunne gi en tilbakemelding til dette i det hele tatt.
            
#Har en viss ide om at man må bruke .append og lister. 

        if velg == 6: #Legge til dette på listen av velg()
            siste_endringer #funksjonen kommer til å hele siste_endringer. Må man bruke def(?)
            
historie [self.saldo, saldo.innskudd(), saldo.uttak(), saldo.beregn_rente(), saldo.beregn_oppgjor()]

#En liste av funksjonene av noe slag, og bruke append for å resultatene til slutt? Kanskje *parametere?
#Håper på gode tilbakemeldinger slik at jeg kan løse denne oppgaven til slutt, for det er veldig vanskelig å løse denne iht. det vi har lært.


#Oppgave 4.)
import random

def tre_tilfeldige(): #Bruker skriver inn 'tre_tilfeldige()'
    nummer1 = random.randint(1, 9)
    nummer2 = random.randint(1, 9)
    nummer3 = random.randint(1, 9)
    
    minst = min(nummer1, nummer2, nummer3)
    stoerst = max(nummer1, nummer2, nummer3)
    midten = (nummer1 + nummer2 + nummer3 - minst - stoerst)
    return (minst, midten, stoerst)


