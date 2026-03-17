import translator as tr

t = tr.Translator()
t.loadDictionary("dictionary.txt")

while(True):

    t.printMenu()

    txtIn = input("Inserire un  numero: ")

    # Add input control here!
    while int(txtIn) > 5 or int(txtIn) <= 0:
        txtIn = input("Numero errato - Inserire un  numero da 1 a 4: ")

    if int(txtIn) == 1:
        at = input("1 \ninserisci la parola aliena e italiana da aggiungere separati da spazio: ")
        parole = at.rstrip().split()
        t.handleAdd(parole)

    if int(txtIn) == 2:
        p_aliena = input("2 \ninserisci la parola aliena da tradurre: ")
        print(f"la traduzione di {p_aliena} è: ")
        t.handleTranslate(p_aliena)

    if int(txtIn) == 3:
        p_aliena = input("2 \ninserisci la parola aliena da tradurre con ?: ")
        if p_aliena.count("?") == 1:
            t.handleWildCard(p_aliena)

    if int(txtIn) == 4:
        t.stampa()

    if int(txtIn) == 5:
        break