import dictionary as di
class Translator:
    def __init__(self):
        self.d = di.Dictionary()

    def printMenu(self):
        print("------------------------------------------------")
        print("           Translater Alien-Italian")
        print("------------------------------------------------")
        print ("1- Aggiungi nuova parola")
        print ("2- Cerca una traduzione")
        print ("3- Cerca una wildcard")
        print ("4- Stamoa tutto il dizionario")
        print ("5- exit")

    def loadDictionary(self, nomeFile):
        with open(nomeFile, "r") as file:
            for riga in file:
                campiRiga = riga.rstrip().split()
                self.d.addWord(campiRiga[0], campiRiga[1].split())

    def handleAdd(self, entry):
        flag = self.d.addWord(entry[0], entry[1:])
        if flag:
            print("Parola aggiunta correttamente")
        else:
            print("Parola NON aggiunta")

    def handleTranslate(self, query): #query is a string parola_aliena
        self.d.translate(query)

    def stampa(self):
        self.d.stampaDiz()


    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        self.d.translateWordWildCard(query)