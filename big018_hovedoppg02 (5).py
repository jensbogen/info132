#big018_hovedoppg02

#Besvarelse for oppgave 1 og 2.)
#Bruker trenger ikke å lagre filen når man avslutter med input '5'.
#Tjener samme formål!:)


#Tomme lister
Emner = []
Fagkoder = []
Karakterer = []

#Klasse for emne.
class Emne:
    def __init__(self, emne):
        self.emne = emne

    def leggTil(self):
        Emner.append(self)

    def iListe(self):
        for e in Emner:
            if e.emne == self.emne:
                return True
        return False

    def hentFag(self):
        for f in Fagkoder:
            if f.kode == self.emne[:-3]:
                return f.tilTekst()
        return ''

    def tilTekst(self):
        return self.hentFag() + ' ' + self.emne


#Klasse for fagkode.
class Fagkode:
    def __init__(self, fag, kode):
        self.fag = fag
        self.kode = kode

    def leggTil(self):
        Fagkoder.append(self)

    def iListe(self):
        for f in Fagkoder:
            if f.fag == self.fag:
                return True
        return False

    def tilTekst(self):
        return self.fag

#Klasse for karakterer.
class Karakter:
    def __init__(self, emne, karakter):
        self.emne = emne
        self.karakter = karakter

    def leggTil(self):
        Karakterer.append(self)

    def iListe(self):
        for k in Karakterer:
            if k.emne.emne == self.emne.emne:
                return True
        return False

    def tilTekst(self):
        return self.emne.tilTekst() + ' ' + self.karakter

#Her filen lages.
def start():
    try:
        fil = open('emneInfo.txt', 'r')
    except FileNotFoundError:
        open('emneInfo.txt', 'w').close()
        fil = open('emneInfo.txt', 'r')
    tekst = fil.readlines()
    fil.close()
    if len(tekst) > 0:
        for t in tekst:
            k = t.split()
            emne = Emne(k[1])
            if not emne.iListe():
                emne.leggTil()
            fagkode = Fagkode(k[0], k[1][:-3])
            if not fagkode.iListe():
                fagkode.leggTil()
            try:
                karakter = Karakter(emne, k[2])
                if not karakter.iListe():
                    karakter.leggTil()
            except IndexError:
                pass

    meny()

#Her endringene lagres i fil, også input 5.
def avslutt():
    def write():
        open('emneInfo.txt', 'w').close()
        fil = open('emneInfo.txt', 'w')
        for emne in Emner:
            funnet = False
            ln = ''
            for k in Karakterer:
                if emne.emne == k.emne.emne:
                    funnet = True
                    ln = k.tilTekst() + '\n'
            if not funnet:
                ln = emne.tilTekst() + '\n'
            fil.write(ln)
        fil.close()

    svar = input("Ønsker du å lagre endringene?(j/n) >") 
    if svar.lower() == 'j': #Lagres først her hvis bruker skriver inn j/J.
        write()
    print("Takk for nå")

#Handlinger som bruker har tilgjengelig vises frem her.
def meny():
    menu = '''\n
--------------------
 1 Emneliste
 2 Legg til emne
 3 Sett karakter
 4 Karaktersnitt
 5 Avslutt
--------------------'''
    print(menu)
    skrivTall()


#Her inputen registreres, og gjøres om til tall for beregningens skyld.
def skrivTall():
    num = input("Velg handling (0 for meny)> ")
    if num == '0':
        meny()
    elif num == '1':
        emneliste()
    elif num == '2':
        nytt_emne()
    elif num == '3':
        sett_karakter()
    elif num == '4':
        karaktersnitt()
    elif num == '5':
        avslutt()
    else:
        skrivTall()


#Input 1, viser emnelisten.
def emneliste():
    print("Velg fag og/eller emnenivå (<enter> for alle)")
    fag = input(" - Fag: ").strip()
    nivaa = input(" - Emnenivå: ").strip()
    for emne in Emner:
        if (fag == '' or fag == emne.emne[:-3]) and (nivaa == '' or nivaa[0] == emne.emne[-3]):
            karakter = Karakter('', '')
            for k in Karakterer:
                if emne.emne == k.emne.emne:
                    karakter = k

            print(emne.emne, karakter.karakter)

    skrivTall()


#Input 2, legger til nytt emne.
def nytt_emne():
    emne = input(" - Emne: ").strip().upper()
    if len(emne) >= 6 and emne[-3] in ['1', '2', '3']:
        finnes = False
        for fag in Fagkoder:
            if str.upper(fag.kode) == emne[:-3]:
                finnes = True

        if finnes and emne not in Emner:
            nyttemne = Emne(emne)
            nyttemne.leggTil()
        elif not finnes:    #Failproofing
            fagnavn = input("Fag ikke registrert.\n - Skriv fagnavn: ").strip()
            Fagkoder.append(Fagkode(fagnavn, emne[:-3]))
            nyttemne = Emne(emne)
            nyttemne.leggTil()

        skrivTall()
    else:
        print("Emne er ikke gyldig.")
        skrivTall()


#Input 3, setter karakterer for hvert fag.
def sett_karakter():
    emnenavn = input(" - Emne: ").strip().upper()
    emne = Emne('')
    for e in Emner:
        if e.emne == emnenavn:
            emne = e
    if emne.emne != '':
        karakter = input(" - Karakter (<enter> for å slette): ").strip().upper()
        if karakter == "":
            slette = Karakter
            for k in Karakterer:
                if k.emne == emne:
                    slette = k

            Karakterer.remove(slette)
            print('Karakter slettet!')
            skrivTall()
        elif karakter not in ['A', 'B', 'C', 'D', 'E', 'F'] or len(karakter) > 1:   #Mer failproofing
            print("Ikke gyldig karakter.")
            skrivTall()
        else:
            nyKarakter = Karakter(emne, karakter)
            finnes = False
            for i in range(len(Karakterer)):
                if Karakterer[i].emne == emne:
                    Karakterer[i] = nyKarakter
                    finnes = True

            if not finnes:
                nyKarakter.leggTil()

            skrivTall()
    else:
        print("Emne finnes ikke i emnelisten.")
        skrivTall()


#Input 4, regner ut karaktersnitt
def karaktersnitt():
    print("Velg fag og/eller emnenivå (<enter> for alle)")
    fag = input(" - Fag: ").strip()
    nivaa = input(" - Emnenivå: ").strip()
    nivaer = []
    for f in Fagkoder:
        if fag == '' or fag.lower() == f.fag.lower() or fag.upper() == f.kode.upper():
            nivaer.append(f) #Legger til i Karakter listen

    if len(nivaer) == 0:
        print("Fag ikke funnet.")
        skrivTall()
    else:
        karak = []
        for k in Karakterer:
            for f in nivaer:
                if (f.kode == k.emne.emne[:-3]) and (nivaa == '' or nivaa[0] == k.emne.emne[-3]):
                    karak.append(k.karakter)

        if len(karak) == 0:
            print("Ingen karakterer ble funnet.")
            skrivTall()
        else:
            a = 0
            b = 0
            c = 0
            d = 0
            e = 0
            
            for kar in karak:
                if str(kar).lower() == 'a':
                    a += 6
                elif str(kar).lower() == 'b':
                    b += 5
                elif str(kar).lower() == 'c':
                    c += 4
                elif str(kar).lower() == 'd':
                    d += 3
                elif str(kar).lower() == 'e':
                    e += 2

            gjennomsnitt = (a + b + c + d + e) / len(karak)
            
            if int(gjennomsnitt) == 2:
                gjKar = 'E'
            elif int(gjennomsnitt) == 3:
                gjKar = 'D'
            elif int(gjennomsnitt) == 4:
                gjKar = 'C'
            elif int(gjennomsnitt) == 5:
                gjKar = 'B'
            elif int(gjennomsnitt) == 6:
                gjKar = 'A'
            else:
                gjKar = 'F'
            print("Snitt:", gjKar)
            skrivTall()


start()
