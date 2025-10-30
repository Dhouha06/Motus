import unicodedata
import random

def clean_word(word):
    mot=""
    for ch in word:
        if ch.isalpha():
            mot +=ch
    mot=unicodedata.normalize('NFD',mot)
    mot="".join(c for c in mot if unicodedata.category(c)!='Mn')
    return mot.upper()

def load_words(filename):
    mots=[]
    with open(filename,"r",encoding="utf-8")as f:
        for ligne in f:
            mot=clean_word(ligne.strip())
            if mot!="":
                mots.append(mot)
    return mots 

def get_words_dict(listemots):
    dico={}
    for mot in listemots:
        n=len(mot)
        if n not in dico:
            dico[n]=[]
        dico[n].append(mot)
    return dico

def random_word(n,dico):
    if n not in dico:
        return None
    return random.choice(dico[n])

def check_word(secret,propo):
    taille=len(secret)
    resultat=[-1]*taille
    reste=list(secret)
    for i in range(taille):
        if propo[i]==secret[i]:
            resultat[i]=1
            reste[i]=None
    for i in range(taille):
        if resultat[i]==-1 and propo[i]in reste:
            resultat[i]=0
            index=reste.index(propo[i])
            reste[index]=None 
    return resultat

def print_clues(mot,indice):
    for i in range(len(mot)):
        if indice[i]==1:
            print(mot[i]+" ",end=" ")
        elif indice[i]==0:
            print("("+mot[i]+")",end=" ")
        else:
            print("("+"_"+")",end=" ")
    print()

def play(dico,word_len,max_tries):
    secret=random_word(word_len,dico)
    print(" _ "*word_len)
    print(secret)
    for essai in range(1,max_tries+1):
        propo=input(f"{essai} .MOT?").strip().upper()
        if len(propo)!=word_len:
            print("attention le mot doit avoir",word_len,"lettres")
            continue
        if propo not in dico[word_len]:
            print("mot propose pas dans le dictionnaire")
            continue
        indices=check_word(secret,propo)
        print_clues(propo,indices)
        if propo==secret:
            print(f"GAGNE EN {essai} coups")
            a=input("voulez vous rejouez?")
            if a=="oui":
                play(a,5,5)
            break 
        if essai==max_tries:
            print("PERDU")
            a=input("voulez vous rejouez?")
            if a=="oui":
                play(a,5,5)
            break 



b=load_words("frenchDict.txt")
a=get_words_dict(b)
play(a,5,5)