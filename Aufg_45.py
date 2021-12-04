import random as r
import time

# Aufgabe S. 4
# r.seed()
# r_lst = [r.random(), r.random(), r.random(), r.random(), r.random()]
# r.seed()
# r_lst2 = [r.random(), r.random(), r.random(), r.random(), r.random()]
#
# # Aufgabe S. 5
# r.seed(1234)
# r_lst3 = [r.random(), r.random(), r.random(), r.random(), r.random()]
# r.seed(1234)
# r_lst4 = [r.random(), r.random(), r.random(), r.random(), r.random()]
# r.seed(1235)
# r_lst5 = [r.random(), r.random(), r.random(), r.random(), r.random()]
#
# # Aufgabe S. 6
# r.seed(1)
# r_lst6 = [r.randrange(10, 56, 2), r.randrange(10, 56, 2), r.randrange(10, 56, 2), r.randrange(10, 56, 2), r.randrange(10, 56, 2)]
#
# # Aufgabe S. 7
# # -- V1 --
# anzahl = 9900
# maxVal = 10000
# t0 = time.time()
# print("Start")
# # Hier kommt das Verfahren rein
# i = 0
# r_lst7 = []
# while i < anzahl:
#     rand = r.randrange(maxVal)
#     if rand in r_lst7:
#         continue
#     r_lst7.append(rand)
#     i += 1
# print("Stop", time.time() - t0)
# # Ergebniskontrolle:
# print("Anzahl Zahlen:", len(r_lst7), "- Als Set:", len(set(r_lst7)))
# # -- V2 --
# anzahl = 9900
# maxVal = 10000
# t0 = time.time()
# print("Start")
# # Hier kommt das Verfahren rein
# r_set = set()
# while len(r_set) < anzahl:
#     r_set.add(r.randrange(maxVal))
# print("Stop", time.time() - t0)
# # Ergebniskontrolle:
# print("Anzahl Zahlen (Set):", len(r_set))
# # -- V3 -- Laufzeitvergleich
# maxVal = 10000
# for anzahl in [9100, 9200, 9300, 9400, 9500, 9600, 9700, 9800, 9900]:
#     t0 = time.time()
#     n = 0
#     # Hier kommt das Verfahren rein
#     r_lst8 = list()
#     while len(r_lst8) < anzahl:
#         n += 1
#         rand = r.randrange(maxVal)
#         if rand not in r_lst8:
#             r_lst8.append(rand)
#     print(anzahl, n, time.time() - t0)
#     r_lst8.clear()
# # -- V4 -- Laufzeitvergleich set
# maxVal = 10000
# for anzahl in [9100, 9200, 9300, 9400, 9500, 9600, 9700, 9800, 9900]:
#     t0 = time.time()
#     n = 0
#     # Hier kommt das Verfahren rein
#     r_set2 = set()
#     while len(r_set2) < anzahl:
#         n += 1
#         rand = r.randrange(maxVal)
#         r_set2.add(rand)
#     print(anzahl, n, time.time() - t0)
#     r_set2.clear()
# # -- V5 -- Generieren Quell-Liste, herausziehen in Ziel-Liste
# maxVal = 10000
# for anzahl in [9100, 9200, 9300, 9400, 9500, 9600, 9700, 9800, 9900]:
#     n = 0
#     t0 = time.time()
#     # Hier kommt das Verfahren rein
#     src = list(range(maxVal))
#     dst = list()
#     while len(dst) < anzahl:
#         n += 1
#         i = r.randrange(len(src))
#         dst.append(src.pop(i))
#     print(anzahl, n, time.time() - t0)
#     dst.clear()
# # -- V6 --
# maxVal = 10000
# for anzahl in [9100, 9200, 9300, 9400, 9500, 9600, 9700, 9800, 9900]:
#     t0 = time.time()
#     # Hier kommt das Verfahren rein
#     r_range1 = range(maxVal)
#     r_lst9 = list(r_range1)
#     r.shuffle(r_lst9)
#     r_lst9 = r_lst9[:anzahl]
#     print(anzahl, time.time() - t0)
#     r_lst9.clear()


# Aufgabe S. 10
# 1 Anzahl Zeilen
f = open("data/moby.txt", "rt")
i = 0
for line in f: # die Datei ist zeilenweise iterierbar
    i+=1
    # i = 33460 Zeilen unbereinigt
f.close() # Datei schliessen (guter Ton)
# 2 bereinigen leerer Zeilen
f = open("data/moby.txt", "rt")
s_list = list()
for line in f:
    s_list.append(line)
f.close() # Datei schliessen (guter Ton)
# Neue Version:
s_list_c = list()
for line in s_list:
    if len(line) > 4:
        s_list_c.append(line) # Anzahl Zeilen 17141 bereinigt
# Folgendes schlecht gelöst! Nicht in Iteration Objekt verändern, über das iteriert wird, lieber neue Variable!
# for idx, line in enumerate(s_list):
#     if len(line) <= 4:
#         s_list.pop(idx) # Anzahl Zeilen 17852 bereinigt > nicht genug, falsch!
# Fix für schlechte Lösung? Rückwärts Index!
# enumeration = list(enumerate(s_list))
# enumeration.reverse()
# for (idx, line) in enumeration:
#     if len(line) <= 4:
#         s_list.pop(idx) # Anzahl Zeilen 17852 bereinigt > nicht genug, falsch!
# 3. Variante, besonders speichersparend
for i in range(len(s_list)-1, -1, -1):
    if len(s_list[i]) <= 4:
        s_list.pop(i)

# 3 - Wörter zählen
f = open("data/moby.txt", "rt")
s_list = list()
for line in f:
    s_list.append(line)
f.close() # Datei schliessen (guter Ton)
for i in range(len(s_list)-1, -1, -1):
    if len(s_list[i]) <= 4:
        s_list.pop(i)
words = list()
for line in s_list:
    words.extend(line.split())
# 4 - Anzahl Wörter jeweiliger Länge
# Dictionary nutzen, Wortlänge über Iteration prüfen, Prüfen ob Key existiert > Ja dann hochzählen, nein dann generieren mit 1
word_len_dic = dict()
for word in words:
    if len(word) in word_len_dic:
        word_len_dic[len(word)] += 1
    else:
        word_len_dic[len(word)] = 1
# V2 von Prof: Ohne if Anweisung, Zugriff über get, mit default RÜckgabe falls nicht vorhanden
word_len_dic2 = dict()
for word in words:
    l = len(word)
    word_len_dic2[l] = word_len_dic2.get(l, 0) + 1
# Anzahl einzelner Wörter
word_len_dic3 = dict()
for word in words:
    word_len_dic3[word] = word_len_dic3.get(word, 0) + 1
word_len_dic3_max = max(word_len_dic3.values())
word_len_dic3_len = len(word_len_dic3)

None


