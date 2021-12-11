#big018_t7

#Oppgave 1.)                        #Bruker skriver inn sitt navn og nummer
nn = input('Navn og nummer: ')

fil = open('telefon.txt', 'a') 
fil.write('\n' + nn)                #Linjeskift pluss verdier fra 'nn'.
fil.close()

#Åpner man telefon.txt filen, så er verdiene lagt til.


#Oppgave 2.)
import os

fil = 'telefon.txt'
nyfil = 'ny-' + fil
original = open(fil)
ny = open(nyfil, 'w')

navn = input('Navn: ')

for linje in original:
    if linje.startswith(navn): #Sjekker hvilken person vi skal endre i filen
        oldnum = linje[len(navn)+1:-1] #Henter ut gamle nummeret
        print('Gammelt telefonnummer: ', oldnum) #Printer ut gamle nummeret

        newnum = input('Nytt nummer: ')
        ny.write(navn + ' ' + newnum + '\n')

    else:
        ny.write(linje)

original.close()
ny.close()

os.remove(fil) #Fjerner originalfilen 'telefon.txt'
os.rename(nyfil, fil) #Omdøper filen til 'telefon.txt' igjen :)

#Oppgave 3.)
vokaler = ('a', 'e', 'i', 'o', 'u', 'y', 'æ', 'ø', 'å')

def fjernVokaler(filnavn, encoding): #Bruker skriver inn filnavn på filen de vil ha endret, og encodingen til filen.
    mvokaler = open(filnavn, encoding=encoding) 
    uvokaler = open('uten-vokaler-' + filnavn, 'w') #Lager ny fil
    
    for i in mvokaler:
        for bokstav in i:
            if bokstav not in vokaler: #Sjekker om bokstaven er en vokal
                uvokaler.write(bokstav); #Skriver ut tekst uten vokalene i ny fil
                
    mvokaler.close()
    uvokaler.close()
        
fn = 'tre-små-kinesere.txt'
print(fjernVokaler(fn, 'UTF-8')) #Sjekker man den nye filen har den ikke vokaler

