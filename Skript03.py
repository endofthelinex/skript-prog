# Aufgabe Klassen und Objekte Skript


class Kontoverwaltung:
    def __init__(self):
        self.transfers = []
        self.konten = []

    def new_transfer(self, sender, empfaenger, betrag):
        self.transfers.append(Transfer_log(sender, empfaenger, betrag))
    def print_tranfers(self):
        for i in self.transfers:
            print(i.__dict__)

    def new_konto(self, name, balance = 0, dispo = 0):
        self.konten.append(Konto(name, balance, dispo, self))
        return self.konten[-1]


class Transfer_log:
    def __init__(self, sender, empfaenger, betrag):
        if isinstance(sender, Konto):
            self.sender = sender.name
        else:
            self.sender = sender
        if isinstance(empfaenger, Konto):
            self.empfaenger = empfaenger.name
        else:
            self.empfaenger = empfaenger
        self.betrag = betrag


class Konto(Kontoverwaltung):
    def __init__(self, name, balance, dispo, creator):
        self.name = name
        self.balance = balance
        self.dispo = dispo
        self.creator = creator

    def einzahlen(self, betrag):
        self.balance += betrag
        sender = 'Einzahlung'
        empfaenger = self
        self.creator.new_transfer(sender, empfaenger, betrag)

    def auszahlen(self, betrag):
        if (self.balance - betrag) > (0 - self.dispo):
            self.balance -= betrag
        else:
            betrag = self.balance + self.dispo
            self.balance = 0 - self.dispo
        sender = self
        empfaenger = 'Auszahlung'
        self.creator.new_transfer(sender, empfaenger, betrag)
        return betrag

    def transferieren(self, empfaenger, betrag):
        sender = self
        betrag = self.auszahlen(betrag)
        empfaenger.einzahlen(betrag)
        self.creator.new_transfer(sender, empfaenger, betrag)

    def guth(self):
        return self.dispo == 0

    istGuthabenKonto = property(guth)


Kontoverw = Kontoverwaltung()

k1 = Kontoverw.new_konto('Fredi', 1000)
k2 = Kontoverw.new_konto('Hans', 2000)

k1.einzahlen(500)

k2.transferieren(k1, 500)
k1.transferieren(k2, 300)

# Dispo Test
# k3 = Kontoverw.new_konto('Peter', 500, 200)
# print(k3.auszahlen(600), k3.balance)
# print(k3.auszahlen(600), k3.balance)

print('Guthabenkonto?', k1.istGuthabenKonto)

Kontoverw.print_tranfers()
None
