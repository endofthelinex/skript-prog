# Aufgabe Klassen und Objekte Skript


class Kontobewegungen:
    def __init__(self):
        self.transfers = []
        self.konten = []

    def new_transfer(self, sender, empfaenger, betrag):
        self.transfers.append(Transfer_log(sender, empfaenger, betrag))  # TODO Konto findet transfers nicht bei Aufruf aus Unterklasse!!

    def print_tranfers(self):
        for i in self.transfers:
            print(i.__dict__)

    def new_konto(self, name, balance = 0, dispo = 0):
        self.konten.append(Konto(name, balance, dispo))
        return self.konten[-1]


class Transfer_log:
    def __init__(self, sender, empfaenger, betrag):
        self.sender = sender
        self.empfaenger = empfaenger
        self.betrag = betrag


class Konto(Kontobewegungen):
    def __init__(self, name, balance, dispo):
        super().__init__()
        self.name = name
        self.balance = balance
        self.dispo = dispo

    def einzahlen(self, betrag):
        self.balance += betrag

    def auszahlen(self, betrag):
        if (self.balance - betrag) > (0 - self.dispo):
            self.balance -= betrag
            return betrag
        else:
            self.balance = 0 - self.dispo
            return self.balance + self.dispo

    def transferieren(self, empfaenger, betrag):
        sender = self
        betrag = self.auszahlen(betrag)
        empfaenger.einzahlen(betrag)
        super().new_transfer(sender, empfaenger, betrag)


Kontobew = Kontobewegungen()

k1 = Kontobew.new_konto('Fredi', 1000)
k2 = Kontobew.new_konto('Hans', 2000)

k1.einzahlen(500)

k2.transferieren(k1, 500)

Kontobew.print_tranfers()
