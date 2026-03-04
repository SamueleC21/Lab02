class Dictionary:
    def __init__(self, dizionario):
        self.dizionario = dizionario

    def addWord(self, aliena, italiana):
        if aliena.isalpha() and italiana.isalpha():
            aliena.lower()
            italiana.lower()
            self.dizionario[aliena] = italiana
            return f"[{aliena}, {italiana}] \n Paola Aggiunta"
        else:
            return f"Parola non Aggiunta"

    def translate(self, chiave):    #parola italiana
        return self.dizionario[chiave]


    def translateWordWildCard(self):
        pass