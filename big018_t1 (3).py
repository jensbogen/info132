#Oppgave 1:

#Brukte 'sep='\n'' for å separere linjene slikt som vi lærte i den første forelesningen.
print('Jens', 'Vu', 'Bogen', sep= '\n')

print('Jens')
print('Vu')
print('Bogen')

#Oppgave 2:
print('******  *****  *     *   ****')
print('     *  *      **    *  *    *')
print('     *  *      * *   *  *')
print('     *  *****  *  *  *   ****')
print('*    *  *      *   * *       *')
print('*    *  *      *    **  *    *')
print(' ****   *****  *     *   ****')
print('>>>')

#Oppgave 3a:

#Slik jeg har gjort det gjør programmet fleksibelt grunnet bruk av konvertering til de ulike valutaene.

kroner_input = float(input('Skriv inn kroner: '))
dollar = kroner_input*0.12
euro = kroner_input*0.097
d = ('%.2f' % (dollar))
e = ('%.2f' % (euro))

print('Tilsvarer i', 'dollar:', d, 'og', 'euro:', e)

#Oppgave 3b:

#La til '(u"\N{euro sign}")' og '(u"\N{dollar sign}"' inne i print etter 'd' og 'e'. 

kroner_input = float(input('Skriv inn kroner: '))
dollar = kroner_input*0.12
euro = kroner_input*0.097
d = ('%.2f' % (dollar))
e = ('%.2f' % (euro))

print('Tilsvarer i', 'dollar:', d,(u"\N{euro sign}") , 'og', 'euro:', e,(u"\N{dollar sign}"))











