import dictionary as di
class Translator:
    def __init__(self):
        dizionario = {}
        self.d = di.Dictionary(dizionario)

    def printMenu(self):
        print("------------------------------------------------")
        print("           Translater Alien-Italian")
        print("------------------------------------------------")
        print ("1- Aggiungi nuova parola")
        print ("2- Cerca una traduzione")
        print ("3- Cerca una wildcard")
        print ("4- exit")

    def loadDictionary(self, nomeFile):
        with open(nomeFile, "r") as file:
            for riga in file:
                campiRiga = riga.split()
                self.d.addWord(campiRiga[0], campiRiga[1])
        pass

    def handleAdd(self, entry):
        return self.d.addWord(entry[0], entry[1])
        pass

    def handleTranslate(self, query): #parola italiana - string
       return self.d.translate(query)


    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass