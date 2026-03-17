class Dictionary:
    def __init__(self):
        self.dizionario = {}

    def addWord(self, aliena, italiane:list):
        if aliena.isalpha() and all(italiana.isalpha() for italiana in italiane):
            aliena = aliena.lower()
            italiane2 = [italiana.lower() for italiana in italiane]

            if aliena not in self.dizionario:
                self.dizionario[aliena] = italiane2
            else:
                self.dizionario[aliena].extend(italiane2)
            return True
        else:
            return False

    def translate(self, chiave):    #parola aliena
        traduzione = self.dizionario.get(chiave, "Non esiste")
        print(traduzione)

    def stampaDiz(self):
        for aliena, italiana in self.dizionario.items():
            print(aliena, italiana)

    def translateWordWildCard(self, query):
        traduzione = list()
        posizione = query.index("?")
        for chiave in self.dizionario.keys():
            if chiave[:posizione] == query[:posizione] and chiave[posizione+1:] == query[posizione+1:]:
                traduzione.extend(self.dizionario[chiave])
        print(traduzione)