saldytuvas = {"slyvos" : 3}
while True:
    pasirinkimas = input("pasirinkit: ")
    if pasirinkimas == "0":
        break

    elif pasirinkimas == "1": # Deivida
        pass
    elif pasirinkimas == "2": # Gabrielius
        pass
    elif pasirinkimas == "3": # Giedrius - istraukti produkta
        istraukimas_produktas = str(input("pasirinkite produkta: "))
        if not istraukimas_produktas in saldytuvas.keys():
            print("produkto nera")
        else:
            istraukimas_kiekis = int(input("pasirinkite kieki: "))
            if istraukimas_produktas in saldytuvas.keys() and saldytuvas[istraukimas_produktas] < istraukimas_kiekis:
                print("tiek daug produkto nera")
            if istraukimas_produktas in saldytuvas.keys() and saldytuvas[istraukimas_produktas] >= istraukimas_kiekis:
                saldytuvas[istraukimas_produktas] -= istraukimas_kiekis
            if saldytuvas[istraukimas_produktas] == 0:
                saldytuvas.pop(istraukimas_produktas)                 
    elif pasirinkimas == "4": # Mindaugas
        pass
    elif pasirinkimas == "5": # Ruslanas
        pass
