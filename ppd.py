#1 Ruslanas
def prideti():
    pass
#2 Deividai
def papildyti():
    pass
#3 Gabrielius
def skaiciuoti_turinio_svori():
    pass
#4 Giedrius
def ar_iseina(saldytuvas):
    receptas = {}
    ivedimas = input("IVESKITE: ")
    def print_receptas(receptas):
        print("Receptas:")
        for ingredientas, kiekis in receptas.items():
        print(f"{ingredientas}: {kiekis}")
    ingridientu_sarasas = ivedimas.split(",")
    for ingredientas in ingridientu_sarasas:
        ingredientas1, kiekis = ingredientas.split(":")
        receptas[ingredientas1.strip()] = kiekis 
    return receptas
    print(print_receptas)

    
#5 Mindaugas
def turinys(saldytuvas):
    for daiktas, kiekis in saldytuvas.items():
        print("{} :{}".format(daiktas, kiekis))
    

saldytuvas = {"slyvos":3,"bananai":5,"pasikorusi ziurke":0.5,"kiausiniai":7,"pienas":2,"vanduo":4,"keciupas":1.2}
while True:
    pasirinkimas = input("0 - išeiti iš šaldytuvo\n1 - pridėti naują produktą\n2 - papildyti produkto kiekį\n3 - ištraukti produktą\n4 - peržiūrėti produktus\n5 - ieškoti produktų\n  pasirinkite:")
    if pasirinkimas == "0":
        break      
    elif pasirinkimas == "1": # Deivida
        produktas = input('Įveskite produktą: ')
        kiekis = float(input('Įveskite kiekį: '))
        saldytuvas[produktas]=kiekis
    elif pasirinkimas == "2": # Gabrielius
        print(saldytuvas)
        pildomas_produktas = input("Įveskite, kurį produktą norite papildyti: ")
        kiek_pildysim = float(input("Įveskite kiekį, kurį norite papildyti:"))
        saldytuvas[pildomas_produktas] += kiek_pildysim
        print((saldytuvas)[pildomas_produktas])
    elif pasirinkimas == "3": # Giedrius - istraukti produkta
        istraukimas_produktas = input("pasirinkite produkta: ")
        if not istraukimas_produktas in saldytuvas.keys():
            print("produkto nera")
        else:
            istraukimas_kiekis = float(input("pasirinkite kieki: "))
            if istraukimas_produktas in saldytuvas.keys() and saldytuvas[istraukimas_produktas] < istraukimas_kiekis:
                print("tiek daug produkto nera")
            if istraukimas_produktas in saldytuvas.keys() and saldytuvas[istraukimas_produktas] >= istraukimas_kiekis:
                saldytuvas[istraukimas_produktas] -= istraukimas_kiekis
            if saldytuvas[istraukimas_produktas] == 0:
                saldytuvas.pop(istraukimas_produktas)                 
    elif pasirinkimas == "4": # Mindaugas
        print(f"Šaldytuve yra: {turinys(saldytuvas)}")
    elif pasirinkimas == "5": # Ruslanas
        produktai = input('produkto paieška: ')
        if produktai in saldytuvas:
            print(f'{produktai} yra: {saldytuvas[produktai]}')
        else:
            print('produkto nera saldytuve')
    elif pasirinkimas == "7":
        ar_iseina(saldytuvas)