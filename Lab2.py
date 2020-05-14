from array import *
from builtins import print
import random


# Zadanie 2
# r = {"pierwsza"}
# while True:
#     a = input("Czy chcesz dodać wartość do tablicy?\n Jeśli tak wpisz ją w innym wypadku wciścnij enter bez podawania wartości: ")
#     if  a:
#         r.add(a)
#     else:
#         break
#
# print(r)

# Zadanie 3

# tablica = array('i', [])
#
# print(tablica)
# for i in range(20):
#     tablica.append(random.randint(-5,5))
#
# print(tablica)
# file = open("result.txt", "a")
# for i in tablica:
#     file.write("Liczba losowa: " + str(tablica[i]) + "\n")

#Zadanie 4

# def Funkcja():
#     T = [[2, 3, 4, 5, 6]]
#     l=0
#     for r in T:
#         Bufor = []
#         for c in r:
#             Bufor.append(c*c)
#         T.append(Bufor)
#         l=l+1
#         if  l >= 3:
#             break
#     print(T)
#
# Funkcja()

# Zadanie 5

# def histogram(sciezka):
#     file = open(sciezka, "r")
#     wyraz = file.readline()
#     histo = {}
#
#     for i in wyraz:
#         if i == " ":
#             continue
#         elif i in histo:
#             histo[i] = histo[i]+1
#         else:
#             histo[i] = 1
#     print(histo)
#
# histogram("document.txt")

# Zadanie 6


def deck():
    deck = []
    ranga = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'D', 'K', 'A']
    kolor = ['c', 'd', 'h', 's']
    for r in ranga:
        for k in kolor:
            thistuple = (r,k)
            deck.append(thistuple)
            #print("Dodaję :" + str(thistuple) + "\n")

    #print()
    #print(len(deck))
    return deck

def shuffle_deck(deck):
    random.shuffle(deck)
    return(deck)

def deal(deck, n):
    if  n > 10:
        return
    print("Następuje przyznanie kart:")
    print()
    for g in range(n):
        print("Karty gracza nr." + str(g+1))
        for p in range(5):
            print("\tKarta[" + str(p+1) + "]: "+ str(deck.pop()))

deck = deck()
shuffle_deck(deck)
deal(deck,3)
