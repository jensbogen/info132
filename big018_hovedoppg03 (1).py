#big018_hoved03
#Wish Solitaire the Jens way


import os.path
import random as r


def start(): 
    kortStokk = []

    stokkA = []
    
    stokkB = []

    stokkC = []

    stokkD = []

    stokkE = []

    stokkF = []

    stokkG = []

    stokkH = []

    alleStokker = [stokkA, stokkB, stokkC, stokkD, stokkE, stokkF, stokkG, stokkH]
    
    for symboler in ['\u2660', '\u2666', '\u2663', '\u2665']:
        for tall in [7, 8, 9, 10, 'J', 'Q', 'K', 'A']:
            kortStokk.append((symboler, str(tall)))

    for i in alleStokker:
        if len(kortStokk) > 0:
            while len(i) <= 3:
                c = r.choice(kortStokk) #choice() metode velger et tilfeldig element fra liste
                i.append(c)
                kortStokk.remove(c)

    return alleStokker


def writeStack(noe): #Skriver frem hver "runde" av spillet
    for i in noe:
        if i == None:
            a == '--'
            return a
        
        elif i == []:
            b == '--'
            return b

        else:
            c = "".join(map(str, noe[0]))
            return c


def check(noe): #check() sjekker om det er noen muligheter igjen for å vinne for brukeren.
    antall = 0
    
    for a in noe:
        if a == None:
            continue
        
        for b in noe:
            if b == None:
                continue

            elif a[1] == b[1] and a != b:
                antall+=1

    if antall > 0:
        return True
    else:
        return False


def letters(): #letters() failproofer brukererrors. 
    while True:
        brukerInp = input(': ').upper()
        lovligeTegn = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'SAVE'] #Kun elementene i listen kan skrives av brukeren

        if brukerInp == 'SAVE': #SAVE trigrer lagring
            return brukerInp
        elif brukerInp in lovligeTegn:
            return lovligeTegn.index(brukerInp)
        else:
            print('\n??WTF?? - Please choose a letter from A-H.\n')


def win(noe): #win() sjekker om bruker har vunnet eller tapt.
    antall = 0
    for a in noe:
        if a != []:
            antall+=1
            
    if antall > 0:
        print('\nNo possible ways to win - better luck next time.\n')
        
    else:
        print('\nGGWP - You won!\n')


def stackSize(noe): #stackSize() skriver ut antall kort som er igjen i bunken.
    liste = []
    for i in noe:
        liste.append('    '+str(len(i))+' ')
    return liste


def saveGame(noe): #Lagrer spillet.
    gamesave = open('WishSolitaireGameSaves.txt', 'w')
    
    for a in noe:
        gamesave.write(str(a))
        gamesave.write('\n')
    gamesave.close()


def loadGame(): #Laster inn spillet.
    if os.path.exists('WishSolitaireGameSaves.txt') == True: #os.path() for å sjekke om filen eksisterer
        gamesave = open('WishSolitaireGameSaves.txt', 'r') #deretter loade inn saven :D
        liste = []
        
        for i in gamesave:
            liste.append(eval(i)) #Fjerner tegn osv.
        
        else:
            return liste

    gamesave.close()


while True: #Startmeny
    print('!!!WISH SOLITAIRE!!!')
    print('--------------------')
    print('1 - START GAME')
    print('2 - LOAD GAME')
    print('--------------------')
    spillerValg = int(input('- : '))

    if spillerValg == 1:
        game = start()
    elif spillerValg == 2:
        game = loadGame()
    else:
        print('\n??WTF?? - Choose 1 or 2, is it that hard?\n')


    go = True
    lagreSpill = False


    while go == True:
        current = list(map(writeStack, game))
        currentTwo = []

        for i in current:
            if i == None:
                currentTwo.append('--')
            else:
                currentTwo.append(i)

        go = check(current)

        print('    A     B     C     D     E     F     G     H') #Spillet som vises
        print(currentTwo)
        print(''.join(stackSize(game)))

        if go == False:
            break
        
        print('Write SAVE, to save and quit the current game.')
        print('Choose first stack!')
        sjekk = letters()

        if sjekk == 'SAVE':
            saveGame(game)
            lagreSpill = True
            break

        print('Choose second stack!')
        sjekkTo = letters()

        try: #Sjekker om verdiene er like.
            if current[sjekk][1] == current[sjekkTo][1]:
                game[sjekk].remove(game[sjekk][0])
                game[sjekkTo].remove(game[sjekkTo][0])
            
            else:
                print('\n??WTF?? - Choose two equal numbers.\n')

        except:
            print('\n??WTF?? - You have chosen an empty stack.\n')

    if lagreSpill is True:
        print('Game is saved.')
    else:
        win(game)
