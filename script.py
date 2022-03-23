import pandas as pd
from math import *
from random import randint
from itertools import permutations
from pandas import *
from time import *
"""
Module à import : math et random
Le programme prend trois fonctions, une fonction angramme, une fonction maths, une fonction exe
La fonction anagramme prend en argument un chaine de caractère, et trouve le mot correct en y incluant une base de donnée.
"""
def verification(c):
    c=c.lower()
    listing=pd.read_csv("Lexique383.csv")
    searching=listing[(listing["1_ortho"] == c)]
    if len(searching)>0:
        return True
    return False

def verification_txt(c):
    c=c.lower()
    fichier=open("pli07.txt","r")
    l=[]
    for i in fichier:
        i=i.replace('\n',"")
        i=i.lower()
        l.append(i)
    if c in l:
        return True
    return False

def search_word():
    listing=pd.read_csv("Lexique383.csv")
    index=len(listing["1_ortho"])
    word_rand=randint(0,index+1)
    word=listing["1_ortho"][word_rand]
    return word

def search_word_txt():
    fichier=open("pli07.txt","r")
    l=[]
    for i in fichier:
        i=i.replace('\n',"")
        i=i.lower()
        l.append(i)
    word_rand=randint(0,len(l)+1)
    word=l[word_rand]
    if len(word)>10:
        search_word_txt()
    return word

def math():
    #lvl=int(input("Niveau de difficulté des calcul entre 1 et 10"))
    a=randint(0,10)
    b=randint(0,10)
    return a,b

def arrangement(c):
    """Prend en argument une chaine de caractère et retourne le nombre d'arangement possible de ce mot"""
    factorielle = lambda n: n * factorielle(n-1) if n != 0 else 1
    return factorielle(len(c))

#print(arrangement("bonjour"))

def anagramme(c):
    debut=time()
    """Prend en argument une chaine de caractère et retourne le mot existant dans le bon ordre."""
    c=c.lower()
    print(f"Le nombre de combinaison possible du mot est : {arrangement(c)}")
    print(f"Le mot à {len(c)} lettres")
    a=[''.join(p) for p in permutations(c)]
    ana_rand=randint(1,len(a))
    #print(f"ana_rang : {ana_rand}")
    anag=a[ana_rand-1]

    if verification_txt(c)==False:
        print("Le mot est absent de la base de donnée!")
        return None
    print("Le mot est présent dans la base de donnée !")

    i=0
    mem=[] #Memoire des lettres trouvés
    while i!=len(c):
        x,y=math()
        res=int(input(f"Veuillez rentrer de resultat de {x}x{y} :"))
        if res==x*y:
            mem.append(anag[i])
            print(f"Lettre trouvé : {anag[i]}")
            i+=1
        else:
            print(f"Perdu, le résultat était {x*y}")
            return None
    print("Bravo voici les lettres trouvées :",end=" ")
    for i in range(len(anag)):
        print(anag[i],end="")
    print("")
    mot=input("Quel est le mot mystere ? : ")
    
    if mot==c:
        print("Vous avez gagné ! Félicitation !")
        return None
    print(f"Dommage vous avez perdu, le mot était {c}")
    fin=time()
    print(f"Essai effectué en {floor(fin-debut)} secondes")

    
    


anagramme(search_word_txt())