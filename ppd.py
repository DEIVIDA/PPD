print("\n")
saldytuvas = {
    "Mėsa:": {
        "kumpis" : 4,
        "dešra" : 2
    },
    "Vaisiai:": {
        "bananai" : 1,
        "mandarinai" : 4,
        "obuoliai" : 8
    },
    "Pieno produktai:" : {
        "pienas" : 1,
        "varškė" : 4
    }
}
print("****ŠALDYTUVAS****")
for produktas, kiekis in saldytuvas.items():
    print(produktas)
    for produktas_antras, kiekis_antras in kiekis.items():
        print(f"   {produktas_antras} : {kiekis_antras}")
print("\n")
print("*****VALDYMO PULTAS*******")
print("1 - pridėti naują produktą")
print("2 - papildyti produkto kiekį")
print("3 - ištraukti produktą nurodant jo kiekį")
print("4 - peržiūrėti produktus")
print("5 - ieškoti produktų")
print("0 - išėjimas")
print("\n")
'''
meniu = [
    ("1", "pridėti naują produktą"),
    ("2", "papildyti produkto kiekį"),
    ("3", "ištraukti produktą nurodant jo kiekį"),
    ("4", "peržiūrėti produktus"),
    ("5", "ieškoti produktų"),
    ("0", "išėjimas")
]
titulas = "***** VALDYMO PULTAS *****"
print(titulas)
for pasirinkimas in meniu:
    print(f"{pasirinkimas[0]:<2} - {pasirinkimas[1]}")
'''
while True:
    pasirinkimas = input("Pasirinkite: ")
    print("\n")
    if pasirinkimas == "0":
        print("Iki pasimatymo!")
        break  
    elif pasirinkimas == "1": 
        print("Į kokį skyrių norite pridėti produktą?")
        for indeksas, (indeksas_kitas, vidus) in enumerate(saldytuvas.items()):
            print(indeksas + 1, indeksas_kitas[:-1].lower())
        print("\n")
        pridejimo_skyrius = int(input("Įveskite šaldytuvo skyriaus numerį, kurį papildysite: "))
        pasirinktas_pridejimo_skyrius = list(saldytuvas.keys())[pridejimo_skyrius - 1]
        print("\n")
        produkto_pavadinimas = input("Įveskite produkto pavadinimą, kurį norite įdėti: ")
        print("\n")
        produkto_kiekis = float(input("Įrašykite pridedamo produkto kiekį: "))
        print("\n")
        saldytuvas[pasirinktas_pridejimo_skyrius][produkto_pavadinimas] = produkto_kiekis
        print(f"Produktas: '{produkto_pavadinimas}' pridėtas prie skyriaus '{pasirinktas_pridejimo_skyrius[:-1].lower()}'.")
        print("\n")
        print(saldytuvas)
    elif pasirinkimas == "2": 
        print("Kurį šaldytuvo skyrių norite papildyti?")
        for indeksas, (indeksas_kitas, vidus) in enumerate(saldytuvas.items()):
            print(indeksas + 1, indeksas_kitas[:-1].lower())
        print("\n")
        indeks = int(input("Įveskite šaldytuvo skyrių, kurį norite papildyti: ")) - 1
        pasirinktas_skyrius = list(saldytuvas.keys())[indeks]
        print(f"Pasirinkote pildyti skyrių: '{pasirinktas_skyrius[:-1].lower()}'.")
        print("\n")
        print("Šiame skyriuje yra(skliaustuose - kiekis): ")
        for indeksas, (produktas, kiekis) in enumerate(saldytuvas[pasirinktas_skyrius].items()):
            print(f"{indeksas + 1} {produktas} ({kiekis})")
        print("\n")
        produktas_indeksas = int(input("Įveskite produkto numerį, kurį norite papildyti: ")) - 1
        produktas_pasirinkimas = list(saldytuvas[pasirinktas_skyrius].keys())[produktas_indeksas]
        print("\n")
        if produktas_pasirinkimas in saldytuvas[pasirinktas_skyrius]:
            kiek_papildysim = float(input("Įveskite kiekį, kuriuo norite papildyti pasirinktą produktą: "))
            saldytuvas[pasirinktas_skyrius][produktas_pasirinkimas] += kiek_papildysim
            print(f"Papildėte produktą: '{produktas_pasirinkimas}'. Dabar turite: {saldytuvas[pasirinktas_skyrius][produktas_pasirinkimas]}...")
        print("\n")
        print(saldytuvas)

        #    for indeksas in enumerate(saldytuvas):
            
        #sujungtas = ("\n".join(f"{k}\t{v}" for k, v in saldytuvas.items()))
        #for i in enumerate(sujungtas):
        #   print(i)
        #for produktas in saldytuvas:
            #ivedimas = input(f"Iveskite {}")
            #if produktas == "slyvos":
               # skaicius = int(input("Iveskite papildymą"))
                # saldytuvas["slyvos"] = skaicius
        pass
    elif pasirinkimas == "3":
        print("Iš kurio skyriaus norite ištraukti produktą? ")
        for indeksas, (indeksas_kitas, vidus) in enumerate(saldytuvas.items()):
            print(indeksas + 1, indeksas_kitas[:-1].lower())
        print("\n")
        pasirinkti_skyriaus_indeksas = int(input("Įveskite šaldytuvo skyriaus numerį: ")) - 1
        pasirinktas_skyrius = list(saldytuvas.keys())[pasirinkti_skyriaus_indeksas]
        print("\n")
        print("Šiame skyriuje yra(skliaustuose - kiekis): ")
        for indeksas, (produktas, kiekis) in enumerate(saldytuvas[pasirinktas_skyrius].items()):
            print(f"{indeksas + 1} {produktas} ({kiekis})")
        print("\n")
        produkto_indeksas = int(input("Įveskite produkto numerį: ")) - 1
        pasirinktas_produktas = list(saldytuvas[pasirinktas_skyrius].keys())[produkto_indeksas]
        print("\n")
        if pasirinktas_produktas in saldytuvas[pasirinktas_skyrius]:
            kiek_isimsim = float(input("Įveskite pasirinkti produkto kiekį, kurį išimsite: "))
            print("\n")
            if kiek_isimsim >= saldytuvas[pasirinktas_skyrius][pasirinktas_produktas]:
                del saldytuvas[pasirinktas_skyrius][pasirinktas_produktas]
                print(f"Ištraukėte visą produktą: '{pasirinktas_produktas}'...")
                print("\n")
            else:
                saldytuvas[pasirinktas_skyrius][pasirinktas_produktas] -= kiek_isimsim
                print(f"Ištraukėte iš produkto '{pasirinktas_produktas}' {kiek_isimsim} kiekį. Dabar šaldytuve liko: {saldytuvas[pasirinktas_skyrius][pasirinktas_produktas]}...")
                print("\n")
        else:
            print(f"Produktas '{pasirinktas_produktas}' nerastas šiame skyriuje.")
        print("\n")
        print(saldytuvas)
    elif pasirinkimas == "4": 
        print("****KAS VIDUJE?****")
        for produktas, kiekis in saldytuvas.items():
            print(produktas)
            for produktas_antras, kiekis_antras in kiekis.items():
                print(f"   {produktas_antras} : {kiekis_antras}")
        print("\n")
    elif pasirinkimas == "5":
        ieskomas_produktas = input("Įveskite produktą, kurį norite surasti: ")
        rastas = False
        print("\n")
        for skyrius, produktai in saldytuvas.items():
            for produktas, kiekis in produktai.items():
                if ieskomas_produktas.lower() in produktas.lower():
                    print(f"Produktas '{produktas}' rastas skyriuje '{skyrius[:-1].lower()}', turimas kiekis yra {kiekis}...")
                    rastas = True
        print("\n")
        if not rastas:
            print("Tokio produkto nėra.")
            print("\n")
        pass
    #naujasaa
