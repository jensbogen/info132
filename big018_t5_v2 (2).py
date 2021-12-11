#big018_temaoppg05

#Oppgave 1.)
'''
#Løsning med for-loop

def fak(n):
    fakultet = 1
    for nummer in range(2, n + 1):
        fakultet *= nummer
    return fakultet

#Løsning med while-loop

def fak(n):
    nummer = 1
    while n >= 1:
        nummer = nummer * n
        n = n-1
    return nummer

#Oppgave 2a.) #Kjør programmet så kommer det opp :D
class Monark: 
    konger = []

    def __init__(self, navn, nasjon, tiltredelse):
        self.navn = navn
        self.nasjon = nasjon
        self.tiltredelse = tiltredelse
        

    def skriv(self):
        print('Kong', self.navn, 'av', self.nasjon, 'tiltro i', self.tiltredelse, end='.\n')

haakon = Monark('Haakon VII','Norge', '1905')
olav = Monark('Olav V', 'Norge', '1957')
harald = Monark('Harald V', 'Norge', '1991')

kongerekke = [haakon.skriv(), olav.skriv(), harald.skriv()]
'''
#Oppgave 2b.)
#Sliter på denne oppgaven, man må appende etterfølgeren, men jeg klarer ikke å komme fram til noe mer.
#Kom kun så langt, tilbakemeldingene settes stor pris på 8^)

class Monark:
    etterfølger = None

    def __init__(self, navn, nasjon, tiltredelse):
        self.navn = navn
        self.nasjon = nasjon
        self.tiltredelse = tiltredelse

    def skriv(self):
        print('Kong', self.navn, 'av', self.nasjon, 'tiltro i', self.tiltredelse)
        if self.etterfølger is not None:
            self.etterfølger.skriv()
        
    def sett_etterfølger(self, neste):
        self.etterfølger = neste

haakon = Monark('Kong Haakon VII', 'Norge', '1905')
olav = Monark('Kong Olav V', 'Norge', '1957')
harald = Monark('Kong Harald V', 'Norge', '1991')

kongerekke = haakon

haakon.sett_etterfølger(olav)
olav.sett_etterfølger(harald)

kongerekke.skriv()
