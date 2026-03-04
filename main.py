import translator as tr

t = tr.Translator()


while(True):

    t.printMenu()

    t.loadDictionary("dictionary.txt")

    txtIn = input("Inserire un  numero: ")

    # Add input control here!

    if int(txtIn) == 1:
        print()
        flag = True
        at = input("Inserisci la parola aliena e traduzione: ")

        parole = at.split()
        print(t.handleAdd(parole))
        pass
    if int(txtIn) == 2:
        p_aliena = input("cerca una traduzione: ")
        print(t.handleTranslate(p_aliena))
    if int(txtIn) == 3:
        pass
    if int(txtIn) == 4:
        break