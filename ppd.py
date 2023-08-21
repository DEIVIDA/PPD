saldytuvas = {"slyvos" : "3", "bananai" :"5", "pasikorusi ziurke" : "0.5", "kiausiniai" :"7", }
while True:
    pasirinkimas = input("0 - išeiti iš šaldytuvo\n 1 - pridėti naują produktą\n 2 - papildyti produkto kiekį\n 3 - ištraukti produktą\n 4 - peržiūrėti produktus\n 5 - ieškoti produktų\n  pasirinkite:")
    if pasirinkimas == "0":
        break
       
    elif pasirinkimas == "1": # Deivida
        produktas = input('Įveskite produktą: ')
        kiekis=input('Įveskite kiekį: ')
        saldytuvas[produktas]=kiekis
        pass
    elif pasirinkimas == "2": # Gabrielius
        pass
    elif pasirinkimas == "3": # Giedrius
        pass
    elif pasirinkimas == "4": # Mindaugas
        print("Šaldytuve yra:")
        for daiktas, kiekis in saldytuvas.items():
            print("{} ({})".format(daiktas, kiekis))
        pass
    elif pasirinkimas == "5": # Ruslanas
        produktai = input('produkto paieška: ')
        while produktai in saldytuvas:
            print('produktas yra saldytuve')
            break
        else:
            print('produkto nera saldytuve')
            break