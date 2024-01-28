# A card game called "Pouilleux". 

# The computer is the card dealer.

# A card is a string of 2 characters. 
# The first character represents a value and the second a suit.
# Values are characters like '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', and 'A'.
# Colors are characters like: ♠, ♡, ♣, and ♢.
# We use 4 Unicode symbols to represent the 4 suits: spades, hearts, clubs and diamonds.
# For cards of 10 we use 3 characters, because the value '10' uses two characters.

import random

def attend_le_joueur():
    '''()->None
    Pause program until user presses Enter
    '''
    try:
         input("Press Enter to continue.")
    except SyntaxError:
         pass


def prepare_paquet():
    '''()->list of str
        Returns a list of strings representing all cards,
        except the black jack.
    '''
    paquet=[]
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for val in valeurs:
        for couleur in couleurs:
            paquet.append(val+couleur)
    paquet.remove('J\u2663') # eliminates the black jack (jack of clubs)
    return paquet

def melange_paquet(p):
    '''(list of str)->None
       Mix the list of strings representing the pack of cards    
    '''
    random.shuffle(p)

def donne_cartes(p):
     '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing the two hands of cards.  
     The dealer gives one card to the other player, one to himself,
     and so on until the end of pack p.
     '''
     
     donneur=[]
     autre=[]
     i = 0
     for i in range(len(p)):
         if i % 2 == 0:
             autre.append(p[i])
         else:
             donneur.append(p[i])
     return (donneur, autre)


def elimine_paires(l):
    '''
     (list of str)->list of str

     Returns a copy of list l with all pairs eliminated 
     and shuffles the remaining elements.

     Test:
     (Note that the order of the elements in the result may be different)
     
     >>> elimine_paires(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> elimine_paires(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    resultat=[]
    i = 0
    n = 0
    for i in range(len(l)):
        if i >= (len(l)-1):
            break
        if l[i] == "y":
            continue
        for n in range(len(l)):
            if (i+n+1) >= (len(l)):
                break
            if l[i][0] == l[i+n+1][0]:
                l[i]="y"
                l[i+n+1]="y"
                break
    while 'y' in l:
        l.remove('y')
    random.shuffle(l)
    return l


def affiche_cartes(p):
    '''
    (list)->None
    Displays elements of list p separated by spaces
    '''
    global no_spaces
    no_spaces = ""
    for u in range(len(p)):
        no_spaces += p[u] + " "
        u += 1
    print(no_spaces)

def entrez_position_valide(n):
     '''
     (int)->int
     n = len(donneur)
     Returns an integer from the keyboard, from 1 to n (1 and n included).
     Continues to ask if the user enters an integer not in the interval [1,n].
     Precondition: n>=1
     '''
     print("I have " + str(n) + " cards. If 1 is the position of my first card and " + str(n) + " is the position of my last card, from which of my cards do you want to pick?")
     nombre_choisi = input("Please enter an integer between 1 and " + str(n) + " : ")
     list_of_options = []
     for i in range(1, (n+1)):
         list_of_options.append(str(i))
     #    i += 1
     while nombre_choisi not in list_of_options:
         nombre_choisi = input("Invalid position. Please enter an integer between 1 and " + str(n) + " : ")         
     nombre_choisi = int(nombre_choisi)
     return(nombre_choisi)
    
def humain_choisi(nombre_choisi, donneur):                  
     '''
     (int, list)->str
     the human chooses a card from the dealer's hand (robot)
     '''
     if nombre_choisi == 1:
         suffixe = "st"
     elif nombre_choisi == 2:
         suffixe = "nd"
     elif nombre_choisi == 3:
         suffixe = "rd"
     else: suffixe = "th"
     print("You asked for my " + str(nombre_choisi) + suffixe + " card.")
     carte_choisie_humain = donneur[nombre_choisi-1]
     print("Here it is, it's a ", carte_choisie_humain)
     print("With " + carte_choisie_humain + " added, your new hand is:")
     return(carte_choisie_humain)

def donneur_choisi(n):                                      
    '''
    (list)->str
    n = humain
    the dealer (robot) chooses his card, at random, from the human's hand
    '''
    a = random.choice(n)
    for index in range(len(n)+1):
        if a == n[index]:
            carte_choisie_donneur = a
            i = index
            i += 1
            break
    if i == 1:
         suffixe = "st"
    elif i == 2:
         suffixe = "nd"
    elif i == 3:
         suffixe = "rd"
    else: suffixe = "th"
    print("I took your " + str(i) + suffixe + " card.")
    return(carte_choisie_donneur)
    

def ajouter_enlever_cartes(carte, l_add, l_rem):            
    '''
    (str, list, list)->list, list
    Add the carte_choisie to the chooser's deck and remove it from the opposition's deck.
    '''
    l_add.append(carte)
    l_rem.remove(carte)
    return(l_rem, l_add)

def ui_start(n_jeu):                                        
    '''
    (int)->None
    text UI for the start, influenced by the incremental number of games
    '''
    print("======================================================================")
    print("Jeu " + str(n_jeu))
    print("======================================================================")

def ui_mid():                                               
    '''
    ()->None
    text UI for separation of turns
    '''
    print("***********************************************************")

def ui_end_robot():                                         
    '''
    ()->None
    robot victory message
    '''
    print("I finished with all the cards.")
    print("I, the almighty Mr Robot, won the game!")
    
def ui_end_humain():                                        
    '''
    ()->None
    human victory message
    '''
    print("You finished with all the cards.")
    print("Congratulations! You, human, have won against the all-mighty Mr Robot!")

def nouvelle_joute(n):                                      
    '''
    (int)->bool
    verify if player wants to play another game
    '''
    verdict = True
    if n > 1:
        n = input("Want to play another round? (yes or no): ")
        options = ['yes', 'no']
        while n not in options:
            print("Sorry, even though I am the best game robot, my vocabulary still is something I need to work on... Please specify")
            n = input("(yes or no): ")
        if n == options[1]:
            verdict = False
        else:
            pass
    return(verdict)
        
def joue():
    '''
    ()->None
    This function plays the game
    '''
    joutes = 0
    while True:                         #round incrementations
        joutes += 1
        verdict = nouvelle_joute(joutes)
        if verdict == True:
            p=prepare_paquet()
            melange_paquet(p)
            tmp=donne_cartes(p)
            donneur=tmp[0]
            humain=tmp[1]
    
            ui_start(joutes)
            print("Hi, I am the almighty game Robot, I'll distribute the cards.")
            print("Your hand is:")
            affiche_cartes(humain)
            print("Don't you worry, I can't see your hand.")
            print("Now, get rid of all pairs from your hand of cards. I'll do the same.")
            attend_le_joueur()
            tour = -1
            while True:                     #turn incrementations
                tour += 1
                if(len(donneur)) == 0:
                    ui_end_robot()
                    break
                elif(len(humain)) == 0:
                    ui_end_humain()
                    break
                elif(tour % 2 == 0):
                    ui_mid()
                    print("Your turn.")
                    print("Your hand is:")
                    elimine_paires(donneur)
                    elimine_paires(humain)
                    affiche_cartes(humain)

                    #print("donneur")                #code checkpoint.
                    #affiche_cartes(donneur)         #code checkpoint.
                
                    nombre_choisi = entrez_position_valide(len(donneur))
                    carte_choisie_humain = humain_choisi(nombre_choisi, donneur)
                    ajouter_enlever_cartes(carte_choisie_humain, humain, donneur)
                    affiche_cartes(humain)
                    print("After haaving removed all pairs and shuffled, your hand is:")
                    elimine_paires(humain)
                    affiche_cartes(humain)
                    attend_le_joueur()
                else:
                    ui_mid()
                    print("My turn.")
                
                    #print("donneur")                #code checkpoint.
                    #affiche_cartes(donneur)         #code checkpoint.
                
                    carte_choisie_donneur = donneur_choisi(humain)
                    ajouter_enlever_cartes(carte_choisie_donneur, donneur, humain)
                    attend_le_joueur()
        else:
            break
    return()
# main program
joue()


