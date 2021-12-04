
# Erstellen
lst01 = []
lst02 = [1,2,3,4,5]
lst03 = ["eins", "zwei", "drei", "vier", "fünf"]
lst04 = [1.0, 2.0, 3.0, 4.0, 5.0]
lst05 = [1, 2.0, "drei", True, None, [4,5], []]

# Manipulation: Anhängen
l1 = []
i = 0
while i < 5:
    l1.append(i+1)
    print(l1)
    i += 1
l2 = []
l2.extend(["eins", "zwei", "drei", "vier", "fünf", "sechs"])
l3 = []
l4 = []
l5 = []
l3.append(l1)
l3.append(l2)
print(l3)
l4.append(l1)
l4.extend(l2)
l5.extend(l1)
l5.extend(l2)

# Länge, Position, Teillisten
print(len(l1))
# ... für die anderen Listen
print(l2[0])
print(l2[2])
print(l5[5])
print(l2[5])
print(l2[-1])
laenge = len(l2)
print(l2[laenge-1])
print(l4[-1])
print(l4[-2])
print(l5[3:8])
print(l5[0:6])
print(l5[:6])
print(l5[4:])
print(l4[1][3]) # Falsch! 1. Element bei Index 0! 3. Element = Index 2! > Also l4[0][2]

# Bequemes
print(max(l1))
print(min(l1))
l1.extend((0,8))
print(max(l1))
print(min(l1))
# print(max(l5)) # Fehler! Kein Vergleich zwischen String und int möglich

# Manipulation: Diverses
l1.insert(3,12)
l1.pop(3)
l1.remove(8)
# l1.remove(8) # Fehler!
e = l1.pop(5)
l5.reverse()
l1.sort(key=None, reverse=True) # ???
l1.sort(key=None, reverse=False) # ???
l1 *= 3
print(l1)
l4 += l2

# Unveränderliche Datentypen: String
s1 = "ABCDE"
l1.append(s1)
l1.extend(s1)
s1 = s1 + s1
print(s1)
s1 += s1
print(s1)
# s2 = s1.pop(5) # Fehler!
s2 = s1[:4] + s1[5:] # Slicing + Verkettung
s2 = s1[5:]
# s1.pop() # Fehler!
s1 = s1[:-1] # Slicen und neu zuweisen!

# Unveränderliche Datentypen: Tuple
x = (1, 2)
(a, b) = (1, 2)
(a, b) = (b, a)
