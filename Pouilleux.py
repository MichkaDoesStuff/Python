# Jeu de cartes appelé "Pouilleux" 

# L'ordinateur est le donneur des cartes.

# Une carte est une chaine de 2 caractères. 
# Le premier caractère représente une valeur et le deuxième une couleur.
# Les valeurs sont des caractères comme '2','3','4','5','6','7','8','9','10','J','Q','K', et 'A'.
# Les couleurs sont des caractères comme : ♠, ♡, ♣, et ♢.
# On utilise 4 symboles Unicode pour représenter les 4 couleurs: pique, coeur, trèfle et carreau.
# Pour les cartes de 10 on utilise 3 caractères, parce que la valeur '10' utilise deux caractères.

import random

def attend_le_joueur():
    '''()->None
    Pause le programme jusqu'au l'usager appui Enter
    '''
    try:
         input("Appuyez Enter pour continuer. ")
    except SyntaxError:
         pass


def prepare_paquet():
    '''()->list of str
        Retourne une liste des chaines de caractères qui représente tous les cartes,
        sauf le valet noir.
    '''
    paquet=[]
    couleurs = ['\u2660', '\u2661', '\u2662', '\u2663']
    valeurs = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for val in valeurs:
        for couleur in couleurs:
            paquet.append(val+couleur)
    paquet.remove('J\u2663') # élimine le valet noir (le valet de trèfle)
    return paquet

def melange_paquet(p):
    '''(list of str)->None
       Melange la liste des chaines des caractères qui représente le paquet des cartes    
    '''
    random.shuffle(p)

def donne_cartes(p):
     '''(list of str)-> tuple of (list of str,list of str)

     Retournes deux listes qui représentent les deux mains des cartes.  
     Le donneur donne une carte à l'autre joueur, une à lui-même,
     et ça continue jusqu'à la fin du paquet p.
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

     Retourne une copy de la liste l avec tous les paires éliminées 
     et mélange les éléments qui restent.

     Test:
     (Notez que l’ordre des éléments dans le résultat pourrait être différent)
     
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
    Affiche les éléments de la liste p séparées par d'espaces
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
     Retourne un entier du clavier, de 1 à n (1 et n inclus).
     Continue à demander si l'usager entre un entier qui n'est pas dans l'intervalle [1,n]
     Précondition: n>=1
     '''
     print("J'ai " + str(n) + " cartes. Si 1 est la position de ma première carte et " + str(n) + " la position de ma dernière carte, laquelle de mes cartes voulez-vous?")
     nombre_choisi = input("SVP entrez un entier de 1 à " + str(n) + " : ")
     list_of_options = []
     for i in range(1, (n+1)):
         list_of_options.append(str(i))
     #    i += 1
     while nombre_choisi not in list_of_options:
         nombre_choisi = input("Position invalide. SVP entrez un entier de 1 à " + str(n) + " : ")         
     nombre_choisi = int(nombre_choisi)
     return(nombre_choisi)
    
def humain_choisi(nombre_choisi, donneur):                  #personal function
     '''
     (int, list)->str
     l'humain choisi sa carte, au choix, de la main du donneur (robot)
     '''
     suffixe = "-ème" if nombre_choisi != 1 else "-ère"
     print("Vous avez demandé ma " + str(nombre_choisi) + suffixe + " carte.")
     carte_choisie_humain = donneur[nombre_choisi-1]
     print("La voilà. C'est un", carte_choisie_humain)
     print("Avec " + carte_choisie_humain + " ajouté, votre main est:")
     return(carte_choisie_humain)

def donneur_choisi(n):                                      #personal function
    '''
    (list)->str
    n = humain
    le donneur (robot) choisi sa carte, au hazard, de la main de l'humain
    '''
    a = random.choice(n)
    for index in range(len(n)+1):
        if a == n[index]:
            carte_choisie_donneur = a
            i = index
            i += 1
            break
    suffixe = "-ème" if i != 1 else "-ère"
    print("J'ai pris votre " + str(i) + suffixe + " carte.")
    return(carte_choisie_donneur)
    

def ajouter_enlever_cartes(carte, l_add, l_rem):            #personal function
    '''
    (str, list, list)->list, list
    Ajouter la carte_choisie au deck de la personne qui la choisie et l'enlever du deck de l'opposition
    '''
    l_add.append(carte)
    l_rem.remove(carte)
    return(l_rem, l_add)

def ui_start(n_jeu):                                        #personal function
    '''
    (int)->None
    text UI pour le début, influencé par l'incrémentation du nombre de joutes
    '''
    print("======================================================================")
    print("Jeu " + str(n_jeu))
    print("======================================================================")

def ui_mid():                                               #personal function
    '''
    ()->None
    text UI pour les spéarations des tours
    '''
    print("***********************************************************")

def ui_end_robot():                                         #personal function
    '''
    ()->None
    messages pour la victoire du robot
    '''
    print("J'ai terminé toutes les cartes.")
    print("Vous avez perdu! Moi, Robot, j'ai gagné.")
    
def ui_end_humain():                                        #personal function
    '''
    ()->None
    messages pour la victoire de l'humain
    '''
    print("Vous avez terminé toutes les cartes.")
    print("Félicitations! Vous, Humain, vous avez gagné.")

def nouvelle_joute(n):                                      #personal function
    '''
    (int)->bool
    verifier si le joueur veut continuer de jouer après 1 joute
    '''
    verdict = True
    if n > 1:
        n = input("Voulez-vous jouer une autre manche? (oui ou non): ")
        options = ['oui', 'non']
        while n not in options:
            print("Pardon? Je ne peux lire cette monstruosité d'écriture. SVP suivre la syntaxe ci-dessous")
            n = input("(oui ou non): ")
        if n == options[1]:
            verdict = False
        else:
            pass
    return(verdict)
        
def joue():
    '''
    ()->None
    Cette fonction joue le jeu
    '''
    joutes = 0
    while True:                         #incrémentation des joutes
        joutes += 1
        verdict = nouvelle_joute(joutes)
        if verdict == True:
            p=prepare_paquet()
            melange_paquet(p)
            tmp=donne_cartes(p)
            donneur=tmp[0]
            humain=tmp[1]
    
            ui_start(joutes)
            print("Bonjour. Je m'appelle Robot et je distribue les cartes.")
            print("Votre main est:")
            affiche_cartes(humain)
            print("Ne vous inquiétez pas, je ne peux pas voir vos cartes ni leur ordre.")
            print("Maintenant défaussez toutes les paires de votre main. Je vais le faire moi aussi.")
            attend_le_joueur()
            tour = -1
            while True:                     #incrémentation des tours
                tour += 1
                if(len(donneur)) == 0:
                    ui_end_robot()
                    break
                elif(len(humain)) == 0:
                    ui_end_humain()
                    break
                elif(tour % 2 == 0):
                    ui_mid()
                    print("Votre tour.")
                    print("Votre main est:")
                    elimine_paires(donneur)
                    elimine_paires(humain)
                    affiche_cartes(humain)

                    #print("donneur")                #pour aider avec la creation
                    #affiche_cartes(donneur)         #pour aider avec la creation
                
                    nombre_choisi = entrez_position_valide(len(donneur))
                    carte_choisie_humain = humain_choisi(nombre_choisi, donneur)
                    ajouter_enlever_cartes(carte_choisie_humain, humain, donneur)
                    affiche_cartes(humain)
                    print("Après avoir défaussé toutes les paires et mélanger les cartes, votre main est:")
                    elimine_paires(humain)
                    affiche_cartes(humain)
                    attend_le_joueur()
                else:
                    ui_mid()
                    print("Mon tour.")
                
                    #print("donneur")                #pour aider avec la creation
                    #affiche_cartes(donneur)         #pour aider avec la creation
                
                    carte_choisie_donneur = donneur_choisi(humain)
                    ajouter_enlever_cartes(carte_choisie_donneur, donneur, humain)
                    attend_le_joueur()
        else:
            break
    return()
# programme principale
joue()


