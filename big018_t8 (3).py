#big018_t8

#Fortegnelse oppgave 1.)
Eksamen = {'INFO100':'C', 'INFO104':'B', 'INFO116':'E', 'INFO180':'A', 'INFO201':'F',
           'INFO280':'C', 'GEO101':'D', 'GEO110':'B', 'ADM101':'A', 'ECON100':'B',
           'ECON201':'C', 'GEO210': 'C', 'FAIL101':'F'}

#Oppgave 1a.)
def karakterFrekvenser(fortegnelse):
    resultat = {}                           #Tom fortegnelse
    for karakter in fortegnelse.values():   #Sjekker forekomster av karakterer
        resultat[karakter] = list(fortegnelse.values()).count(karakter)
    return resultat                         #Returnerer resultat

f = karakterFrekvenser(Eksamen)
print('1A.)\n\n', f)


#Oppgave 1b.)
def histogram(fortegnelse):
    for i in sorted(fortegnelse):           #Sorterer karakterene
        stjerne = ''
        for n in range(fortegnelse[i]):     #Legger til stjerne for hver forekomst av karakteren
            stjerne += '*'
        print(i, stjerne)                   

print('\n1B.)\n')
histogram(f)

#Fortegnelse oppgave 2.)
engelske_siffer = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
                   5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

#Oppgave 2a.)
def skriv_sortert(fortegnelse):             
    for i in sorted(fortegnelse):           #Går gjennom og sorterer tallende i stigende rekkefølge   
        print(i, fortegnelse[i])

print('\n2A.)\n')
skriv_sortert(engelske_siffer)


#Oppgave 2b.)
def invers(fortegnelse):
    resultat = {}                           #Tom fortegnelse
    for inv in fortegnelse:                 #Looper gjennom slikt at det printes ut flippet
        resultat[fortegnelse[inv]] = inv
    return resultat

inv = invers(engelske_siffer)
print('\n2B.)\n\n', inv)


#Oppgave 2c.)
def skriv_invers_sortert(fortegnelse):
    midlertidig = invers(fortegnelse)
    resultat = {}                           #Tom fortegnelse

    for n in sorted(midlertidig):           #"Flippeloopen" brukes igjen her
        resultat[midlertidig[n]] = n
    for n in resultat:                      #Legges til i tom 'resultat' fortegnelse
        print(n, resultat[n])

del engelske_siffer
print('\n2C.)\n')
skriv_invers_sortert(inv)

