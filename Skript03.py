# Aufgabe Klassen und Objekte Skript


class Kontobewegungen:
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
        if  issubclass(sender, Kontobewegungen):  # TODO: Function must handle object and string as input!
            self.sender = sender.name
        else:
            self.sender = sender
        if  issubclass(empfaenger, Kontobewegungen):
            self.empfaenger = empfaenger.name
        else:
            self.empfaenger = empfaenger
        self.betrag = betrag


class Konto(Kontobewegungen):
    def __init__(self, name, balance, dispo, creator):
        super().__init__()
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


Kontobew = Kontobewegungen()

k1 = Kontobew.new_konto('Fredi', 1000)
k2 = Kontobew.new_konto('Hans', 2000)

k1.einzahlen(500)

k2.transferieren(k1, 500)
k1.transferieren(k2, 300)

k3 = Kontobew.new_konto('Peter', 500, 200)
print(k3.auszahlen(600), k3.balance)
print(k3.auszahlen(600), k3.balance)

Kontobew.print_tranfers()
None
