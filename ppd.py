'''
Parašykite programą šaldytuvas, kuri:

- saugo produktus žodyne, kur:
-- produkto pavadinimas yra raktas
-- kiekis yra reikšmė float

Tarkime, kad:
- kieti produktai matuojami kilogramais
- skysti litrais
- paruošti patiekalai matuojami vienetais
tokiu atveju, mums nereikia apibrėžti mato vieneto

Šaldytuvas turi meniu, per kurį galime:
- įdėti produktus
- išimti produktus
-- jeigu produkto kiekis tampa 0, ištriname
- peržiūrėti produktų sąrašą
- suskaičiuoti šaldytuvo turinio svorį
-- skystų tankis = 1
-- paruoštų patiekalų porcija sveria 1kg

BONUS:
Įterpti meniu punktą "ar išeina", kur vartotojo prašo įvesti:
- vienos porcijos receptą
-- įvedimo formatas: "ingredientas: kiekis" vienoje eilutėje.
- porcijų kiekį
Tada programa turėtų:
- išvesti, ar užtenka ingredientų patiekalams paruošti
- jeigu neužtenka, išvardinti ko ir kiek trūksta (shopping list).
- išvesti, kelioms porcijoms užtenka ingredientų, jei yra perteklius
'''
#3 Istraukti 
def istraukti_produkta(saldytuvas):
    istraukimas_produktas = input("pasirinkite produkta: ")
    if not istraukimas_produktas in saldytuvas.keys():
        print("produkto nera")
    else:
        istraukimas_kiekis = float(input("pasirinkite kieki: "))
        if saldytuvas[istraukimas_produktas] < istraukimas_kiekis:
            print("tiek daug produkto nera")
        if saldytuvas[istraukimas_produktas] >= istraukimas_kiekis:
            saldytuvas[istraukimas_produktas] -= istraukimas_kiekis
        if saldytuvas[istraukimas_produktas] == 0:
            saldytuvas.pop(istraukimas_produktas)
    return istraukimas_produktas

#1 Prideti nauja ir papildyti sena
def papildyti(saldytuvas):
    produktas = input('Įveskite produktą kurį norite papildyti arba prideti: ')
    kiekis = float(input('Įveskite produkto kiekį: '))
    if produktas in saldytuvas:
        saldytuvas[produktas] += kiekis
    else:
        saldytuvas[produktas] = kiekis
    return turinys(saldytuvas)

#2 Svoris
def skaiciuoti_turinio_svori(saldytuvas):
    svoris = sum(saldytuvas.values())
    return svoris

#6 Receptas
def ar_iseina(saldytuvas):
    ivedimas = input("Iveskite recepta: ")
    ingridientu_sarasas = ivedimas.split(",")
    uztenka = []
    for ingredientas in ingridientu_sarasas:
        ingredientas, kiekis = ingredientas.split(":")
        ingredientas = ingredientas.strip()
        kiekis = float(kiekis)
        if ingredientas in saldytuvas:
            if saldytuvas[ingredientas] - kiekis < 0:
                neuzteknka_kiekis = (saldytuvas[ingredientas] - kiekis) * (-1)
                print(f"{ingredientas} truksta: {neuzteknka_kiekis}")
                uztenka.append(False)
            else:
                uztenka.append(saldytuvas[ingredientas] / kiekis)
        else:
            uztenka.append(False)
    if False in uztenka:
        return print("neimanoma pagaminti")
    else:
        print(f"uztenka {min(uztenka)} porcijoms")
        return min(uztenka)

#4 Turinys
def turinys(saldytuvas):
    turi = "Šaldytuve yra:\n"  
    for daiktas, kiekis in saldytuvas.items():
        turi += "{} : {}\n".format(daiktas, kiekis)
    return turi  

#5 Ieskoti
def ieskoti_produktu(saldytuvas):
    produktai = input('produkto paieška: ')
    if produktai in saldytuvas:
        grizo = print(f'{produktai} yra: {saldytuvas[produktai]}')
    else:
        print('produkto nera saldytuve')
    return grizo
    
    
    
saldytuvas = {"slyvos":3,"bananai":5,"pasikorusi ziurke":0.5,"kiausiniai":7,"pienas":2,"vanduo":4,"keciupas":1.2}
while True:
    pasirinkimas = input("0 - išeiti iš šaldytuvo\n1 - Prideti nauja ir papildyti produktus\n2 - Skaiciuoti saldytuvo svori\n3 - ištraukti produktą\n4 - peržiūrėti produktus\n5 - ieškoti produktų\n6 - Receptas\npasirinkite:")
    if pasirinkimas == "0":
        print("Uzdarete saldytuva!")
        break
    elif pasirinkimas == "1": # Gabrielius
        print(papildyti(saldytuvas))
    elif pasirinkimas == "3": # Giedrius - istraukti produkta
        print(f"Istrauktas produktas: {istraukti_produkta(saldytuvas)}")            
    elif pasirinkimas == "4": # Mindaugas
        print(turinys(saldytuvas))
    elif pasirinkimas == "5": # Ruslanas
        ieskoti_produktu(saldytuvas)
    elif pasirinkimas == "6":
        ar_iseina(saldytuvas)
    elif pasirinkimas == "2":
        print(f"Šaldytuvo svoris: {skaiciuoti_turinio_svori(saldytuvas)}...")
        print("\n")
