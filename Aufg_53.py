import random as r
import time

def f01():
    """ Bubble Sort """
    lst = list(range(10))
    print(lst)
    tausch = True
    while tausch:
        tausch = False
        for i in range(len(lst)-1):  # -1, da Zugriffe auf i+1 erfolgen, sonst Indexfehler!
            if lst[i] < lst[i + 1]:
                (lst[i], lst[i + 1]) = (lst[i + 1], lst[i])
                tausch = True

    print(lst)

def f02():
    """ Bubble Sort mit weniger Durchläufen? > Anzahl Durchläufe durch weglassen bereits sortierter Elemente
    in Range reduziert """
    Tausche = 0
    Durchlaufe = 0
    bereitsSortiert = 0
    lst = list(range(10))
    print(lst)
    tausch = True
    while tausch:
        tausch = False
        for i in range(len(lst)-1-bereitsSortiert):  # -1, da Zugriffe auf i+1 erfolgen, sonst Indexfehler!
            Durchlaufe += 1
            if lst[i] < lst[i + 1]:
                (lst[i], lst[i + 1]) = (lst[i + 1], lst[i])
                tausch = True
                Tausche += 1
        bereitsSortiert += 1
    print(lst)
    print("Anzahl Tausche & Durchgaenge:", Tausche, Durchlaufe)

def f03():
    """ Folie 5 """
    maxVal = 10000
    for anzahl in [100, 200, 300, 500]:
        Tausche = 0
        Durchlaufe = 0
        bereitsSortiert = 0
        lst = list()
        while len(lst) < anzahl:
            rand = r.randrange(1, maxVal)
            lst.append(rand)
        t0 = time.time()
        tausch = True
        while tausch:
            tausch = False
            for i in range(len(lst) - 1 - bereitsSortiert):  # -1, da Zugriffe auf i+1 erfolgen, sonst Indexfehler!
                Durchlaufe += 1
                if lst[i] > lst[i + 1]:
                    (lst[i], lst[i + 1]) = (lst[i + 1], lst[i])
                    tausch = True
                    Tausche += 1
            bereitsSortiert += 1
        print(anzahl, time.time() - t0)
        print("Anzahl Tausche & Durchgaenge:", Tausche, Durchlaufe)
        lst.clear()


if __name__ == '__main__':
    f03()
