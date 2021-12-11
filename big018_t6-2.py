#big018_t06

#Oppgave 1.) 
def antallVokaler(setning): #Bruker skriver inn antallVokaler og en setning inne i ('')
    
    vokal = ['a', 'e', 'i', 'o', 'u', 'y', 'æ', 'ø', 'å']
    antall = 0

    for bokstav in setning:
        if bokstav in vokal: #Sjekker om vokal er i en setning
            antall += 1 #Hvis det er en vokal, går antall opp med 1 for hver gang
    return antall


#Oppgave 2.)
tulleverv = '''\
Tulleveien Velforening
leder: Kari
kasserer: Ole
IT-ansvarlig: Liv
parkeringsansvarlig: Kari
arrangementsansvarlig: Liv
hagekonsulent: Kari
brannansvarlig: Kari
'''
def verv(navn): #Bruker skriver inn: verv('Kari') / verv('Ole') / verv('Liv')
    roller = []

    tvliste = tulleverv.split("\n") #Gjør str til list

    for name in tvliste:
        if name.find(navn)>-1: 
            roller.append(name.split(':')[0]) #Fjerner kolon, og legger til i listen

    return roller
