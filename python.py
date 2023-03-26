import time
from random import *


def numeros(quantidade): #Geração de número randomico
    lista = [0] * quantidade

    for i in range(quantidade):
        lista[i] = randint(1,100000)

    return lista

def simples(lista): #Buble sort
    n = len(lista) #Lista para ser ordenada
    for i in range(n): #Range a ser percorrido
        for j in range(0, n-i-1): #i = indice atual, j = proximo elemento 
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

def eficiente(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = lista[:meio]
    direita = lista[meio:]

    esquerda = eficiente(esquerda)
    direita = eficiente(direita)

    return merge(esquerda, direita)


def merge(esquerda, direita):
    listaFinal = []
    i = 0
    j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] <= direita[j]:
            listaFinal.append(esquerda[i])
            i += 1
        else:
            listaFinal.append(direita[j])
            j += 1

    listaFinal += esquerda[i:]
    listaFinal += direita[j:]
    return listaFinal


print ("Execuções com o Buble Sort")
print("================================================")
print("100 Elementos")
inicial = time.time()
lista = numeros(100)
simples(lista)
final = time.time() - inicial
#print("lista:\n", lista, "\n\nTempo: ", final)
print("Tempo 100: ", final)
print("================================================")
print("1000 Elementos")
inicial = time.time()
lista = numeros(1000)
simples(lista)
final = time.time() - inicial
#print("lista:\n", lista, "\n\nTempo: ", final)
print("Tempo 1000: ", final)
print("================================================")
print("10000 Elementos")
inicial = time.time()
lista = numeros(10000)
simples(lista)
final = time.time() - inicial
#print("lista:\n", lista, "\n\nTempo: ", final)
print("Tempo 10000: ", final)
print("================================================")
print("100000 Elementos")
inicial = time.time()
lista = numeros(100000)
simples(lista)
final = time.time() - inicial
#print("lista:\n", lista, "\n\nTempo: ", final)
print("Tempo 100000: ", final)


print("================================================")
print("================================================")

print("Execução com o Marge Sort")
print("================================================")
print("100 Elementos")
inicial = time.time()
lista = numeros(100)
eficiente(lista)
final = time.time() - inicial
#print("lista:\n", lista, "\n\nTempo: ", final)
print("Tempo 100: ", final)
print("================================================")
print("1000 Elementos")
inicial = time.time()
lista = numeros(1000)
eficiente(lista)
final = time.time() - inicial
#print("lista:\n", lista, "\n\nTempo: ", final)
print("Tempo 1000: ", final)
print("================================================")
print("10000 Elementos")
inicial = time.time()
lista = numeros(10000)
eficiente(lista)
final = time.time() - inicial
#print("lista:\n", lista, "\n\nTempo: ", final)
print("Tempo 10000: ", final)
print("================================================")
print("100000 Elementos")
inicial = time.time()
lista = numeros(100000)
eficiente(lista)
final = time.time() - inicial
#print("lista:\n", lista, "\n\nTempo: ", final)
print("Tempo 100000: ", final)
