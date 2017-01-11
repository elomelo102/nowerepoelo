import random

tab = []

for i in range(50):
    tab.append(random.randint(0,200))

print(tab)



def wstawianie(tab):
    for i in range(1, len(tab)):
        klucz = tab[i]
        j = i-1
        while j >= 0 and tab[j] > klucz:
            tab[j+1] = tab[j]
            j -= 1
        tab[j+1] = klucz

def wybieranie(tab):
    for i in range(0, len(tab)):
        for j in range(0, len(tab)):
            if tab[j] > tab[i]:
                tab[j], tab[i] = tab[i], tab[j]

def bubble(tab):
    for i in range(0, len(tab)):
        for j in range(0, len(tab)-i-1):
            if tab[j] > tab[j+1]:
                tab[j],tab[j+1] = tab[j+1], tab[j]

bubble(tab)
print(tab)
